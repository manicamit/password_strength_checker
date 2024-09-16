import re

def check_length(password, min_length=8):
    return len(password) >= min_length 

def check_digit(password):
    return re.search(r"\d", password) is not None

def check_uppercase(password):
    return re.search(r"[A-Z]", password) is not None

def check_lowercase(password):
    return re.search(r"[a-z]", password) is not None

def check_symbol(password):
    # Expanded symbol set
    return re.search(r"[ !@#$%^&*()_+=-{}[\]~`<>?,./|\\]", password) is not None

def check_password_strength(password):
    length_valid = check_length(password)
    digit_valid = check_digit(password)
    uppercase_valid = check_uppercase(password)
    lowercase_valid = check_lowercase(password)
    symbol_valid = check_symbol(password)

    # Collect the errors for detailed feedback
    errors = []
    if not length_valid:
        errors.append("Password length must be 8 characters.")
    if not digit_valid:
        errors.append("Password must contain at least one digit.")
    if not uppercase_valid:
        errors.append("Password must contain at least one uppercase letter.")
    if not lowercase_valid:
        errors.append("Password must contain at least one lowercase letter.")
    if not symbol_valid:
        errors.append("Password must contain at least one special symbol.")

    # Determine strength based on the number of valid components
    valid_checks = [length_valid, digit_valid, uppercase_valid, lowercase_valid, symbol_valid]

    if all(valid_checks):
        return "Strong Password"
    elif valid_checks.count(True) >= 3:
        return "Moderate Password"
    else:
        return "Weak Password. Issues:\n" + "\n".join(errors)

password = input("Enter a password to check its strength: ")
print(check_password_strength(password))

