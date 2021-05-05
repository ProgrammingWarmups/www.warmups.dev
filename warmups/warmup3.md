---
title: 'Warmup 3: How to Search the Contents of a File?'
description:
  "Discover how to create a useful Python program that searches a file's contents"
prev: /warmup2
next: null
type: chapter
id: 3
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

<codeblock id="03_01">

- Fill in the `_` to record the program's output
- Fill in the `_` to reference the correct variables
- Answer these questions as you study this program:
  - What is the output produced by this program?
  - What is the purpose of a user-defined function?
  - What is the input, output, and behavior of `mean`?

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
