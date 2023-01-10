def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if input between 2 to 6 or starts with at least two letters and there's no special char
    if len(s) < 2 or len(s) > 6 or s[0:2].isalpha() == False or s.isalnum() == False:
        return False

    # Checks if the first number is a zero or not (it should not be)
    x = ""
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            x += s[i]
            if x[0] == "0":
                return False

    # Check if all are letters
    if s.isalpha():
        return True

    # Loop through the string and check if numbers are in the middle or not
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            update = i
            break

    valid = True
    for i in range(update, len(s)):
        if s[i].isalpha():
            valid = False

    if valid == False:
        return False
    return True

main()