def test():
    # --> Must have correct end count
    assert count == 4, "Did you fix the code so that count is increased by 1?"
    # --> Must use += assignment operator
    assert "+=" in __solution__, "Did you use the assignment operator that sets a variable equal to itself plus a value?"
    __msg__.good("Well done!")
