# Prompts the user for a greeting
greetings = input("Greeting: ").lower().strip()
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


# If the greeting starts with “hello”, output $0
if "hello" in greetings:
    print("$0")

# If the greeting starts with an “h” (but not “hello”), output $20
elif greetings[0] == "h":
    print("$20")

# Otherwise, output $100
else:
    print("$100")


# Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

# Hello = $0
# Hello, Newman = $0
# How you doing? = $20
# What's happening? = $0