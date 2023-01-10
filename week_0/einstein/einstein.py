# Einstein formula E = mc²
# E - represents energy (measured in Joules)
# m - represents mass (measured in kilograms)
# c - represents the speed of light (measured approx. as 300m meters per second)
c = 300000000

# Prompt the users for mass as an integer (in kg)
kg = int(input())

# Convert using Einstein formula
joules = kg * (c ** 2)

# Outputs the equivalent number of Joules as an integer
print(joules)