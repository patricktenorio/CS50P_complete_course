# menu dictionary provided
menu_of_entrees = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# total variable set to 0
total_price = 0
while True:
    try:
        # promt the user to to place an order from the menu
        # assume that every item on the menu will be titlecased
        order = input("Item: ").title()

        # check if input food item is in the menu
        if order in menu_of_entrees:
            # add the price of the food item on the total price variable
            total_price += menu_of_entrees[order]
            # print the total amount formatted to two decimal
            print(f"Total: ${total_price:.2f}")

    # detect EOF error
    except EOFError:
        # print a new line so cursor doesn't remain on same line
        print()
        # break if EOF error detected
        break