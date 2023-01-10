from um import count

def main():
    test1()
    test2()
    test3()

def test1():
    assert count("um") == 1

def test2():
    assert count("um, um. yummy") == 2

def test3():
    assert count("Um, thanks for the album.") == 1
    assert count("hello, world") == 0

if __name__ == "__main__":
    main()