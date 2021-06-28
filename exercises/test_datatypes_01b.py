def test():
    # --> Name must be string
    assert isinstance(name, str), f"{repr(name)} is not a string. Did you make sure to surround it with single or double quotes?"
    # --> Age must be integer
    assert isinstance(age, int), f"{repr(age)} is not an integer. Did you make sure it does not contain a decimal point?"
    # --> GPA must be a float
    assert isinstance(gpa, float), f"{repr(gpa)} is not a float. Did you make sure it contains a decimal point?"
    # --> Loves programming must be a boolean
    assert isinstance(loves_programming, bool), f"{repr(loves_programming)} is not a boolean. Did you make sure it is either True or False?"
    __msg__.good("Well done!")
