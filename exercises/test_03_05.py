def test():
    # if an assertion fails, the message will be displayed
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
