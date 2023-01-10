# import package library emoji
import emoji

# prompts the user for a str in English
str = input("Input: ")

# outputs the “emojized” version of that str
print(emoji.emojize(f'Output: {str}', language='alias'))