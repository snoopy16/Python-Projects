## Python Practice Projects
**Author:** Nidhi Tare


## Introduction

This repository contains a collection of beginner-to-intermediate Python practice scripts and algorithms, including file parsing, number and string manipulation, data structures, recursion, and classic programming exercises. Each script is self-contained, uses clear inputs and outputs, and is accompanied by comprehensive unit tests.

Python Projects from Practice Python - https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

***

## Features

- **File operations:** Reading and writing files line by line.
- **Math algorithms:** Factorial, Fibonacci, sum of list, palindrome detection, divisor enumeration, and more.
- **List operations:** Filtering, removing duplicates, finding intersections, and list comprehensions.
- **Games:** Rock-Paper-Scissors.
- **String processing:** Substring generation, anagram detection, palindrome checks.
- **Unit tests:** Each module is covered with thorough unit tests using Python’s `unittest`.
- **Beginner-friendly code:** Each script is written clearly, well-commented, and self-explanatory for easy learning.

***

## Project Structure

```
.
├── Numbers/
│   ├── palindrome.py
│   ├── removeduplicatesfromlist.py
│   ├── twosum.py
├── Recursion/
│   ├── factorial.py
│   ├── fibonacci.py
│   ├── listSum.py
├── StringManupulation/
│   ├── PossibleSubstrings.py
│   ├── VowelSubstrings.py
├── tests/
│   ├── test_factorial.py
│   ├── test_fibonacci.py
│   ├── test_listsum.py
│   ├── test_numbers.py
│   ├── test_removeduplicatesfromlist.py
│   ├── test_twosum.py
│   ├── test_possiblesubstrings.py
│   ├── test_vowelsubstrings.py
└── README.md
```

***

## How to Run the Code

1. **Clone the repo:**
    ```bash
    git clone git@github.com:snoopy16/Python-Projects.git
    cd Python-Projects
    ```

2. **Run any script directly:**
    ```bash
    python Numbers/palindrome.py
    python Recursion/factorial.py
    ```

***

## How to Run Unit Tests

All test files use Python's built-in `unittest` framework.

1. **Install requirements (if any):**
    - This project uses only standard Python libraries. Include `requirements.txt`
       if additional libraries are needed. You'll however need to install/run it in virtualenv or sandbox environment.

2. **Run a single test module:**
    ```bash
    # python -m unittest tests/test_factorial.py
    ```

3. **Run all tests (from repo root):**
    ```bash
    # python -m unittest discover -s tests

    # Ran 44 tests in 0.001s
     OK
    ```

***

## Contribution Guidelines

Contributions are welcome! To contribute:

- Fork this repository.
- Create a feature branch (`git checkout -b feature/your-feature`).
- Add your code, tests, or improvements. Please follow the style and documentation conventions in the repo.
- Run all tests to ensure your changes do not break existing code.
- Submit a pull request with a clear description of your changes.

If you discover a bug or have a suggestion, please open an issue with clear details.

***

## Acknowledgements

- Inspired by [Practice Python](https://www.practicepython.org)
- Thanks to contributors and the Python learning community!

***