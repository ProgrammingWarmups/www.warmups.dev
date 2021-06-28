---
title: 'What Kind Of Values Can Be Stored In Variables?'
description:
 'Explore the primary data types in Python and learn the different ways to update the value of a variable'
slug: /datatypes
type: chapter
---

<!-- EXERCISE { -->
<exercise id="1" title="Primary Data Types">

- Python has numerous built-in types of data that can be stored in variables
    - To see the full list, visit [W3Schools' List Of Built-in Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- For now, we'll focus on four primary data types: `int`, `float`, `str`, `bool`
    - `int`, or integers, are whole numbers, positive or negative (`0`, `23`, `-123456`)
    - `float` are decimal numbers (`0.0`, `3.14159`, `-123456.7`)
    - `str`, or strings, are sequences of characters (`'a'`, `"hello"`, `"3.14159"`)
        - They are normally used for textual data
        - Notice that strings are defined using single (`'`) or double (`"`) quotes
    - `bool`, or booleans, can be either `True` or `False`
        - `True` and `False` are case-sensitive, so make sure they are capitalized!
- These primary data types are the basic building blocks of data in Python
- Most of the other built-in data types are constructed using these primary data types
- In Python, the data type of a variable is automatically recognized when you assign its value

For example, the code below will print `<class 'int'>`, which shows that the type of `count` is `int`

<codeblock id="datatypes_01a" interactive=false>
</codeblock>

***In the following code, assign***

***- `name` to a `str`***

***-`age` to an `int`***

***-`gpa` to a `float`***

***-`loves_programming` to a `bool`***

<br>

<codeblock id="datatypes_01b">

- Make sure you replace every `?` with a value
- The data type of a variable is inferred based on its value, so make sure the values are of the correct type
    - Integers should be whole numbers without a decimal point
    - Floats should contain a decimal point
    - Strings should be surrounded by either single (`'`) or double (`"`) quotes
    - Booleans should be either `True` or `False`

</codeblock>

<br>

</exercise>
<!-- EXERCISE } -->

