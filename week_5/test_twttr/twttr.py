def main():
    # prompts the user for a string of text
    input_string = input("Input: ")

    # call shorten function and asssign input_string to output
    output = shorten(input_string)

    # print the final result
    print(f"Output: {output}")

def shorten(word):
    # hold all vowels both lower and upercase
    vowels = "aeiouAEIOU"
    # for each char in the inputed string
    for char in word:
        # check if any char from the string is a vowel
        if char in vowels:
            # update word and replace all vowels with null value
            word = word.replace(char, "")
    # return to main function
    return word

if __name__ == "__main__":
    main()