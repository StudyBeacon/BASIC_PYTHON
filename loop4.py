# 🔥 Loop Exercise #4 — Count How Many Tries It Took

# Write a program that:

# Secret number = 5

# Ask the user to guess the number

# If wrong → print "Wrong!"

# Keep asking until they get it right

# Count how many guesses they took

# When correct → print:



tries = 0

guess = int(input("Guess the number: "))

while guess != 5:
    print("Wrong!")
    tries += 1
    guess = int(input("Guess the number: "))

tries += 1
print(f"Correct! You took {tries} tries.")
