---
title: 'How to Search the Contents of a File?'
description:
  "Discover how to create a useful Python program that searches a file's contents"
slug: /warmup3
type: chapter
---

<!-- EXERCISE { -->

<exercise id="1" title="Input and Display a File">

- Using the following source code, can you find these parts of a program?
  - User-defined function:
      - Name: `read`
      - Input: `file_name`
      - Output: `file_text`
      - Body: three comments and three statements
  - User-defined function:
      - Name: `display`
      - Input: `contents`
      - Output: `None`
      - Body: two comments and two statements
- The `contents` variable is also called the parameter to the `display` function
- Note that the `display` function produces output but does not `return` a value
- Complete the task near each `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="warmup3_01">

- Fill in the `_` to record the program's output
- Fill in the `_` to reference the correct variables
- Answer these questions as you study this program:
  - What is the output produced by this program?
  - What is the input, output, and behavior of `read`?
  - What is the input, output, and behavior of `display`?

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="2" title="Check: Input and Display a File">

```python
import pathlib
from rich import print

def read(file_name):
    # create a Path object to the file
    file_path = pathlib.Path(file_name)
    # read the text of the file
    file_text = file_path.read_text()
    # return the file's contents
    return file_text
```

What would happen if this program did not have the statement `import pathlib`?

<choice>

<opt text="The program would run to completion and show ten email addresses in the output">

Actually, the program will crash because the `pathlib` package was not imported.

</opt>

<opt text="The program would crash when running the statement <code>from rich import print</code>">

Actually, `from rich import print` will not cause the program to crash.

</opt>

<opt text="The program would crash when calling the constructor for <code>pathlib.Path</code>" correct="true">

Yes, the program will crash because the `pathlib` package was not imported.

</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="3" title="Search Through a File">

- Using the following source code, can you find these parts of a program?
    - A `for` loop that can iterate through each line of a string
    - An `if` statement that checks to see if a lists length is not zero
    - The call to the `search` function that will not find a  matching email
    - The call to the `search` function that will find a matching email
    - An assignment statement that creates an empty listing using `[]`
- The `display` function prints out all matching lines or a message otherwise
- The `search` function goes through each line in the file's text and looks for an email
- Complete the task near each `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="warmup3_03">

- Fill in the `_` for an email address not found in the file
- Fill in the `_` for an email address found in the file
- Answer these questions as you study this program:
  - What is the output produced by this program?
  - What is the purpose of the `for` loop in the `search` function?
  - What is the purpose of the `if` statement in the `search` function?

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="4" title="Check: Search Through a File">

```python
from rich import print
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
```

In this program, what is the purpose of the source code `if email_address in line:`?

<choice>

<opt text="It iterates through all of the lines stored in <code>file_contents</code>">

Actually, it checks to see if the current `email_address` is in the line of text.

</opt>

<opt text="It checks to see if the <code>email_address</code> is in the current line of text" correct="true">

Yes, it checks to see if the current `email_address` is in the line of text.

</opt>

<opt text="It returns the list of all matching email addresses stored in <code>matching_lines</code>">

Actually, it checks to see if the current `email_address` is in the line of text.

</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="5" title="Fixing a File Searching Program">

- This is the purpose of each user-defined function in this program:
    - The `read` function accesses a file and returns all of its contents
    - The `display` function prints out all matching lines or a message otherwise
    - The `search` function goes through each line in the file's text and looks for an email
- If these functions are not called correctly then the program may:
    - Produce the wrong output
    - Crash and print a traceback showing what went wrong
    - Both produce the wrong output and crash and print a traceback
- After reviewing the correct program from exercise three, fix the broken function calls
- After modifications, the program should produce the same output as in the third exercise
- Complete the task near the `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="warmup3_05">

- Answer these questions as you study this program:
  - What is the purpose of the `read` function?
  - What is the purpose of the `display` function?
  - What is the purpose of the `search` function?
- Mistake example: `display(emails_file)` should be `read(emails_file)`

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="6" title="Check: Fixing a File Searching Program">

```python
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
```

In this program, what is the best order in which to call the functions `read`, `display`, and `search`?

<choice>

<opt text="First, <code>read</code> the file, then <code>search</code> for an email, and finally <code>display</code> the matches" correct="true">

Yes, the correct order would be to call `read`, then `search`, and finally `display`.

</opt>

<opt text="First, <code>search</code> for an email, then <code>read</code> the file, and finally <code>display</code> the matches">

Actually, the correct order would be to call `read`, then `search`, and finally `display`.

</opt>

<opt text="First, <code>display</code> the matches, then <code>read</code> the file, and finally <code>read</code> the file">

Actually, the correct order would be to call `read`, then `search`, and finally `display`.

</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<exercise id="7" title="Stretch: How to Search the Contents of a File?">

```python
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
```

- This source code segment illustrates the following parts of a program:
  - A `read` function that uses both `Pathlib.Path` and `read_text` to access a file's contents
  - A `search` function that iterates through each line in a string and looks for a matching email
  - A `display` function that prints one of two suitable labels and then any lines in a list
- This source code segment also includes the following Python constructs:
    - A `for` loop that can iterate through each line of a string
    - An `if` statement that checks to see if a list's length is not zero
    - A `return` statement that creates output for a function
- This source code would not work as well as it does without these features:
    - A language-defined package called `pathlib` that supports accessing and reading files
    - Language-defined functions like `join`, `map`, and `iter` that manipulate and create variables
    - An externally defined package called `rich` that provides a `print` function that decodes emojis

- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

</exercise>

<!-- EXERCISE } -->
