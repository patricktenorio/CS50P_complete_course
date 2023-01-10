# prompts the user for a string of text
input_string = input("Input: ")
# assign output string as input string
output_string = input_string

# hold all vowels both lower and upercase
vowels = "aeiouAEIOU"

# for each letter in the inputed string
for letter in input_string:
    # check if any letter from the string is a vowel
    if letter in vowels:
        # update output_string and replace all vowels with null value
        output_string = output_string.replace(letter, "")

# print the final result
print(f"Output: {output_string}")