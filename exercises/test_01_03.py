def test():
    # if an assertion fails, the message will be displayed
    # --> must calculate the arithmetic mean as 4.0
    assert mean == 4.0, "Are you correctly calculating the arithmetic mean?"
    # --> must use the correct equation for calculating arithmetic mean
    assert "s / N" in __solution__, "Are you correctly calculating the arithmetic mean?"
    # --> must display the arithmetic mean
    assert "{mean}" in __solution__, "Are you displaying the arithmetic mean?"
    # --> must use the correct assignment for sum
    assert "s = sum(" in __solution__, "Are you correctly calculating the sum?"
    # --> must use the correct assignment for len
    assert "N = len(" in __solution__, "Are you correctly calculating the length?"
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
