# SimplePassword.py

# Set minimum password length
MIN_LENGTH = 8

# Get password input from user
password = input("Enter your password: ")

# Check the length
if len(password) >= MIN_LENGTH:
    print("✅ Password is valid.")
else:
    print(f"❌ Password is too short. Minimum {MIN_LENGTH} characters required.")
# To run: python A7.simplepassword.py