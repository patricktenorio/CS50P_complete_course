from numb3rs import validate

def main():
    test_true()
    test_false()

def test_true():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True

def test_false():
    assert validate("300.300.300.300") == False
    assert validate("190.300.300.300") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()