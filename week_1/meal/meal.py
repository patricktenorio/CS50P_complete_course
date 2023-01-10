# prompts the user for a time
time = float(input("What time is it? ").replace(":", "."))

def main():
    # call the convert function
    convert(time)

# breakfast between 7:00 and 8:00
# lunch between 12:00 and 13:00
# dinner between 18:00 and 19:00
def convert(time):
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("")
    # return time to main function
    return time

if __name__ == "__main__":
    main()



