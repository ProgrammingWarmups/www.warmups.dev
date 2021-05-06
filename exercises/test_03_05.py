def test():
    # if an assertion fails, the message will be displayed
    # --> must have code construct
    assert "read(emails_file)" in __solution__, "Did you call the read function correctly?"
    # --> must have code construct
    assert "search(emails_text" in __solution__, "Did you call the search function correctly?"
    # --> must have code construct
    assert "search(emails_text" in __solution__, "Did you call the search function correctly?"
    # --> must have code construct
    assert "display(matching_emails)" in __solution__, "Did you call the display function correctly?"
    # --> must not have a TODO marker in the solution
    assert "TODO" not in __solution__, "Did you remove the TODO marker when finished?"
    # display a congratulations for a correct solution
    __msg__.good("Well done!")
