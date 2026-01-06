# Math Operations

This repository contains Python functions for performing basic math operations (addition and subtraction) along with automated tests and CI/CD integration.

## Files

- **src/math_operations.py**: Contains functions for addition and subtraction.
- **tests/test_add.py**: Pytest file for testing the addition function.
- **tests/test_subtract.py**: Pytest file for testing the subtraction function.
- **math.json**: Metadata file for CI/CD workflows.
- **requirements.txt**: Contains the dependencies for the project.

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run tests using `pytest tests/`.

## CI/CD Workflow

The repository is configured for automated testing using GitHub Actions. Any changes to the repository will trigger the CI workflow defined in `.github/workflows/ci.yml`.