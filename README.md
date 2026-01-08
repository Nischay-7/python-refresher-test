# Python Refresher - Cave of Craft Project

A project-based learning experience to refresh and strengthen your Python skills through hands-on coding challenges.

## Project Overview

This project is designed to guide you through Python fundamentals in a structured, stage-by-stage approach. Each stage builds upon the previous one, helping you master Python concepts through practical implementation.

## Project Structure

```
python-refresher/
├── project/              # Your code goes here
│   ├── hello_world.py   # Stage 0: Hello World
│   └── main.py          # Main entry point (future stages)
├── tests/               # Stage-wise test suites
│   └── s0/             # Stage 0 tests
│       └── test_hello_world.py
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation:**
   ```bash
   pytest --version
   ```

## Stage 0: Hello World

### Objective
Create a function that prints "Hello, World!" to the console.

### Instructions

1. Open `project/hello_world.py`
2. Implement the `hello_world()` function to print "Hello, World!"
3. Run the tests to verify your implementation:
   ```bash
   pytest tests/s0/ -v
   ```

### Running Stage-Specific Tests

You can run tests for a specific stage using:

```bash
# Run Stage 0 tests
pytest tests/s0/ -v

# Run all tests
pytest -v

# Run with more detailed output
pytest tests/s0/ -v -s

# Run tests and output JSON to stdout
python run_stage_tests.py 0 --json

# Run tests and save JSON report to file
python run_stage_tests.py 0 --json-report report.json
```

### Expected Output

When you run the tests, you should see:
```
tests/s0/test_hello_world.py::test_hello_world_output PASSED
tests/s0/test_hello_world.py::test_hello_world_is_function PASSED
tests/s0/test_hello_world.py::test_hello_world_exact_output PASSED
```

## Testing

This project uses [pytest](https://docs.pytest.org/) as the testing framework. Tests are organized by stage in the `tests/` directory.

### Running Tests

- **All tests:** `pytest`
- **Specific stage:** `pytest tests/s0/`
- **With coverage:** `pytest --cov=project tests/`
- **Verbose output:** `pytest -v`

## Project Stages

- **Stage 0:** Hello World ✅ (Current)
- **Stage 1:** Coming soon...
- **Stage 2:** Coming soon...

## Tips

- Read the test files to understand what's expected
- Run tests frequently to catch errors early
- Check the TODO comments in the project files for guidance
- Don't hesitate to experiment and learn!

## Support

For issues or questions about this project, refer to the Cave of Craft platform documentation.

---

**Happy Coding! 🚀**
