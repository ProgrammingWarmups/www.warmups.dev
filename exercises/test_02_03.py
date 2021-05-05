def test():
    # if an assertion fails, the message will be displayed
    # --> must have the correct arithmetic mean
    assert numbers_one_mean == 4.0, "Are you calculating the arithmetic mean?"
    # --> must have the first function call
    assert "mean(numbers_one)" in __solution__, "Did you call the mean function with numbers_one as input?"
    # --> must have the second function call
    assert "display(numbers_one)" in __solution__, "Did you call the display function with numbers_one as input?"
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
