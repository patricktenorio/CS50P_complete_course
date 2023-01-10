# Prompts the user for an arithmetic expression
math = input("Expression: ").strip()

# Assume that the user’s input will be formatted as x y z
x, y, z = math.split(" ")

# convert x and z to integer
x = int(x)
z = int(z)

# Calculates and outputs formatted to one decimal place
if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))

