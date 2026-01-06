# Math Operations

This repository contains basic mathematical operations (addition and subtraction) implemented in Python. It also includes pytest files for comprehensive testing.

## Files

1. **math_operations.py**: Contains the `add` and `subtract` functions.
2. **test_add.py**: Contains pytest test cases for the `add` function.
3. **test_subtract.py**: Contains pytest test cases for the `subtract` function.

## Usage

### Running the Functions

Import the functions from `math_operations.py` and use them in your Python code:

```python
from math_operations import add, subtract

result_add = add(3, 5)  # Returns 8
result_subtract = subtract(10, 5)  # Returns 5
```

### Running Tests

To run the tests, navigate to the `src` folder and execute:

```bash
pytest test_add.py
pytest test_subtract.py
```

## Workflow

1. Clone the repository.
2. Navigate to the `src` folder.
3. Run the tests using pytest to verify functionality.

## Contribution

Feel free to contribute by adding more functions or improving the existing ones. Create a pull request for review.

## License

This project is licensed under the MIT License.