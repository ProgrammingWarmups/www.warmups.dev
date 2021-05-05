import pathlib
from rich import print

def read(filename):
    return pathlib.Path(filename).read_text()

def display(contents):
    print(contents)

def print_tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

print_tree(pathlib.Path("exercises"))

emails_file = "exercises/emails.txt"
emails_text = read(emails_file)
display(emails_text)
