from twttr import shorten

def main():
    # call functions
    test_case_sensitivity()
    test_numbers()
    test_punctuations()

def test_case_sensitivity():
    # Test for case sensitivity errros
    assert shorten("twitter") == "twttr", "check case sensitivity"
    assert shorten("TWITTER") == "TWTTR", "check case sensitivity"
    assert shorten("TwItTeR") == "TwtTR", "check case sensitivity"

def test_punctuations():
    # Test for punctuations errors
    assert shorten("?!,.") == "?!,.", "check symbol errors"

def test_numbers():
    # Test for number errors
    assert shorten("1234") == "1234", "check for number errors"

if __name__ == "__main__":
    main()