def test():
    # if an assertion fails, the message will be displayed
    # --> must calculate the arithmetic mean
    assert "mean = s / N" in __solution__, "Are you calculating the arithmetic mean?"
    assert mean == s / N, "Are you calculating the arithmetic mean?"
    # --> must display the arithmetic mean
    assert "{mean}" in __solution__, "Are you displaying the arithmetic mean?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
