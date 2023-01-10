# import library
import sys
import os # for extensions
from PIL import Image, ImageOps # import & add package

# check if the lenght of cmd-line argument is equal to 3
if len(sys.argv) == 3:

    # assign extensions
    ext = [".jpeg", ".jpg", ".png"]
    # split to cross check both extensions
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])
    # if ext1 is equal to ext2 and if ext1 is in ext
    if ext1[1] == ext2[1] and ext1[1] in ext:

        try:
            # open image
            my_image = Image.open(sys.argv[1])

        # catch FileNotFoundError
        except FileNotFoundError:
            # output error if file/image can't be found
            sys.exit("Input does not exist")

        # open main image
        my_shirt = Image.open("shirt.png")
        # assign shirt .size to a variable
        my_size = my_shirt.size
        # resize image to fit the cs50 shirt
        my_image = ImageOps.fit(my_image, my_size)
        # paste the shirt to the image
        my_image.paste(my_shirt, my_shirt)
        # add it on the 3rd line argument
        my_image.save(sys.argv[2])

    # else if ext1 is not equal to ext
    elif ext1[1] != ext2[1]:
        # program should exit with sys.exit and provide an error message
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Please use proper image extensions")

# if lenght is greater than 3
if len(sys.argv) > 3:
    # program should exit with sys.exit and provide an error message
    sys.exit("Too many command-line arguments")
# if lenght is less than 3
if len(sys.argv) < 3:
    # program should exit with sys.exit and provide an error message
    sys.exit("Too few command-line arguments")