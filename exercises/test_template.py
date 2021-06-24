from wasabi import Printer
import sys

# https://stackoverflow.com/a/14906787
class Logger(object):
    captured = ""
    def __init__(self):
        self.terminal = sys.stdout

    def write(self, message):
        self.terminal.write(message)
        self.captured += message

    def flush(self):
        self.terminal.flush()

sys.stdout = Logger()

__msg__ = Printer()
__solution__ = """${solution}"""
${solution}

__stdout__ = sys.stdout.captured
${test}
try:
    test()
except AssertionError as e:
    __msg__.fail(e)
