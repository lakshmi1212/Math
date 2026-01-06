# Math Operations

This repository provides basic math operations such as addition and subtraction. It is integrated with a CI pipeline for automated testing.

## Usage

- `add(a, b)`: Returns the sum of two numbers.
- `subtract(a, b)`: Returns the difference when the second number is subtracted from the first.

## Workflow

The repository includes a CI workflow that triggers tests on every `push` or `pull_request` to the `main` branch.

### Steps:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run tests using `pytest`.

## CI/CD
The `.github/workflows/ci.yml` file defines the CI pipeline for this project.
