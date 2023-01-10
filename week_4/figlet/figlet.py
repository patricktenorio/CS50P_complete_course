
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# get figlet fonts
fonts = figlet.getFonts()

# Zero if the user would like to output text in a random font.
if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))

# Two if the user would like to output text in a specific font
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    figlet.setFont(font = sys.argv[2])
else:
    # exit via sys.exit with an error message
    sys.exit("Invalid usage")

# Prompts the user for a str of text.
str = input("Input: ")

# Outputs that text in the desired font.
print(figlet.renderText(str))


