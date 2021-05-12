def test():
    # if an assertion fails, the message will be displayed
    # --> must have the diagnostic comment
    assert "10 email addresses" in __solution__, "Did you record the correct number of emails as a comment?"
    # --> must have code construct
    assert "print(file_contents)" in __solution__, "Did you print the file_contents variable?"
    # --> must have code construct
    assert "display(emails_text)" in __solution__, "Did you display the emails_text variable?"
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
