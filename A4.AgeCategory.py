# Get age from the user
age = int(input("Enter your age: "))

# Determine the age category
if age < 0:
    print("Invalid age entered.")
elif age <= 12:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
elif age <= 59:
    print("You are an Adult.")
else:
    print("You are a Senior.")
