# empty dictionary to hold grocery list
grocery_list = {}

# Loop until break
while True:
    try:
        # prompt user of an item
        item = input().lower()

        # check if the input is in the grocery list
        if item in grocery_list:
            # if it is, then add 1
            grocery_list[item] += 1
        else:
            # add the item in the grocery list
            grocery_list[item] = 1

    except EOFError:
        # loop to print the items in order
        for i in sorted(grocery_list.keys()):
            # change i to uppercase
            print(f"{grocery_list[i]} {i.upper()}")
        # escape the loop
        break
