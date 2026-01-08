#!/usr/bin/env python3
"""
Helper script to run stage-specific tests for the Python Refresher project.

Usage:
    python run_stage_tests.py 0                    # Run Stage 0 tests
    python run_stage_tests.py 1                    # Run Stage 1 tests (when available)
    python run_stage_tests.py all                  # Run all tests
    python run_stage_tests.py 0 --json             # Run Stage 0 tests, output JSON to stdout
    python run_stage_tests.py 0 --json report.json # Run Stage 0 tests, save JSON to file
    python run_stage_tests.py 0 --json-report report.json  # Alternative format
"""

import sys
import subprocess
import json
import argparse
from pathlib import Path


def run_stage_tests(stage, json_output=None, json_file=None):
    """
    Run tests for a specific stage.
    
    Args:
        stage: Stage number or "all"
        json_output: If True, output JSON to stdout
        json_file: If provided, save JSON report to this file
    
    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    project_root = Path(__file__).parent
    
    if stage == "all":
        test_path = project_root / "tests"
        if not json_output and not json_file:
            print(f"Running all tests...")
    else:
        try:
            stage_num = int(stage)
            test_path = project_root / "tests" / f"s{stage_num}"
            
            if not test_path.exists():
                error_msg = f"Error: Stage {stage_num} tests not found at {test_path}"
                if json_output:
                    print(json.dumps({"error": error_msg, "available_stages": get_available_stages()}))
                else:
                    print(error_msg)
                    print(f"Available stages: {get_available_stages()}")
                return 1
                
            if not json_output and not json_file:
                print(f"Running Stage {stage_num} tests...")
        except ValueError:
            error_msg = f"Error: Invalid stage number '{stage}'"
            if json_output:
                print(json.dumps({"error": error_msg}))
            else:
                print(error_msg)
                print("Usage: python run_stage_tests.py <stage_number|all> [--json] [--json-report FILE]")
            return 1
    
    # Build pytest command
    cmd = ["pytest", str(test_path), "-v"]
    
    # Determine JSON report file location
    json_report_file = None
    temp_file_created = False
    
    if json_output or json_file:
        if json_file:
            # Use specified file
            json_report_file = str(json_file)
        else:
            # Create temporary file for stdout output
            import tempfile
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
            temp_file.close()
            json_report_file = temp_file.name
            temp_file_created = True
        
        cmd.extend(["--json-report", "--json-report-file", json_report_file])
    
    # Run pytest
    if json_output or json_file:
        # Capture output when JSON mode is enabled
        result = subprocess.run(
            cmd, 
            cwd=project_root,
            capture_output=True,
            text=True
        )
    else:
        # Normal mode - let output go to stdout
        result = subprocess.run(cmd, cwd=project_root)
    
    # If JSON output requested, read and print JSON
    if json_output or json_file:
        try:
            with open(json_report_file, 'r') as f:
                json_data = json.load(f)
            
            # If outputting to stdout, print the JSON
            if json_output:
                print(json.dumps(json_data, indent=2))
            
            # Clean up temporary file if we created one
            if temp_file_created:
                import os
                try:
                    os.unlink(json_report_file)
                except OSError:
                    pass
                    
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # Fallback: create our own JSON structure
            json_data = {
                "error": f"Failed to read JSON report: {str(e)}",
                "exit_code": result.returncode,
                "stage": stage,
                "stdout": result.stdout if hasattr(result, 'stdout') else "",
                "stderr": result.stderr if hasattr(result, 'stderr') else "",
                "passed": result.returncode == 0
            }
            if json_output:
                print(json.dumps(json_data, indent=2))
            
            # Clean up temporary file if we created one
            if temp_file_created:
                import os
                try:
                    os.unlink(json_report_file)
                except OSError:
                    pass
    
    return result.returncode


def get_available_stages():
    """Get list of available test stages."""
    project_root = Path(__file__).parent
    tests_dir = project_root / "tests"
    
    if not tests_dir.exists():
        return []
    
    stages = []
    for item in tests_dir.iterdir():
        if item.is_dir() and item.name.startswith("s") and item.name[1:].isdigit():
            stages.append(int(item.name[1:]))
    
    return sorted(stages)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run stage-specific tests for the Python Refresher project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_stage_tests.py 0
  python run_stage_tests.py 0 --json
  python run_stage_tests.py 0 --json-report report.json
  python run_stage_tests.py all --json
        """
    )
    parser.add_argument(
        "stage",
        help="Stage number (e.g., 0, 1, 2) or 'all' to run all stages"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output test results as JSON to stdout"
    )
    parser.add_argument(
        "--json-report",
        metavar="FILE",
        help="Save JSON test report to the specified file"
    )
    
    args = parser.parse_args()
    
    exit_code = run_stage_tests(
        args.stage,
        json_output=args.json,
        json_file=args.json_report
    )
    sys.exit(exit_code)

