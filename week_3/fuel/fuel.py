# while x > y is True - Loop
while True:
    try:
        # prompts the user for a fraction
        frac = input("Fraction: ")
        # split input with / and asign numbers to be x and y
        x, y = frac.split("/")

        # make x and y an integer
        x = int(x)
        y = int(y)

        # compute x and y to decimal and round up using round function
        decimal = round(x / y, 2)
        # multiply the decimal to 100 to get the percentage value
        percent = int(decimal * 100)

        # if x int is greater than y int, continue loop
        if x > y:
            continue
        # if decimal is more than 99%, print F
        elif decimal > 0.9:
            print("F")
        # if decimal is less than 1%, print E
        elif decimal < 0.1:
            print("E")
        # else, print the percent variable and add a "%" symbol as string
        else:
            print(f"{percent}%")

        # end loop if condition met
        break

    # except function for Value and ZeroDivison errors
    except (ValueError, ZeroDivisionError):
        # continue to prompt the input
        continue