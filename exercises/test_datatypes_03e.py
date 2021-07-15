def test():
    # --> Must have set variables to the correct values
    assert a == 10, "Did you correctly update the value of the numerator variable, a?"
    assert b == 3, "Did you correctly update the value of the denominator variable, b?"
    # --> Must have correct remainder
    assert remainder == 1, "Did you use the correct operator?"
    __msg__.good("Well done!")
