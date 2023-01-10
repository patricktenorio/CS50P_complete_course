import re

def main():
    print(count(input("Text: ")))

def count(s):
    s = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(s)

if __name__ == "__main__":
    main()