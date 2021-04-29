def test():
    # if an assertion fails, the message will be displayed
    # --> must have the output in a comment
    assert "Mean: 5.0" in __solution__, "Did you record the correct program output as a comment?"
    # --> must display the arithmetic mean
    assert "DONE" in __solution__, "Did you mark the TODO task as DONE?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
