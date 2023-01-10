def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # should accept a string as input
    # formatted as ($##.##) wherein each # is a decimal digit
    # remove the leading $, and return the amount as a float
    # example = $50.00 to 50.0
    d = float(d.replace("$", ""))
    return d

def percent_to_float(p):
    # should accept a string as input
    # formatted as (##%) wherein each # is a decimal digit
    # remove the trailing %, and return the percentage as a float
    # example = 15% to 0.15
    p = float(p.replace("%", ""))
    p = p/100
    return p

main()