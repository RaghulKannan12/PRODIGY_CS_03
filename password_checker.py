import re

def check_password_complexity(password):
    # Define criteria for password complexity
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_character_criteria = bool(re.match(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess password strength based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_character_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
        return "Moderate"
    else:
        return "Weak"

def main():
    password = input("Enter your password: ")
    complexity = check_password_complexity(password)
    print("Password strength:", complexity)

if __name__ == "__main__":
    main()
