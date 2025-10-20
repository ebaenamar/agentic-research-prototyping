---
name: experiment-design-skill
description: Rigorous experimental design and execution for foundational models research. Ensures reproducibility, proper controls, statistical validity, and meaningful results. Use after methodology validation to implement and execute experiments correctly.
---

# Experiment Design & Execution

Rigorous approach to designing and executing experiments on foundational models.

## Core Principles

1. **Reproducibility First**: Every detail documented
2. **Proper Controls**: Isolate what you're testing
3. **Statistical Validity**: Adequate power, proper tests
4. **Honest Reporting**: All results, not just favorable

## Pre-Experiment Checklist

Before running ANY experiment:

- [ ] Research question clearly defined
- [ ] Hypotheses pre-specified
- [ ] Measures validated against ground truth
- [ ] Statistical analysis plan written
- [ ] Sample size justified (power analysis)
- [ ] Control conditions specified
- [ ] Reproducibility plan complete
- [ ] Data collection protocol documented

**If ANY item unchecked, STOP and complete it first.**

## Experimental Design

### 1. Define Experimental Conditions

**For each condition, specify:**

```markdown
## Condition: [Name]

**Purpose:** [What this condition tests]

**Configuration:**
- Model: [exact model name/version]
- Parameters:
  - temperature: [value]
  - top_p: [value]
  - max_tokens: [value]
  - [all other parameters]
- Prompt: [exact prompt text]
- System message: [if applicable]

**Rationale:** [Why these settings]

**Expected Outcome:** [What you expect to see]
```

### 2. Control Conditions

**Types of Controls:**

1. **Baseline**: Standard approach without your intervention
2. **Negative Control**: Should show no effect
3. **Positive Control**: Should show known effect
4. **Ablation**: Remove components to test necessity

**For each control:**
```markdown
## Control: [Name]

**Type:** [Baseline/Negative/Positive/Ablation]

**Purpose:** [What this controls for]

**Configuration:** [Exact settings]

**Expected Result:** [What should happen]
```

### 3. Variables

**Independent Variables (What you manipulate):**
```markdown
| Variable | Type | Levels | Operationalization |
|----------|------|--------|-------------------|
| [Name] | [Categorical/Continuous] | [Values] | [How implemented] |
```

**Dependent Variables (What you measure):**
```markdown
| Variable | Type | Range | Measurement Method | Validated? |
|----------|------|-------|-------------------|-----------|
| [Name] | [Type] | [Range] | [How measured] | [Yes/No + metrics] |
```

**Confounds (What you control):**
```markdown
| Confound | Why Control | How Controlled |
|----------|-------------|----------------|
| [Name] | [Rationale] | [Method] |
```

### 4. Sample Selection

**Sampling Strategy:**

```markdown
## Sample Selection

**Population:** [What you're sampling from]

**Sampling Method:** [Random/Stratified/Systematic]

**Sample Size:** [N per condition]
- Justification: [Power analysis]
- Minimum: [Below which underpowered]

**Inclusion Criteria:**
- [Criterion 1]
- [Criterion 2]

**Exclusion Criteria:**
- [Criterion 1]
- [Criterion 2]

**Stratification:** [If applicable]
- Strata: [e.g., by domain, difficulty]
- Rationale: [Why stratify]
```

### 5. Randomization

**Randomization Plan:**

```markdown
## Randomization

**What is randomized:**
- [e.g., Order of conditions]
- [e.g., Assignment to conditions]
- [e.g., Sample selection]

**Method:**
- Random seed: [specific seed value]
- Generator: [numpy.random, random, etc.]
- Algorithm: [how randomization done]

**Verification:**
- [ ] Balance check across conditions
- [ ] No systematic differences
```

## Implementation

### 1. Code Structure

**Required Structure:**

```python
# experiment_config.py
"""
Complete experimental configuration
All parameters in one place for reproducibility
"""

EXPERIMENT_CONFIG = {
    'name': 'experiment_name',
    'version': '1.0',
    'date': '2025-10-19',
    
    # Random seeds for reproducibility
    'random_seed': 42,
    'numpy_seed': 42,
    'torch_seed': 42,
    
    # Model configuration
    'models': {
        'gpt4': {
            'name': 'gpt-4-turbo-2024-04-09',
            'temperature': 0.7,
            'top_p': 0.95,
            'max_tokens': 1000,
            'frequency_penalty': 0.0,
            'presence_penalty': 0.0
        },
        # ... other models
    },
    
    # Experimental conditions
    'conditions': {
        'baseline': {
            'description': 'Standard generation',
            'prompt_template': 'prompts/baseline.txt',
            'system_message': 'You are a helpful assistant.'
        },
        'intervention': {
            'description': 'With our intervention',
            'prompt_template': 'prompts/intervention.txt',
            'system_message': 'You are a helpful assistant.'
        }
    },
    
    # Sample configuration
    'sample': {
        'size_per_condition': 100,
        'stratification': 'domain',
        'domains': ['cs', 'bio', 'physics']
    },
    
    # Measurement configuration
    'measures': {
        'primary': {
            'name': 'bias_score',
            'validated': True,
            'validation_f1': 0.75
        }
    }
}
```

### 2. Reproducibility Requirements

**Every experiment MUST have:**

```python
# Set all random seeds
import random
import numpy as np
import torch

def set_seeds(seed=42):
    """Set all random seeds for reproducibility"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    # Set deterministic behavior
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

# Call at start of experiment
set_seeds(EXPERIMENT_CONFIG['random_seed'])
```

**Log everything:**

```python
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'experiment_{datetime.now()}.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log all important events
logger.info(f"Starting experiment: {EXPERIMENT_CONFIG['name']}")
logger.info(f"Configuration: {EXPERIMENT_CONFIG}")
logger.info(f"Random seed: {EXPERIMENT_CONFIG['random_seed']}")
```

### 3. Data Collection Protocol

**Structured Data Collection:**

```python
class ExperimentRunner:
    """
    Runs experiments with full logging and error handling
    """
    
    def __init__(self, config):
        self.config = config
        self.results = []
        self.errors = []
        
    def run_experiment(self):
        """Run complete experiment"""
        
        # Log start
        logger.info("Starting experiment")
        
        # For each condition
        for condition_name, condition_config in self.config['conditions'].items():
            logger.info(f"Running condition: {condition_name}")
            
            # For each sample
            for sample_id, sample in enumerate(self.get_samples()):
                try:
                    # Run trial
                    result = self.run_trial(
                        sample=sample,
                        condition=condition_config,
                        trial_id=f"{condition_name}_{sample_id}"
                    )
                    
                    # Store result
                    self.results.append(result)
                    
                except Exception as e:
                    # Log error but continue
                    logger.error(f"Error in trial {sample_id}: {e}")
                    self.errors.append({
                        'trial_id': f"{condition_name}_{sample_id}",
                        'error': str(e)
                    })
        
        # Save results
        self.save_results()
        
    def run_trial(self, sample, condition, trial_id):
        """Run single trial with full logging"""
        
        start_time = datetime.now()
        
        # Generate response
        response = self.generate_response(sample, condition)
        
        # Measure outcome
        measurements = self.measure_outcomes(response)
        
        end_time = datetime.now()
        
        # Return complete trial data
        return {
            'trial_id': trial_id,
            'condition': condition['description'],
            'sample': sample,
            'response': response,
            'measurements': measurements,
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'duration': (end_time - start_time).total_seconds(),
            'config': condition  # Store exact config used
        }
```

### 4. Quality Control

**During Experiment:**

```python
class QualityControl:
    """Monitor experiment quality in real-time"""
    
    def __init__(self):
        self.checks = []
        
    def check_response_quality(self, response):
        """Check if response is valid"""
        issues = []
        
        # Check length
        if len(response.split()) < 10:
            issues.append("Response too short")
        
        # Check for errors
        if "error" in response.lower():
            issues.append("Error in response")
        
        # Check for completion
        if not response.strip():
            issues.append("Empty response")
        
        return issues
    
    def check_measurement_validity(self, measurement):
        """Check if measurement is valid"""
        issues = []
        
        # Check range
        if not (0 <= measurement <= 1):
            issues.append("Measurement out of range")
        
        # Check for NaN
        if np.isnan(measurement):
            issues.append("Measurement is NaN")
        
        return issues
```

## Execution

### 1. Pilot Run

**Before full experiment:**

```markdown
## Pilot Run

**Purpose:** Test experimental setup

**Sample Size:** 10-20 per condition

**Checks:**
- [ ] All conditions run without errors
- [ ] Measurements produce valid values
- [ ] Logging captures all necessary info
- [ ] Time per trial reasonable
- [ ] Data format correct

**Issues Found:** [Document any issues]

**Fixes Applied:** [Document fixes]

**Ready for Full Run:** [Yes/No]
```

### 2. Full Experiment

**Execution Checklist:**

- [ ] Pilot run completed successfully
- [ ] All code reviewed and tested
- [ ] Configuration file finalized
- [ ] Random seeds set
- [ ] Logging configured
- [ ] Storage space available
- [ ] Backup plan in place
- [ ] Monitoring in place

**Run Protocol:**

```bash
# 1. Set up environment
python -m venv exp_env
source exp_env/bin/activate
pip install -r requirements.txt

# 2. Verify configuration
python verify_config.py

# 3. Run experiment
python run_experiment.py --config experiment_config.py

# 4. Monitor progress
tail -f experiment_*.log

# 5. Verify completion
python verify_results.py
```

### 3. Error Handling

**Handle Errors Gracefully:**

```python
def run_with_retry(func, max_retries=3, delay=1):
    """Run function with retries"""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                logger.error(f"All retries failed")
                raise
```

## Data Management

### 1. Data Storage

**Structure:**

```
experiments/
├── config/
│   └── experiment_config.py
├── data/
│   ├── raw/
│   │   └── responses_YYYYMMDD.json
│   ├── processed/
│   │   └── measurements_YYYYMMDD.csv
│   └── metadata/
│       └── experiment_metadata.json
├── logs/
│   └── experiment_YYYYMMDD.log
├── results/
│   ├── statistics/
│   └── figures/
└── code/
    ├── run_experiment.py
    └── analyze_results.py
```

### 2. Data Format

**Standardized Format:**

```json
{
  "experiment": {
    "name": "experiment_name",
    "version": "1.0",
    "date": "2025-10-19",
    "config": {...}
  },
  "trials": [
    {
      "trial_id": "baseline_001",
      "condition": "baseline",
      "sample": {...},
      "response": "...",
      "measurements": {
        "bias_score": 0.35,
        "quality_score": 7.5
      },
      "metadata": {
        "timestamp": "2025-10-19T10:00:00",
        "duration": 2.5,
        "model_version": "gpt-4-turbo-2024-04-09"
      }
    }
  ],
  "errors": [...]
}
```

## Analysis Preparation

### 1. Data Verification

**Before Analysis:**

```python
def verify_data(results):
    """Verify data integrity"""
    
    checks = {
        'complete': check_completeness(results),
        'valid': check_validity(results),
        'balanced': check_balance(results),
        'quality': check_quality(results)
    }
    
    return checks

def check_completeness(results):
    """Check all trials completed"""
    expected = EXPERIMENT_CONFIG['sample']['size_per_condition']
    actual = len(results)
    return actual >= expected

def check_validity(results):
    """Check all measurements valid"""
    for result in results:
        for measure, value in result['measurements'].items():
            if not is_valid_measurement(value):
                return False
    return True
```

### 2. Data Cleaning

**Document All Cleaning:**

```python
class DataCleaner:
    """Clean data with full documentation"""
    
    def __init__(self):
        self.cleaning_log = []
    
    def clean(self, data):
        """Clean data and log all changes"""
        
        cleaned = data.copy()
        
        # Remove invalid trials
        invalid = self.identify_invalid(cleaned)
        if invalid:
            self.cleaning_log.append({
                'action': 'remove_invalid',
                'count': len(invalid),
                'ids': invalid
            })
            cleaned = self.remove_trials(cleaned, invalid)
        
        # Handle outliers
        outliers = self.identify_outliers(cleaned)
        if outliers:
            self.cleaning_log.append({
                'action': 'handle_outliers',
                'method': 'winsorize',
                'count': len(outliers),
                'ids': outliers
            })
            cleaned = self.handle_outliers(cleaned, outliers)
        
        return cleaned, self.cleaning_log
```

## Quality Gates

**Before proceeding to analysis:**

- [ ] All trials completed
- [ ] Data verified and cleaned
- [ ] Cleaning documented
- [ ] No systematic errors
- [ ] Balance across conditions verified
- [ ] Measurements validated
- [ ] All data saved with backups

## Next Phase

Once experiment is complete and data verified:
→ Proceed to **Results Analysis** (results-analysis-skill)

Bring forward:
- Complete experimental data
- Configuration files
- Cleaning log
- Quality control reports
- Statistical analysis plan
