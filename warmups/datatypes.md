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

<!-- EXERCISE { -->

<exercise id="2" title="Check: Primary Data Types">

In the code below, what is the type of `num`?

```
num = "-123456.7"
```

<choice>

<opt text="<code>int</code>">
<code>"-123456.7"</code> is not an integer.
</opt>

<opt text="<code>float</code>">
Though floats do contain decimal points, they are not surrounded by double quotes.
</opt>

<opt text="<code>str</code>" correct=true>
Any value surrounded by single or double quotes is a string.
</opt>

<opt text="<code>bool</code>">
A boolean can only be <code>True</code> or <code>False</code>.
</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->
<exercise id="3" title="Arithmetic Operators">

In Python, arithmetic operators are used perform mathematical operations on numerical values.

| Operator | Name |
|----------|-----------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `**` | Exponentiation |
| `%` | Modulus |
| `//` | Floor division |

You are probably familiar with addition, subtraction, multiplication, division, and exponentiation, which are demonstrated below.

<br>

<codeblock id="datatypes_03a" interactive=false>
</codeblock>

Modulus and floor division are much less common outside of computer science, so let's take a closer look.

The modulus operator (`%`) divides the left operand by the right operand and returns the remainder.

The example below demonstrates the difference between the division operator, which returns the actual result of dividing `7` by `2`, and the modulus operator, which returns the remainder of dividing `7` by `2`.

<br>

<codeblock id="datatypes_03b" interactive=false>
</codeblock>

The floor division operator (`//`) divides the left operand by the right operand and rounds down to the closest integer.

As shown below, since the result of dividing `7` by `2` is `3.5`, using the floor division operator to divide `7` by `2` returns `3`, since `3` is the closest integer below `3.5`.

<br>

<codeblock id="datatypes_03c" interactive=false>
</codeblock>

You can use operators with variables as well.

For example, the code below performs the addition operation on variables `a` and `b` and stores the result in another variable named `result`.

<br>

<codeblock id="datatypes_03d" interactive=false>
</codeblock>

***In the following code, assign the value of the variable `remainder` to the remainder of dividing `10` by `3`.***

<br>

<codeblock id="datatypes_03e">

- Make sure that all of the question marks (<code>?</code>) have been replaced by either values or operators
- Remember that the modulus operator (<code>%</code>) returns the remainder of dividing the left operand by the right operand

</codeblock>

</exercise>
<!-- EXERCISE } -->
