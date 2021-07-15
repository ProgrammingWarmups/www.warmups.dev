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

<!-- EXERCISE { -->

<exercise id="4" title="Check: Arithmetic Operators">

Which of the following operators divides the left operand by the right operand and rounds down to the closest integer?

<choice>

<opt text="Division (<code>/</code>)">
The division operator simply divides the left operand by the right operand.
</opt>

<opt text="Floor division (<code>//</code>)" correct=true>
The floor division operator divides the left operand by the right operand and rounds down to the closest integer.
</opt>

<opt text="Modulus (<code>%</code>)">
The modulus operator divides the left operand by the right operand and returns the remainder.
</opt>

<opt text="Exponentiation (<code>**</code>)">
The exponentiation operator raises the left operand to the right operand.
</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->
<exercise id="5" title="Assignment Operators">

In programming, there are many times when you want to add or subtract from a variable's current value.

The most obvious way to write this code would look something like `a = a + 2` or `b = b - 4`.

However, there are even simpler ways to achieve this behavior using assignment operators.

In a [previous warmup](https://warmups.dev/intro_to_variables), we were introduced to the `=` assignment operator, which assigns the left-hand variable to the right-hand value. In the example `a = a + 2`, the variable `a` is assigned the value of itself plus `2`.

This expression could also be written as `a += 2`, which uses the `+=` assignment operator. The `+=` assignment operator assigns the left-hand variable, `a`, to the value of itself plus the right-hand value `2`.

Similarly, the expression `b = b - 4` could be rewritten as `b -= 4`, using the `-=` assignment operator to assign `b` to the value of itself minus `4`.

In fact, there are numerous other assignment operators that can be used to simplify various operations. There is no need to memorize all of them, since [they can quickly be found online](https://www.w3schools.com/python/gloss_python_assignment_operators.asp), but it is good to keep them in mind when you find yourself assigning the value of a variable to the result of an operation involving itself.

<br>

***The following code should increase the value of the variable `count`, initially set to `3`, by `1`, so that it becomes `4`. However, the print statement reveals that by the end, `count` is not `4`, but rather equal to `1`. Can you spot the bug and fix the code so that `count` is instead increased by `1` and the end count is `4`?***

<br>

<codeblock id="datatypes_05">

- Make sure that the correct assignment operator is being used to set count equal to itself plus <code>1</code>

</codeblock>

This might seem like an obvious mistake, but this is actually a very common type of bug that is easy to miss!

<br>

</exercise>
<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="6" title="Check: Assignment Operators">

If `b = 5`, which of the following expressions, once executed, will result in `b` having the value `3`? 

<choice>

<opt text="<code>b += 2</code>">
This will result in <code>b</code> having the value <code>7</code>.
</opt>

<opt text="<code>b = 2</code>">
This will result in <code>b</code> having the value <code>2</code>.
</opt>

<opt text="<code>b /= 2</code>">
This will result in <code>b</code> having the value <code>2.5</code>.
</opt>

<opt text="<code>b -= 2</code>" correct=true>
This will result in <code>b</code> having the value <code>3</code>.
</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="7" title="Review: What Kind Of Values Can Be Stored In Variables?">

- Primary Data Types 
    - Python has numerous built-in types of data that can be stored in variables
    - The primary data types, which are the basic building blocks of data in Python, are `int`, `float`, `str`, and `bool`
    - The data type of a variable is automatically recognized when you assign its value
- Arithmetic Operators
    - Arithmetic operators (`+`, `-`, `*`, `/`, `**`, `%`, `//`) are used perform mathematical operations on numerical values
    - Least common outside of computer science are the modulus operator, `%`, and the floor division operator, `//`
    - The modulus operator divides the left operand by the right operand and returns the remainder
    - The floor division operator divides the left operand by the right operand and rounds down to the closest integer
- Assignment Operators
    - When you want to add or subtract from a variable’s current value, you can use the `+=` or `-=` assignment operator, which assigns the left-hand variable to the value of itself plus or minus the right-hand value
    - There are [numerous other assignment operators](https://www.w3schools.com/python/gloss_python_assignment_operators.asp) that can be used to simplify various operations in a similar fashion

<br>

</exercise>

<!-- EXERCISE } -->
