def test():
    # --> Must print correct sentence
    assert "My favorite class is CMPSC 100." in __stdout__, "Did you fix the variable's name and make sure its value is \"100\"?"
    __msg__.good("You bet it is ;)")
