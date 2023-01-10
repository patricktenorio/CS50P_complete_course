# prompt for users input
text = input()

# function convert
def convert(text):
    # convert happy and sad text to emoji
    face = text.replace(":)", "🙂").replace(":(", "🙁")
    # return to print the result
    return face

def main():
    # call the convert function and assign a variable
    result = convert(text)
    # print the result variable
    print(result)

# It said don't forget to call main :)
main()

