def test():
    # if an assertion fails, the message will be displayed
    # --> must have the output in a comment
    assert "Mean: 5.0" in __solution__, "Did you record the correct program output as a comment?"
    # --> must have the correct arithmetic mean
    assert mean == 5.0, "Are you calculating the arithmetic mean?"
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
