def test():
    # if an assertion fails, the message will be displayed
    # --> must have the correct arithmetic mean
    assert numbers_one_mean == 4.0, "Are you calculating the arithmetic mean?"
    # --> must have the first function call
    assert "mean(numbers_one)" in __solution__, "Did you call the mean function with numbers_one as input?"
    # --> must have the second function call
    assert "inspect(numbers_one" in __solution__, "Did you call the inspect function with numbers_one as input?"
    # --> must have the first emoji
    assert ":mag_right:" in __solution__, "Did you display a magnifying glass emoji with :mag_right:?"
    # --> must have the second emoji
    assert ":rocket:" in __solution__, "Did you display a rocket emoji with :rocket:?"
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
