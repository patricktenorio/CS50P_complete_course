import inflect

p = inflect.engine()

# blank list that will hold input
names = []

while True:
    try:
        # prompts the user for names
        name = input("Name: ")
        # add input in the list
        names.append(name)

    # catch EOFError then break
    except EOFError:
        print()
        break

# join words into a list
mylist = p.join(names)
# print the output
print(f"Adieu, adieu, to {mylist}")

