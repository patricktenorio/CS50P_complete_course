import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s := re.search('.+src="https?://(www.)?youtube.com/embed/(.+?)"', s):
        yt_link = "https://youtu.be/" + s.group(2)
        return yt_link
    else:
        return None

if __name__ == "__main__":
    main()