import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if s := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s):
        s = s.groups()
        if int(s[1]) > 12 or int(s[5]) > 12:
            raise ValueError
        time1 = format(s[1], s[2], s[3])
        time2 = format(s[5], s[6], s[7])
        return time1 + " to " + time2
    else:
        raise ValueError

def format(hrs, min, am_pm):
    if am_pm == "PM":
        if int(hrs) == 12:
            format_hrs = 12
        else:
            format_hrs = int(hrs) + 12
    else:
        if int(hrs) == 12:
            format_hrs = 0
        else:
            format_hrs = int(hrs)
    if min == None:
        format_min = ":00"
        format_time = f"{format_hrs:02}" + format_min
    else:
        format_time = f"{format_hrs:02}" + ":" + min
    return format_time

if __name__ == "__main__":
    main()