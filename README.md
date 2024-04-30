# PRODIGY_CS_03
# Password Complexity Checker
Imagine you're creating a password for an important account, like your email or online banking. You want to make sure your password is strong enough to protect your information from unauthorized access. This code helps you determine the strength of your password by checking for various criteria.

Password Complexity Check Function:
The check_password_complexity function is like a security guard for your password. It inspects the password you provide and evaluates its strength based on specific rules.
Criteria for Password Complexity:
To decide if a password is strong, moderate, or weak, the function looks for certain qualities.
Length Criteria: Your password should be at least 8 characters long to resist simple attacks.
Uppercase Criteria: It's good to include at least one uppercase letter for added complexity.
Lowercase Criteria: Similarly, including at least one lowercase letter makes the password more secure.
Digit Criteria: Including at least one digit (0-9) adds another layer of security.
Special Character Criteria: Using special characters like !@#$%^&*(),.?":{}|<> makes the password even stronger.
Password Strength Assessment: Based on whether the password meets these criteria, the function categorizes its strength.
Strong Password: If the password satisfies all criteria, it's labeled as "Strong." This means it's highly secure.
Moderate Password: If the password is at least 8 characters long, contains either uppercase or lowercase letters (or both), and includes at least one digit, it's classified as "Moderate." While not as secure as a strong password, it still provides decent protection.
Weak Password: If the password doesn't meet any of the above criteria, it's considered "Weak." This indicates that it's vulnerable to attacks and should be strengthened.
User Interaction: In the main function, the user is prompted to enter their password. The check_password_complexity function is then called to assess the password's strength. Finally, the result (strong, moderate, or weak) is displayed to the user, providing feedback on the password's security level.
