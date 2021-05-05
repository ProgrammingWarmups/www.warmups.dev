def test():
    # if an assertion fails, the message will be displayed
    # --> must have the output in a comment
    assert "Mean: 5.0" in __solution__, "Did you record the correct program output as a comment?"
    # --> must have the output in a comment
    assert "Mean: 4.0" in __solution__, "Did you record the correct program output as a comment?"
    # --> must have the first function call
    assert "mean(numbers_one)" in __solution__, "Did you call the mean function with numbers_one as input?"
    # --> must have the second function call
    assert "mean(numbers_two)" in __solution__, "Did you call the mean function with numbers_two as input?"
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
