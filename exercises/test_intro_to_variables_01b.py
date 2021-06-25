def test():
    # --> Must have correct base area
    assert base_area == 182, "Incorrect base area. Did you update the length and width?"
    # --> Must have correct surface area
    assert surface_area == 1174, "Incorrect surface area. Did you update the length, width, and height?"
    # --> Must have correct volume
    assert volume == 2730, "Incorrect volume. Did you update the length, width, and height?"
    __msg__.good("Well done!")
