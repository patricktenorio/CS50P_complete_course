from validator_collection import validators

def main():
    try:
        email = input("What's your email address? ")
        print(validate(email))
    except:
        print("Invalid")
        quit()

def validate(email):
    if email := validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()