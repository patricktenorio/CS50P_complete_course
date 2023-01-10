from fuel import convert, gauge
import pytest

def main():
    # call test functions
    test_convert()
    test_gauge()
    test_errors()

def test_convert():
    # test fraction conditions
    assert convert("1/100") == 1, "Fuel Empty"
    assert convert("1/4") == 25, "Fuel 25%"
    assert convert("1/2") == 50, "Fuel Half"
    assert convert("99/100") == 99, "Fuel Full"

def test_gauge():
    # test percentage conditions
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

def test_errors():
    # test for catched except errors
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()