import sys
import csv

# if lenght is equal 3
if len(sys.argv) == 3:
    # if last 3 letters index is equal to csv (open)
    if sys.argv[1][-3:] == "csv":

        try:
            # open first file
            with open(sys.argv[1]) as f1:
                # read file as dictionary
                read = csv.DictReader(f1)
                # open second file
                with open(sys.argv[2], "w") as f2:
                    # write fieldnames "first, last, and house"
                    write = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
                    # write data
                    write.writeheader()

                    # loop
                    for row in read:
                        # remove name
                        row["first"] = row.pop("name")
                        # split comma separated value
                        lastname, firstname = row["first"].split(", ")
                        # assign firstname to row (first)
                        row["first"] = firstname
                        # assign lastname to row (last)
                        row["last"] = lastname
                        # write data
                        write.writerow(row)

        # catch error if file does not exist
        except FileNotFoundError:
            # program should exit with sys.exit and provide an error message
            sys.exit(f"Could not read {sys.argv[1]}")

    else:
        # program should exit with sys.exit and provide an error message
        sys.exit("Not a CSV file")

# if lenght is greater less than 2
if len(sys.argv) > 3:
    # program should exit with sys.exit and provide an error message
    sys.exit("Too many command-line arguments")
# if lenght is less than 2
if len(sys.argv) < 3:
    # program should exit with sys.exit and provide an error message
    sys.exit("Too few command-line arguments")