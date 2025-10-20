"""
Methodology Auditor
Detects circular logic, missing validation, and other methodological issues in research code
"""

import ast
import re
from typing import List, Dict, Tuple, Set
from dataclasses import dataclass
from pathlib import Path


@dataclass
class MethodologyIssue:
    """Represents a methodological issue found in code"""
    severity: str  # 'critical', 'major', 'minor'
    category: str  # 'circular_logic', 'missing_validation', etc.
    description: str
    location: str  # file:line
    recommendation: str
    
    def __str__(self):
        return f"[{self.severity.upper()}] {self.category} at {self.location}\n  {self.description}\n  → {self.recommendation}"


class MethodologyAuditor:
    """
    Audits research code for methodological issues
    """
    
    def __init__(self):
        self.issues: List[MethodologyIssue] = []
        
        # Patterns indicating circular validation
        self.circular_patterns = [
            (r'def.*validate.*\(', r'self\..*\('),  # validate method calling same class methods
            (r'pattern.*match', r'validate.*pattern'),  # pattern matching validating patterns
            (r'model\.predict', r'validate.*model'),  # model validating itself
            (r'confidence', r'validate.*confidence'),  # confidence validating confidence
        ]
        
        # Patterns indicating missing validation
        self.missing_validation_patterns = [
            r'def\s+measure\s*\(',
            r'def\s+detect\s*\(',
            r'def\s+score\s*\(',
            r'def\s+evaluate\s*\(',
        ]
        
        # Patterns indicating statistical issues
        self.statistical_red_flags = [
            (r'p\s*<\s*0\.05', 'p-value without effect size'),
            (r'significant', 'significance claim without details'),
            (r'\.mean\(\)', 'mean without standard deviation/CI'),
        ]
    
    def audit_file(self, filepath: str) -> List[MethodologyIssue]:
        """Audit a single Python file"""
        self.issues = []
        
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Check for circular validation
            self._check_circular_validation(content, filepath)
            
            # Check for missing validation
            self._check_missing_validation(content, filepath)
            
            # Check for statistical issues
            self._check_statistical_issues(content, filepath)
            
            # Check for reproducibility issues
            self._check_reproducibility(content, filepath)
            
            # Parse AST for deeper analysis
            try:
                tree = ast.parse(content)
                self._check_ast(tree, filepath)
            except SyntaxError:
                pass  # Skip files with syntax errors
            
        except Exception as e:
            print(f"Error auditing {filepath}: {e}")
        
        return self.issues
    
    def audit_directory(self, dirpath: str) -> Dict[str, List[MethodologyIssue]]:
        """Audit all Python files in a directory"""
        results = {}
        
        for filepath in Path(dirpath).rglob("*.py"):
            issues = self.audit_file(str(filepath))
            if issues:
                results[str(filepath)] = issues
        
        return results
    
    def _check_circular_validation(self, content: str, filepath: str):
        """Check for circular validation patterns"""
        lines = content.split('\n')
        
        # Look for validation methods
        validation_methods = []
        for i, line in enumerate(lines, 1):
            if re.search(r'def.*(validate|validation|verify)', line.lower()):
                validation_methods.append((i, line))
        
        # Check if validation uses same methods as measurement
        for line_num, line in validation_methods:
            # Get the method body (simplified - just look at nearby lines)
            method_body = '\n'.join(lines[line_num:min(line_num+20, len(lines))])
            
            # Check for circular patterns
            if re.search(r'self\.(detect|measure|score)', method_body):
                self.issues.append(MethodologyIssue(
                    severity='critical',
                    category='circular_logic',
                    description='Validation method calls measurement method from same class',
                    location=f'{filepath}:{line_num}',
                    recommendation='Validate against independent ground truth, not self-generated data'
                ))
            
            # Check for pattern-based validation
            if re.search(r'pattern', method_body.lower()) and re.search(r'pattern', line.lower()):
                self.issues.append(MethodologyIssue(
                    severity='critical',
                    category='circular_logic',
                    description='Pattern matching appears to validate pattern matching',
                    location=f'{filepath}:{line_num}',
                    recommendation='Validate against expert annotations, not pattern presence'
                ))
    
    def _check_missing_validation(self, content: str, filepath: str):
        """Check for measurement methods without validation"""
        lines = content.split('\n')
        
        # Find measurement methods
        measurement_methods = []
        for i, line in enumerate(lines, 1):
            for pattern in self.missing_validation_patterns:
                if re.search(pattern, line):
                    measurement_methods.append((i, line))
        
        # Check if there's any validation
        has_validation = any(
            re.search(r'(validate|validation|ground.truth)', content.lower())
        )
        
        if measurement_methods and not has_validation:
            for line_num, line in measurement_methods:
                self.issues.append(MethodologyIssue(
                    severity='critical',
                    category='missing_validation',
                    description='Measurement method found but no validation against ground truth',
                    location=f'{filepath}:{line_num}',
                    recommendation='Implement validation against independent ground truth before using measure'
                ))
    
    def _check_statistical_issues(self, content: str, filepath: str):
        """Check for statistical red flags"""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for p-values without effect sizes
            if re.search(r'p\s*[<>=]', line.lower()):
                # Look for effect size in nearby lines
                context = '\n'.join(lines[max(0, i-5):min(len(lines), i+5)])
                if not re.search(r'(cohen|effect.size|confidence.interval)', context.lower()):
                    self.issues.append(MethodologyIssue(
                        severity='major',
                        category='statistical_issue',
                        description='P-value reported without effect size or confidence interval',
                        location=f'{filepath}:{i}',
                        recommendation='Always report effect sizes with confidence intervals alongside p-values'
                    ))
            
            # Check for significance claims
            if re.search(r'significant', line.lower()) and not re.search(r'#', line):
                self.issues.append(MethodologyIssue(
                    severity='major',
                    category='statistical_issue',
                    description='Significance claim without statistical details',
                    location=f'{filepath}:{i}',
                    recommendation='Provide complete statistical details: test used, p-value, effect size, CI'
                ))
    
    def _check_reproducibility(self, content: str, filepath: str):
        """Check for reproducibility issues"""
        lines = content.split('\n')
        
        # Check for random operations without seeds
        has_random = False
        has_seed = False
        
        for i, line in enumerate(lines, 1):
            if re.search(r'(random|shuffle|sample|choice)', line.lower()):
                has_random = True
            if re.search(r'(seed|random_state)', line.lower()):
                has_seed = True
        
        if has_random and not has_seed:
            self.issues.append(MethodologyIssue(
                severity='major',
                category='reproducibility',
                description='Random operations without seed specification',
                location=f'{filepath}',
                recommendation='Set random seed for reproducibility: np.random.seed(42) or random_state=42'
            ))
        
        # Check for hardcoded values without documentation
        for i, line in enumerate(lines, 1):
            # Look for magic numbers in important contexts
            if re.search(r'(threshold|alpha|beta|learning_rate)\s*=\s*[0-9.]+', line):
                # Check if there's a comment explaining it
                if not re.search(r'#', line):
                    self.issues.append(MethodologyIssue(
                        severity='minor',
                        category='reproducibility',
                        description='Hyperparameter without documentation',
                        location=f'{filepath}:{i}',
                        recommendation='Document why this value was chosen'
                    ))
    
    def _check_ast(self, tree: ast.AST, filepath: str):
        """Check AST for deeper issues"""
        
        # Find all class definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self._check_class(node, filepath)
    
    def _check_class(self, node: ast.ClassDef, filepath: str):
        """Check a class for methodological issues"""
        
        # Find measurement and validation methods
        measure_methods = []
        validate_methods = []
        
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                name = item.name.lower()
                if any(keyword in name for keyword in ['measure', 'detect', 'score', 'evaluate']):
                    measure_methods.append(item)
                if any(keyword in name for keyword in ['validate', 'verify', 'check']):
                    validate_methods.append(item)
        
        # If there are measurement methods but no validation
        if measure_methods and not validate_methods:
            self.issues.append(MethodologyIssue(
                severity='critical',
                category='missing_validation',
                description=f'Class {node.name} has measurement methods but no validation',
                location=f'{filepath}:{node.lineno}',
                recommendation='Add validation method that checks against independent ground truth'
            ))
        
        # Check if validation methods call measurement methods (circular)
        for validate_method in validate_methods:
            for measure_method in measure_methods:
                # Check if validation calls measurement
                for subnode in ast.walk(validate_method):
                    if isinstance(subnode, ast.Call):
                        if isinstance(subnode.func, ast.Attribute):
                            if subnode.func.attr == measure_method.name:
                                self.issues.append(MethodologyIssue(
                                    severity='critical',
                                    category='circular_logic',
                                    description=f'Validation method {validate_method.name} calls measurement method {measure_method.name}',
                                    location=f'{filepath}:{validate_method.lineno}',
                                    recommendation='Validate against independent ground truth, not self-generated measurements'
                                ))
    
    def generate_report(self) -> str:
        """Generate a human-readable report"""
        if not self.issues:
            return "✓ No methodological issues found!"
        
        # Group by severity
        critical = [i for i in self.issues if i.severity == 'critical']
        major = [i for i in self.issues if i.severity == 'major']
        minor = [i for i in self.issues if i.severity == 'minor']
        
        report = "=" * 80 + "\n"
        report += "METHODOLOGY AUDIT REPORT\n"
        report += "=" * 80 + "\n\n"
        
        report += f"Total Issues: {len(self.issues)}\n"
        report += f"  Critical: {len(critical)}\n"
        report += f"  Major: {len(major)}\n"
        report += f"  Minor: {len(minor)}\n\n"
        
        if critical:
            report += "CRITICAL ISSUES (Must Fix Before Publication)\n"
            report += "-" * 80 + "\n"
            for issue in critical:
                report += str(issue) + "\n\n"
        
        if major:
            report += "MAJOR ISSUES (Should Fix)\n"
            report += "-" * 80 + "\n"
            for issue in major:
                report += str(issue) + "\n\n"
        
        if minor:
            report += "MINOR ISSUES (Nice to Fix)\n"
            report += "-" * 80 + "\n"
            for issue in minor:
                report += str(issue) + "\n\n"
        
        report += "=" * 80 + "\n"
        report += "RECOMMENDATIONS\n"
        report += "=" * 80 + "\n\n"
        
        if critical:
            report += "1. Address all CRITICAL issues before proceeding\n"
            report += "   - Circular logic undermines all findings\n"
            report += "   - Missing validation means measures are unvalidated\n\n"
        
        if major:
            report += "2. Fix MAJOR issues to strengthen claims\n"
            report += "   - Statistical issues weaken credibility\n"
            report += "   - Reproducibility issues prevent verification\n\n"
        
        if minor:
            report += "3. Consider fixing MINOR issues for completeness\n"
            report += "   - Improves documentation and clarity\n\n"
        
        return report


def audit_project(project_path: str, output_file: str = None):
    """
    Audit an entire project for methodological issues
    """
    auditor = MethodologyAuditor()
    results = auditor.audit_directory(project_path)
    
    # Generate report
    report = auditor.generate_report()
    
    # Print to console
    print(report)
    
    # Save to file if requested
    if output_file:
        with open(output_file, 'w') as f:
            f.write(report)
        print(f"\nReport saved to {output_file}")
    
    # Return summary
    return {
        'total_issues': len(auditor.issues),
        'critical': len([i for i in auditor.issues if i.severity == 'critical']),
        'major': len([i for i in auditor.issues if i.severity == 'major']),
        'minor': len([i for i in auditor.issues if i.severity == 'minor']),
        'files_with_issues': len(results)
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python methodology_auditor.py <project_path> [output_file]")
        sys.exit(1)
    
    project_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    summary = audit_project(project_path, output_file)
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files audited: {summary['files_with_issues']}")
    print(f"Total issues: {summary['total_issues']}")
    print(f"  Critical: {summary['critical']}")
    print(f"  Major: {summary['major']}")
    print(f"  Minor: {summary['minor']}")
    
    if summary['critical'] > 0:
        print("\n⚠️  CRITICAL ISSUES FOUND - Do not proceed without fixing")
        sys.exit(1)
    elif summary['major'] > 0:
        print("\n⚠️  MAJOR ISSUES FOUND - Should fix before publication")
        sys.exit(0)
    else:
        print("\n✓ No critical or major issues found")
        sys.exit(0)
