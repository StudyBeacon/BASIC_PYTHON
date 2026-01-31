# 🔥 Loop Exercise #1 — Enter PIN

# Write a program that:

# Keeps asking user for a PIN

# Correct PIN = 4321

# If wrong → print "Incorrect PIN. Try again."

# If correct → print "Access granted!"

# Use a while loop

PIN = input("Enter your PIN: ")

while PIN != "4321":
    print("Incorrect PIN. Try again.")
    PIN = input("Enter your PIN: ")

print("Access granted!")
