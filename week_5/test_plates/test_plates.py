from plates import is_valid

def main():
    # call test functions
    test_lenght()
    test_two_letters()
    test_middle_char()
    test_others()

def test_lenght():
    # test if max of 6 chars and min of 2 chars
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFGH") == False
    assert is_valid("ABCDEFGHIJ") == False

def test_two_letters():
    # test if first two char are letters
    assert is_valid("AB") == True
    assert is_valid("CD") == True
    assert is_valid("1E") == False
    assert is_valid("F1") == False
    assert is_valid("11") == False

def test_middle_char():
    # test if middle char and end char are numbers
    assert is_valid("A1") == False
    assert is_valid("A2B") == False
    assert is_valid("AB3C") == False
    assert is_valid("AB444") == True
    assert is_valid("ABC555") == True

def test_firstnum_zero():
    # test if first mid number is zero (0)
    assert is_valid("AB01") == False
    assert is_valid("CD10") == True

def test_others():
    # test for punctation and white spaces
    assert is_valid("AB1!23") == False
    assert is_valid("CD4?56") == False
    assert is_valid("EF7 89") == False

if __name__ == "__main__":
    main()