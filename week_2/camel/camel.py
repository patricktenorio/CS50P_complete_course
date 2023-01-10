# prompts the user for the name of a variable in camel case
camel_text = input("camelCase: ").strip()

# assign the first char of the camel case
snake_text = camel_text[0]

# check the first letter in input
for char in camel_text[1:]:
    # check if first letter is upper
    if char.isupper():
        # add "_" at the beginning of the uppercase char then make it lowercase
        snake_text += "_" + char.lower()
    else:
        snake_text += char.lower()
# outputs the corresponding name in snake case.
print(f"snake_case: {snake_text}")