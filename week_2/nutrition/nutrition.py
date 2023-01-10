# prompts users to input a fruit (case-insensitively)
fruit_item = input("Item: ").lower()

# a dictionary to associate a fruit with its calories
fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 100,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

# check if the fruit item is in the fruit dictionary
if fruit_item in fruits:
    # assign the calories of the fruit item on a variable
    calories = fruits[fruit_item]
    # print the calories of the inputed fruit item
    print(f"Calories: {calories}")
