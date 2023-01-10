def main():
    # prompts the user for a fraction
    fraction = input("Fraction: ")
    # call convert function
    percentage = convert(fraction)
    answer = (gauge(percentage))
    print(answer)

def convert(fraction):
    # while x > y is True - Loop
    while True:
        try:
            # split input with / and asign numbers to be x and y
            x, y = fraction.split("/")

            # make x and y an integer
            x = int(x)
            y = int(y)

            # compute x and y to decimal and round up using round function
            fraction = round(x / y, 2)

            # if x int is greater than y int, continue loop
            if x > y:
                fraction = input("Fraction: ")
                continue
            # end loop if condition met
            else:
                # multiply the decimal to 100 to get the percentage value
                percentage = int(fraction * 100)
                return percentage

        # except function for Value and ZeroDivison errors
        except (ValueError, ZeroDivisionError):
            # continue to prompt the input
            raise

def gauge(percentage):
    # if percentage is more than 99%, print F
    if percentage >= 99:
        return "F"
    # if percentage is less than 1%, print E
    elif percentage <= 1:
        return "E"
    # else, print the percent variable and add a "%" symbol as string
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()