# Loop Exercise #3 — Password Retry System

# Write a program that:

# Asks the user for a password

# Correct password = "python123"

# If wrong → print: "Wrong password. Try again."

# Keep asking until they enter the correct one

# When correct → print: "Login successful!"


password = input("Enter the password: ")
while password != "python123":
  print("Wrong password. Try again.")
  password = input("Enter the password: ")

print("Login successful!")

