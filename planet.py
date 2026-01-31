# 🧑‍🚀 Planet Weights

# 15 XP

# HARD
# Instructions

# The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

# Create a weight conversion program that:

#     Asks the user what their Earth weight is (as a float).
#     Asks the user for a planet number (as an int).

# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

# To calculate the user's weight:
# destination weight=Earth weight × relative gravity
# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14

# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.


earth_weight = float(input("Enter your weight: "))
planet_num = int(input("Enter the planet number: "))

if planet_num == 1:
  print(f"Weight on Mercury : {earth_weight * 0.38}")
elif planet_num == 2:
  print(f"Weight on Venus : {earth_weight * 0.91}")
elif planet_num == 3:
  print(f"Weight on Mars : {earth_weight * 0.38}")
elif planet_num == 4:
  print(f"Weight on Jupiter : {earth_weight * 2.53}")
elif planet_num == 5:
  print(f"Weight on Saturn : {earth_weight * 1.07}")
elif planet_num == 6:
  print(f"Weight on Uranus : {earth_weight * 0.89}")
elif planet_num == 7:
  print(f"Weight on Neptune : {earth_weight * 1.14}")
else:
  print("Invalid Planet number. ")