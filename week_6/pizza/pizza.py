import sys
import csv
# table format ASCII art (package)
import tabulate

# if lenght is equal 2
if len(sys.argv) == 2:
    # if last 3 letters index is equal to csv (open)
    if sys.argv[1][-3:] == "csv":

        try:
            # open file
            with open(sys.argv[1]) as f:
                # read dictionary file
                read = csv.DictReader(f)
                # output tabulate package
                print(tabulate.tabulate(read, headers="keys", tablefmt="grid"))
        # catch error if file does not exist
        except FileNotFoundError:
            # program should exit with sys.exit and provide an error message
            sys.exit("File does not exist")

    else:
        # program should exit with sys.exit and provide an error message
        sys.exit("Not a CSV file")

# if lenght is greater less than 2
if len(sys.argv) > 2:
    # program should exit with sys.exit and provide an error message
    sys.exit("Too many command-line arguments")
# if lenght is less than 2
if len(sys.argv) < 2:
    # program should exit with sys.exit and provide an error message
    sys.exit("Too few command-line arguments")

