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
    # there are lines of text, so display them
    if len(lines) != 0:
        comma = "\n"
        lines_display = comma.join(map(str, lines))
        print(":smile: Here are the matches!")
        print(lines_display)
    # there are no lines of text, display a message
    else:
        print(":cry: Sorry, no matches!")

def search(file_contents, email_address):
    # display the email address to find
    print(f":mag_right: Searching for {email_address}")
    matching_lines = []
    # search through each line in the file for the email address
    for line in iter(file_contents.splitlines()):
        if email_address in line:
            matching_lines.append(line)
    # return the list of all matching email address(es)
    return matching_lines

# TODO: Fix the mistakes in the function
# calls, ensuring same output as before
# read in the text of the email file
emails_file = "exercises/emails.txt"
emails_text = display(emails_file)
# search for a missing email address
matching_emails = read(emails_text, "mukherjee@yahoo.com")
search(matching_emails)
# search for an available email address
matching_emails = search(emails_text, "rsanchez@yahoo.com")
read(matching_emails)
