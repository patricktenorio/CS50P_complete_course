import sys

def main():
    # call command-line argument function
    cmd_line_arg()

    try:
        # open file
        with open(sys.argv[1]) as file:
            # read and assign to rows
            rows = file.readlines()

    # catch error if file does not exist
    except FileNotFoundError:
        # program should exit with sys.exit and provide an error message
        sys.exit("File does not exist")

    #count rows
    count = 0
    # loop to check
    for row in rows:
        # Check for hash (#) and whitespaces
        if hash_whitespace(row) == False:
            # update count add 1
            count += 1
    # output
    print(count)

# test command line arguments function
def cmd_line_arg():
    # if lenght is less than 2
    if len(sys.argv) < 2:
        # program should exit with sys.exit and provide an error message
        sys.exit("Too few command-line arguments")
    # if lenght is greater than 2
    if len(sys.argv) > 2:
        # program should exit with sys.exit and provide an error message
        sys.exit("Too many command-line arguments")
    # test if code is an extension of Python file (py)
    if ".py" not in sys.argv[1]:
        # program should exit with sys.exit and provide an error message
        sys.exit("Not a Python file")

# test for hash (#) and whitespace
def hash_whitespace(row):
    # return true if whitespace detect
    if row.isspace():
        return True
    # strip left then check if starts with hash (#)
    if row.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()