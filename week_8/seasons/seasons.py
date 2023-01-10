from datetime import date
import inflect
import sys

x = inflect.engine()

def main():
    try:
        # prompt user for date of birth
        # split dash separated value
        # assign values to a variable
        year, month, day = input("Date of Birth: ").split("-")

    # catch ValueError, print error msg, then exit
    except ValueError:
        sys.exit("Invalid Format")

    # call calculate_mins function to see output
    print(calculate_mins(year, month, day))

def calculate_mins(year, month, day):
    try:
        # convert input to integer
        dob = date(int(year), int(month), int(day))
    # catch ValueError, print error msg, then exit
    except ValueError:
        return "Invalid Format"

    # get date today (current date)
    today = date.today()
    # substract current date to input date of birth
    sub = today - dob
    # compute minutes by dividing total_seconds func to 60 (1min = 60secs)
    mins = int(sub.total_seconds() / 60)
    # convert number to words, remove and word, capitalize first letter, add minutes at the end
    txt = x.number_to_words(mins, andword="").capitalize() + " minutes"
    return txt

if __name__ == "__main__":
    main()