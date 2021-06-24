from wasabi import Printer
__msg__ = Printer()
__solution__ = """${solution}"""
${solution}

${test}
try:
    test()
except AssertionError as e:
    __msg__.fail(e)
