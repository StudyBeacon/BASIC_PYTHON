# Loop Exercise #2 — Guess the Number (Easy Version)

# Write a program that:

# Picks a secret number: 7

# Asks the user to guess the number

# If the guess is wrong → print: "Wrong guess. Try again."

# Repeat until they guess 7

# When correct → print: "You got it!"


secret_number= input("Guess the number: ")
while secret_number != "7":
    print("Wrong guess. Try again.")
    secret_number= input("Guess the number: ")

print("You got it!")    