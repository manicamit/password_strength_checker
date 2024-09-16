# Password Strength Checker

This Python program evaluates the strength of a password based on various criteria, such as length, the presence of digits, uppercase and lowercase letters, and special symbols. It provides specific feedback for improving weak passwords.

## Features

- Checks password length (default between 8 and 20 characters).
- Validates the presence of:
  - At least one digit.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one special symbol (e.g., `!`, `@`, `#`, `$`, etc.).
- Returns password strength as **Strong**, **Moderate**, or **Weak**.
- Provides specific feedback for weak passwords.

## Requirements

- Python 3.x
- `re` module (comes pre-installed with Python)

## Installation

1. Clone this repository or download the `password_strength_checker.py` file.
2. Run the program using Python:
   ```bash
   python password_strength_checker.py
