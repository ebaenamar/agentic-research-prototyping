"""
Validated Measurement Framework
Prevents circular logic by enforcing independent validation
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, cohen_kappa_score
)
import json
from datetime import datetime


@dataclass
class GroundTruthDataset:
    """
    Ground truth dataset with independent annotations
    """
    samples: List[Any]
    labels: List[Any]
    metadata: Dict[str, Any]
    
    def __post_init__(self):
        if len(self.samples) != len(self.labels):
            raise ValueError("Samples and labels must have same length")
        
        # Validate inter-rater reliability if provided
        if 'inter_rater_reliability' in self.metadata:
            kappa = self.metadata['inter_rater_reliability'].get('cohens_kappa', 0)
            if kappa < 0.7:
                raise ValueError(
                    f"Inter-rater reliability (κ={kappa:.2f}) below threshold 0.7. "
                    "Ground truth may not be reliable."
                )
    
    def split(self, train_ratio=0.6, val_ratio=0.2, test_ratio=0.2, seed=42):
        """Split into train/val/test sets"""
        if not np.isclose(train_ratio + val_ratio + test_ratio, 1.0):
            raise ValueError("Ratios must sum to 1.0")
        
        n = len(self.samples)
        indices = np.random.RandomState(seed).permutation(n)
        
        train_end = int(n * train_ratio)
        val_end = train_end + int(n * val_ratio)
        
        train_idx = indices[:train_end]
        val_idx = indices[train_end:val_end]
        test_idx = indices[val_end:]
        
        return (
            GroundTruthDataset(
                [self.samples[i] for i in train_idx],
                [self.labels[i] for i in train_idx],
                {**self.metadata, 'split': 'train'}
            ),
            GroundTruthDataset(
                [self.samples[i] for i in val_idx],
                [self.labels[i] for i in val_idx],
                {**self.metadata, 'split': 'validation'}
            ),
            GroundTruthDataset(
                [self.samples[i] for i in test_idx],
                [self.labels[i] for i in test_idx],
                {**self.metadata, 'split': 'test'}
            )
        )


@dataclass
class ValidationMetrics:
    """
    Validation metrics for a measure
    """
    accuracy: float
    precision: float
    recall: float
    f1: float
    cohens_kappa: float
    confusion_matrix: np.ndarray
    confidence_intervals: Dict[str, Tuple[float, float]]
    sample_size: int
    timestamp: str
    
    def meets_threshold(self, min_f1=0.7, min_kappa=0.6) -> bool:
        """Check if metrics meet minimum thresholds"""
        return self.f1 >= min_f1 and self.cohens_kappa >= min_kappa
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            'accuracy': float(self.accuracy),
            'precision': float(self.precision),
            'recall': float(self.recall),
            'f1': float(self.f1),
            'cohens_kappa': float(self.cohens_kappa),
            'confusion_matrix': self.confusion_matrix.tolist(),
            'confidence_intervals': self.confidence_intervals,
            'sample_size': self.sample_size,
            'timestamp': self.timestamp
        }


class ValidatedMeasure(ABC):
    """
    Abstract base class for validated measures
    Enforces validation before use
    """
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.is_validated = False
        self.validation_metrics: Optional[ValidationMetrics] = None
        self.ground_truth_source: Optional[str] = None
        self.limitations: List[str] = []
    
    @abstractmethod
    def _measure_impl(self, sample: Any) -> Any:
        """
        Internal measurement implementation
        Subclasses must implement this
        """
        pass
    
    def measure(self, sample: Any) -> Any:
        """
        Public measurement method
        Only callable after validation
        """
        if not self.is_validated:
            raise RuntimeError(
                f"Cannot use measure '{self.name}' before validation. "
                f"Call validate_against_ground_truth() first."
            )
        
        return self._measure_impl(sample)
    
    def measure_batch(self, samples: List[Any]) -> List[Any]:
        """Measure multiple samples"""
        if not self.is_validated:
            raise RuntimeError(
                f"Cannot use measure '{self.name}' before validation."
            )
        
        return [self._measure_impl(sample) for sample in samples]
    
    def validate_against_ground_truth(
        self,
        ground_truth: GroundTruthDataset,
        min_f1: float = 0.7,
        min_kappa: float = 0.6
    ) -> ValidationMetrics:
        """
        Validate measure against independent ground truth
        
        Args:
            ground_truth: Independent ground truth dataset
            min_f1: Minimum F1 score threshold
            min_kappa: Minimum Cohen's kappa threshold
        
        Returns:
            ValidationMetrics object
        
        Raises:
            ValueError: If validation metrics below threshold
        """
        if ground_truth is None:
            raise ValueError("Cannot validate without ground truth dataset")
        
        if len(ground_truth.samples) < 30:
            raise ValueError(
                f"Ground truth dataset too small (n={len(ground_truth.samples)}). "
                f"Need at least 30 samples for reliable validation."
            )
        
        # Get predictions
        predictions = [self._measure_impl(sample) for sample in ground_truth.samples]
        labels = ground_truth.labels
        
        # Calculate metrics
        metrics = self._calculate_metrics(predictions, labels)
        
        # Check thresholds
        if not metrics.meets_threshold(min_f1, min_kappa):
            raise ValueError(
                f"Validation failed for '{self.name}':\n"
                f"  F1: {metrics.f1:.3f} (threshold: {min_f1})\n"
                f"  Cohen's κ: {metrics.cohens_kappa:.3f} (threshold: {min_kappa})\n"
                f"Measure is not valid for use."
            )
        
        # Store validation results
        self.is_validated = True
        self.validation_metrics = metrics
        self.ground_truth_source = ground_truth.metadata.get('source', 'unknown')
        
        print(f"✓ Measure '{self.name}' validated successfully:")
        print(f"  F1: {metrics.f1:.3f}")
        print(f"  Cohen's κ: {metrics.cohens_kappa:.3f}")
        print(f"  Accuracy: {metrics.accuracy:.3f}")
        
        return metrics
    
    def _calculate_metrics(
        self,
        predictions: List[Any],
        labels: List[Any]
    ) -> ValidationMetrics:
        """Calculate validation metrics"""
        
        # Convert to binary if needed
        pred_binary = [1 if p > 0.5 else 0 for p in predictions] if isinstance(predictions[0], float) else predictions
        
        # Calculate metrics
        acc = accuracy_score(labels, pred_binary)
        prec = precision_score(labels, pred_binary, average='weighted', zero_division=0)
        rec = recall_score(labels, pred_binary, average='weighted', zero_division=0)
        f1 = f1_score(labels, pred_binary, average='weighted', zero_division=0)
        kappa = cohen_kappa_score(labels, pred_binary)
        cm = confusion_matrix(labels, pred_binary)
        
        # Calculate confidence intervals (bootstrap)
        ci = self._bootstrap_confidence_intervals(predictions, labels)
        
        return ValidationMetrics(
            accuracy=acc,
            precision=prec,
            recall=rec,
            f1=f1,
            cohens_kappa=kappa,
            confusion_matrix=cm,
            confidence_intervals=ci,
            sample_size=len(labels),
            timestamp=datetime.now().isoformat()
        )
    
    def _bootstrap_confidence_intervals(
        self,
        predictions: List[Any],
        labels: List[Any],
        n_bootstrap: int = 1000,
        confidence: float = 0.95
    ) -> Dict[str, Tuple[float, float]]:
        """Calculate bootstrap confidence intervals"""
        
        n = len(predictions)
        f1_scores = []
        
        for _ in range(n_bootstrap):
            # Resample with replacement
            indices = np.random.choice(n, n, replace=True)
            pred_sample = [predictions[i] for i in indices]
            label_sample = [labels[i] for i in indices]
            
            # Convert to binary if needed
            pred_binary = [1 if p > 0.5 else 0 for p in pred_sample] if isinstance(pred_sample[0], float) else pred_sample
            
            # Calculate F1
            f1 = f1_score(label_sample, pred_binary, average='weighted', zero_division=0)
            f1_scores.append(f1)
        
        # Calculate confidence intervals
        alpha = 1 - confidence
        lower = np.percentile(f1_scores, alpha/2 * 100)
        upper = np.percentile(f1_scores, (1 - alpha/2) * 100)
        
        return {
            'f1': (lower, upper)
        }
    
    def add_limitation(self, limitation: str):
        """Document a limitation of this measure"""
        self.limitations.append(limitation)
    
    def get_validation_report(self) -> str:
        """Generate validation report"""
        if not self.is_validated:
            return f"Measure '{self.name}' has not been validated."
        
        report = f"""
Validation Report: {self.name}
{'=' * 60}

Description: {self.description}

Ground Truth Source: {self.ground_truth_source}

Validation Metrics (n={self.validation_metrics.sample_size}):
  Accuracy:     {self.validation_metrics.accuracy:.3f}
  Precision:    {self.validation_metrics.precision:.3f}
  Recall:       {self.validation_metrics.recall:.3f}
  F1 Score:     {self.validation_metrics.f1:.3f}
  Cohen's κ:    {self.validation_metrics.cohens_kappa:.3f}

Confidence Intervals (95%):
  F1: [{self.validation_metrics.confidence_intervals['f1'][0]:.3f}, 
       {self.validation_metrics.confidence_intervals['f1'][1]:.3f}]

Confusion Matrix:
{self.validation_metrics.confusion_matrix}

Limitations:
"""
        for i, limitation in enumerate(self.limitations, 1):
            report += f"  {i}. {limitation}\n"
        
        if not self.limitations:
            report += "  (No limitations documented)\n"
        
        report += f"\nValidated: {self.validation_metrics.timestamp}\n"
        
        return report
    
    def save_validation(self, filepath: str):
        """Save validation results to file"""
        if not self.is_validated:
            raise RuntimeError("Cannot save validation before validating")
        
        data = {
            'name': self.name,
            'description': self.description,
            'ground_truth_source': self.ground_truth_source,
            'validation_metrics': self.validation_metrics.to_dict(),
            'limitations': self.limitations,
            'is_validated': self.is_validated
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Validation results saved to {filepath}")


class CircularValidationDetector:
    """
    Detects circular logic in validation
    """
    
    @staticmethod
    def check_independence(
        measure_method: str,
        ground_truth_method: str
    ) -> Tuple[bool, str]:
        """
        Check if ground truth is independent of measure
        
        Returns:
            (is_independent, explanation)
        """
        
        # Red flags for circular validation
        circular_patterns = [
            ("pattern matching", "pattern matching"),
            ("dictionary", "dictionary"),
            ("same model", "same model"),
            ("self-reported", "self-reported"),
            ("model confidence", "model output"),
        ]
        
        measure_lower = measure_method.lower()
        gt_lower = ground_truth_method.lower()
        
        for measure_pattern, gt_pattern in circular_patterns:
            if measure_pattern in measure_lower and gt_pattern in gt_lower:
                return False, (
                    f"Circular validation detected: "
                    f"Measure uses '{measure_pattern}' and "
                    f"ground truth uses '{gt_pattern}'. "
                    f"Validation must be independent."
                )
        
        return True, "Validation appears independent"
    
    @staticmethod
    def validate_ground_truth_quality(metadata: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate ground truth quality
        
        Returns:
            (is_valid, issues)
        """
        issues = []
        
        # Check inter-rater reliability
        if 'inter_rater_reliability' in metadata:
            kappa = metadata['inter_rater_reliability'].get('cohens_kappa', 0)
            if kappa < 0.7:
                issues.append(
                    f"Inter-rater reliability (κ={kappa:.2f}) below threshold 0.7"
                )
        else:
            issues.append("Inter-rater reliability not reported")
        
        # Check sample size
        if 'sample_size' in metadata:
            n = metadata['sample_size']
            if n < 100:
                issues.append(
                    f"Sample size (n={n}) below recommended minimum of 100"
                )
        else:
            issues.append("Sample size not reported")
        
        # Check annotator count
        if 'num_annotators' in metadata:
            num = metadata['num_annotators']
            if num < 3:
                issues.append(
                    f"Number of annotators ({num}) below minimum of 3"
                )
        else:
            issues.append("Number of annotators not reported")
        
        # Check if annotation guidelines exist
        if not metadata.get('has_annotation_guidelines', False):
            issues.append("Annotation guidelines not documented")
        
        return len(issues) == 0, issues


# Example usage
if __name__ == "__main__":
    
    # Example: Bias detection measure
    class BiasDetector(ValidatedMeasure):
        def __init__(self):
            super().__init__(
                name="confirmation_bias_detector",
                description="Detects confirmation bias in peer review text"
            )
            
            # Document limitations upfront
            self.add_limitation(
                "Only validated on academic peer reviews in computer science"
            )
            self.add_limitation(
                "May not generalize to other domains or review types"
            )
            self.add_limitation(
                "Cannot distinguish between legitimate criticism and bias in all cases"
            )
        
        def _measure_impl(self, sample: str) -> float:
            """
            Simplified bias detection
            In practice, this would be more sophisticated
            """
            # This is just an example - real implementation would be more complex
            bias_indicators = [
                'however', 'unfortunately', 'disappointing',
                'fails to', 'lacks', 'insufficient'
            ]
            
            text_lower = sample.lower()
            count = sum(1 for indicator in bias_indicators if indicator in text_lower)
            
            # Normalize by length
            words = len(sample.split())
            bias_score = min(count / max(words * 0.05, 1), 1.0)
            
            return bias_score
    
    # Create detector
    detector = BiasDetector()
    
    # Try to use before validation (should fail)
    try:
        detector.measure("This paper is disappointing.")
    except RuntimeError as e:
        print(f"✓ Correctly prevented use before validation: {e}\n")
    
    # Create ground truth (in practice, this would come from expert annotations)
    samples = [
        "This paper presents interesting results.",
        "Unfortunately, this work fails to address key limitations.",
        "The methodology is sound and well-justified.",
        "However, the authors lack understanding of the domain.",
    ] * 10  # Repeat to get enough samples
    
    # Simulated expert labels (0 = no bias, 1 = bias present)
    labels = [0, 1, 0, 1] * 10
    
    ground_truth = GroundTruthDataset(
        samples=samples,
        labels=labels,
        metadata={
            'source': 'Expert annotations',
            'num_annotators': 3,
            'inter_rater_reliability': {'cohens_kappa': 0.75},
            'sample_size': len(samples),
            'has_annotation_guidelines': True
        }
    )
    
    # Check for circular validation
    is_independent, explanation = CircularValidationDetector.check_independence(
        measure_method="pattern matching on bias indicators",
        ground_truth_method="independent expert annotations"
    )
    print(f"Independence check: {explanation}\n")
    
    # Validate
    try:
        metrics = detector.validate_against_ground_truth(ground_truth, min_f1=0.6)
        
        # Now we can use it
        test_text = "Unfortunately, this paper fails to meet expectations."
        bias_score = detector.measure(test_text)
        print(f"\nBias score for test text: {bias_score:.3f}")
        
        # Print validation report
        print(detector.get_validation_report())
        
    except ValueError as e:
        print(f"Validation failed: {e}")
