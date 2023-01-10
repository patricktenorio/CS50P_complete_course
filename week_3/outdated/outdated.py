# Created a dictionary of months
months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

# Loop until True
while True:
    # prompt the user to input a date
    date = input("Date: ")
    try:
        # check if there's a comma in the input date
        if "," in date:
            # assign variable on each split separated with white space
            month, day, year = date.split(" ")
            # remove the comma by replacing it whit "" Null
            day = day.replace(",", "")
            # if day is less than 31 and month is in months dictionary
            if int(day) < 31 and month in months:
                # print date with this format = YYYY-MONTH-DAY
                print(f"{year}-{int(months[month]):02}-{int(day):02}")
                # escape the loop
                break

        # check input if has "/" in it
        elif "/" in date:
            # assign a variable on each split separated with "/"
            month, day, year = date.split("/")

            # convert month, day, and year to integers
            month = int(month)
            day = int(day)
            year = int(year)

            # if the day is greater than 31 days or month is greater than 12 days
            if day > 31 or month > 12:
                # just continue to prompt the user with a valid date
                continue
            # otherwise
            else:
                # print the date with this format = YYYY-MONTH-DAY
                print(f"{year}-{int(month):02}-{int(day):02}")
                # escape the loop
                break
    except:
        # disregard errors
        pass