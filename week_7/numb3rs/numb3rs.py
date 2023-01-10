import re

def main():
    # expects an IPv4 address as input as a str
    print(validate(input("IPv4 Address: ")))

def validate(ip):

    # then returns True or False if input is valid IPv4 address or not
    if ip := re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()