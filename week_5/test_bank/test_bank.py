from bank import value

def main():
    # call all functions
    test_hello()
    test_start_h()
    test_random()

def test_hello():
    # test for  case sensitivity
    assert value("hello") == 0, "Should be equal to 0"
    assert value("HELLO") == 0, "Should be equal to 0"
    assert value("heLLo") == 0, "Should be equal to 0"

def test_start_h():
    # test for greetings starts with an h
     assert value("hey yow") == 20, "Should be equal to 20"
     assert value("hi") == 20, "Should be equal to 20"
     assert value("Hola") == 20, "Should be equal to 20"

def test_random():
    # test for random greetings
    assert value("Kamusta?") == 100, "Should be equal to 100"
    assert value("Kumain ka na?") == 100, "Should be equal to 100"
    assert value("Wazzup") == 100, "Should be equal to 100"

if __name__ == "__main__":
    main()