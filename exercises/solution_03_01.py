import pathlib
from rich import print

def read(file_name):
    # create a Path object to the file
    file_path = pathlib.Path(file_name)
    # read the text of the file
    file_text = file_path.read_text()
    # return the file's contents
    return file_text

def display(file_contents):
    # display a diagnostic message
    print(":mag_right: Contents of the file:")
    # display the file's contents
    print(file_contents)

# read in the text of the email file
emails_file = "exercises/emails.txt"
emails_text = read(emails_file)
# display the text of the email file
display(emails_text)
# there are 10 email addresses in the file
