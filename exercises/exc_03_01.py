import pathlib
from rich import print

def read(filename):
    return pathlib.Path(filename).read_text()

def display(contents):
    print(contents)

emails_file = "exercises/emails.txt"
emails_text = read(emails_file)
display(emails_text)
