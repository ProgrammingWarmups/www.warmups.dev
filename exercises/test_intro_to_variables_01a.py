def test():
    # --> Must have correct base area
    assert base_area == 182, "Did you update the base area formula?"
    # --> Must have correct surface area
    assert surface_area == 1174, "Did you update the surface area formula?"
    # --> Must have correct volume
    assert volume == 2730, "Did you update the volume formula?"
    __msg__.good("Well done!")
