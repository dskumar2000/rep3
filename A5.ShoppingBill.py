# Shopping Bill Calculator

# Input prices of 3 items
item1 = float(input("Enter price of item 1: ₹"))
item2 = float(input("Enter price of item 2: ₹"))
item3 = float(input("Enter price of item 3: ₹"))

# Input tax percentage
tax_percent = float(input("Enter tax percentage: "))

# Calculate subtotal
subtotal = item1 + item2 + item3

# Calculate tax amount
tax_amount = subtotal * (tax_percent / 100)

# Calculate total bill
total = subtotal + tax_amount

# Print the bill
print("\n----- Shopping Bill -----")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax (@{tax_percent}%): ₹{tax_amount:.2f}")
print(f"Total Amount to Pay: ₹{total:.2f}")
# TO RUN  : python A5.ShoppingBill.py