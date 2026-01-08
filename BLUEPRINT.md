# Blueprint Documentation

This document describes the blueprint structure for the Python Refresher project.

## Blueprint Structure

```
python-refresher/
├── project/                    # Student code directory
│   ├── __init__.py            # Package initialization
│   ├── hello_world.py         # Stage 0: Hello World implementation
│   └── main.py                # Main entry point (for future stages)
│
├── tests/                      # Test suites organized by stage
│   ├── __init__.py            # Tests package initialization
│   └── s0/                    # Stage 0 tests
│       ├── __init__.py        # Stage 0 package initialization
│       └── test_hello_world.py # Stage 0 test cases
│
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Python dependencies
├── run_stage_tests.py         # Helper script for stage-wise testing
├── .gitignore                 # Git ignore patterns
├── README.md                  # Project documentation
└── BLUEPRINT.md              # This file
```

## Design Principles

### 1. Stage-Based Organization
- Tests are organized in `tests/s0/`, `tests/s1/`, etc.
- Each stage has its own test directory
- Students can run tests for specific stages independently

### 2. Clear Separation
- `project/` contains student implementation code
- `tests/` contains test suites that verify student code
- Clear boundaries prevent students from modifying tests

### 3. Progressive Learning
- Each stage builds upon previous concepts
- Tests guide students on expected behavior
- TODO comments in code files provide hints

### 4. Standard Tooling
- Uses pytest (industry-standard Python testing framework)
- Follows Python package structure conventions
- Includes proper `__init__.py` files for package imports

## Stage 0: Hello World

### Objective
Students learn to:
- Create a Python function
- Use the `print()` statement
- Understand function structure and syntax

### Implementation File
- `project/hello_world.py` - Contains a `hello_world()` function stub with TODO comments

### Test File
- `tests/s0/test_hello_world.py` - Contains three test cases:
  1. `test_hello_world_output` - Verifies correct output
  2. `test_hello_world_is_function` - Verifies it's a callable function
  3. `test_hello_world_exact_output` - Verifies exact string match

### Running Tests

**Option 1: Using pytest directly**
```bash
pytest tests/s0/ -v
```

**Option 2: Using the helper script**
```bash
python run_stage_tests.py 0
```

**Option 3: Run all tests**
```bash
pytest -v
# or
python run_stage_tests.py all
```

## Adding New Stages

To add a new stage (e.g., Stage 1):

1. **Create stage directory:**
   ```bash
   mkdir -p tests/s1
   touch tests/s1/__init__.py
   ```

2. **Create test file:**
   ```bash
   touch tests/s1/test_<stage_name>.py
   ```
   (Use a descriptive name following the `test_*.py` pattern)

3. **Add implementation file(s) in `project/`:**
   - Create new Python files or modify existing ones
   - Add TODO comments with instructions

4. **Update `pytest.ini`:**
   - Add marker for the new stage: `stage1: Stage 1 tests description`

5. **Update `README.md`:**
   - Add stage description and instructions

## Test Design Guidelines

### Test Naming
- Use descriptive names: `test_<functionality>_<aspect>`
- Example: `test_hello_world_output`, `test_hello_world_is_function`

### Test Structure
- One test per assertion/behavior
- Use clear docstrings explaining what's being tested
- Provide helpful error messages in assertions

### Test Independence
- Each test should be independent
- Tests should not rely on execution order
- Use fixtures for shared setup (if needed)

## Integration with Cave of Craft Platform

### Expected Behaviors
1. **GitHub Template:** This blueprint will be used as a GitHub template
2. **Progress Tracking:** Platform tracks which stage students are on
3. **Test Execution:** Platform can run `pytest tests/s<N>/` to verify completion
4. **Stage Completion:** When all tests pass, student can proceed to next stage

### Platform Integration Points
- Stage completion is determined by passing all tests in a stage directory
- Test output can be parsed to show progress
- Students can run tests locally before submitting

## Dependencies

- **pytest>=7.0.0** - Testing framework
- **pytest-cov>=4.0.0** - Coverage reporting (optional)

Install with: `pip install -r requirements.txt`

## Best Practices for Students

1. **Read the tests first** - They show what's expected
2. **Run tests frequently** - Catch errors early
3. **Read TODO comments** - They provide guidance
4. **Check error messages** - They often point to the solution
5. **Experiment** - Try different approaches

## Future Enhancements

Potential additions for future stages:
- Stage 1: Variables and data types
- Stage 2: Control flow (if/else, loops)
- Stage 3: Functions and parameters
- Stage 4: Data structures (lists, dictionaries)
- Stage 5: File I/O
- Stage 6: Error handling
- Stage 7: Object-oriented programming
- Stage 8: Modules and packages

---

**Note:** This blueprint is designed to be extensible. New stages can be added following the same pattern without disrupting existing stages.

