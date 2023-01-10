from seasons import calculate_mins

def main():
    test_valid()
    test_invalid()

def test_valid():
    assert calculate_mins(1991, 12, 9) == "Sixteen million, two hundred eight thousand, six hundred forty minutes"
    assert calculate_mins(1990, 4, 17) == "Seventeen million, seventy-four thousand eighty minutes"

def test_invalid():
    assert calculate_mins(9, "December", 1991) == "Invalid Format"
    assert calculate_mins("April", 4, 1990) == "Invalid Format"

if __name__ == "__main__":
    main()