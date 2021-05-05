import pathlib
from rich import print

def read(file_name):
    # create a Path object to the file
    file_path = pathlib.Path(file_name)
    # read the text of the file
    file_text = file_path.read_text()
    # return the file's contents
    return file_text

def display(lines):
    # create a newline separator for text
    if len(lines) != 0:
        comma = "\n"
        lines_display = comma.join(map(str, lines))
        print(":smile: Here are the matches!")
        print(lines_display)
    else:
        print(":cry: Sorry, no matches!")

def search(file_contents, email_address):
    print(f":mag_right: Searching for {email_address}")
    matching_lines = []
    for line in iter(file_contents.splitlines()):
        if email_address in line:
            matching_lines.append(line)
    return matching_lines

# read in the text of the email file
emails_file = "exercises/emails.txt"
emails_text = read(emails_file)
# search for an email address
matching_emails = search(emails_text, "mukherjee@yahoo.com")
display(matching_emails)
# search for an email address
matching_emails = search(emails_text, "rsanchez@yahoo.com")
display(matching_emails)
