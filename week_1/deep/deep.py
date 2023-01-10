# Prompts the user for the answer then convert the input to lowercase and strip left and right white spaces
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# Outputting Yes if the user inputs 42 || forty-two || forty two
if question == "42" or question == "forty-two" or question == "forty two":
    print("Yes")
else:
    # Otherwise output No
    print("No")

