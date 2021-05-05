---
title: 'Warmup 2: How to Create a Program with Functions?'
description:
  'Learn how to organize a program into separate functions with distinguished behavior'
prev: /warmup1
next: /warmup3
type: chapter
id: 2
---

<!-- EXERCISE { -->

<exercise id="1" title="Creating a Function">

- Using the following source code, can you find these parts of a program?
  - User-defined function:
      - Name: `mean`
      - Input: `numbers`
      - Output: `arithmetic_mean`
      - Body: three comments and four statements
  - Lists: `numbers_one` and `numbers_two`
  - Language-defined functions: `sum`, `len`, and `print`
- What are the similarities and differences between `mean` and `sum`?
- Complete the task near each `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="02_01">

- Fill in the `_` to record the program's output
- Fill in the `_` to call the correct functions
- Answer these questions as you study this program:
  - What is the output produced by this program?
  - What is the purpose of a user-defined function?
  - What is the input, output, and behavior of `mean`?

</codeblock>

<!-- EXERCISE } -->

</exercise>

<!-- EXERCISE { -->

<exercise id="2" title="Check: Creating a Function">

```python
def mean(numbers):
    # add the numbers together
    number_sum = sum(numbers)
    # count the values in numbers
    number_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = s / N
    return arithmetic_mean
```

Which of the following statements is *not true* about this program?

<choice>

<opt text="<code>sum</code> is a user-defined function and <code>mean</code> is a language-defined function" correct="true">

Yes, `sum` is a function defined by the language and `mean` is a user-defined function.

</opt>

<opt text="<code>mean</code> is a user-defined function and <code>sum</code> is a language-defined function">

Actually, `sum` is a function defined by the language and `mean` is a user-defined function.

</opt>

<opt text="<code>mean</code> is a user-defined function and <code>len</code> is a language-defined function">

Actually, `len` is a function defined by the language and `mean` is a user-defined function.

</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="3" title="Creating Multiple Functions">

- A program can contain more than one function
- Each function should have its own distinct purpose:
    - The `mean` function computes the arithmetic mean of `numbers`
    - The `display` function creates a textual representation of `numbers`
    - Both functions have the same type of input, a `List` called `numbers`
- The `return` statement in a user-defined function creates its output
- Complete the task near each `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="02_03">

- Fill in the `_` for the names of variables and functions
- Answer these questions as you study this program:
  - What is the name of the function that renders a list as text?
  - What is the name of the function that calculates the mean of a list?
  - What is the purpose of the `map(str, numbers)` function call in display?

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="4" title="Check: Creating Multiple Functions">

```python
def mean(numbers):
    # add the numbers together
    number_sum = sum(numbers)
    # count the values in numbers
    number_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = number_sum / number_count
    return arithmetic_mean

def display(numbers):
    comma = ", "
    return comma.join(map(str, numbers))

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# create the text of the list to display
numbers_one_text = display(numbers_one)
print(f"Values: {numbers_one_text}")
```

Which of the following is a correct statement about this program?

<choice>

<opt text="<code>display</code> is a function that accepts as input a string and returns a list of numbers">

Actually, `display` is a function that produces a string when given a list of numbers.

</opt>

<opt text="<code>display</code> is a function that accepts as input a list of numbers and returns a string" correct="true">

Yes, `display` is a function that produces a string when given a list of numbers.

</opt>

<opt text="<code>display</code> is a user-defined function and <code>mean</code> is a language-defined function">

Actually, both `display` and `mean` are user-defined functions created by a programmer.

</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="5" title="Using External Functions">

- There are many external packages, like `rich`, that add features to the Python language:
    - The `rich` package provides colorful and formatted output
    - The `print` function provided by `rich` supports the display of emojis
    - The `inspect` function provided by `rich` tells you all the details about an object
- According to <a href = "https://emojipedia.org/">Emojipedia</a>, `:mag_right:` and `:rocket:` encode a magnifying glass and a rocket
- Complete the task near each `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="02_05">

- Fill in the `_` to call the correct functions
- Fill in the `_` to display the required emojis
- Answer these questions as you study this program:
  - What is the output produced by this program?
  - What is the purpose of the `rich` package?
  - How do you display an emoji in the output?

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="6" title="Check: Using External Functions">

```python
from rich import print
from rich import inspect

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# display a message and a magnifying glass emoji
print("Inspecting the list! :mag_right:")
# inspect the list of numbers
inspect(numbers_one, methods=True)
# display a message and a rocket emoji
print("Computing the mean! :rocket:")
```

Which of the following is a correct statement about the `rich` package used in this program?

<choice>

<opt text="<code>rich</code> is a function that contains additional functions called <code>print</code> and <code>inspect</code>">

Actually, `rich` is a package that contains many functions such as `print` and `inspect`.

</opt>

<opt text="<code>rich</code> is a package that only displays emojis with its <code>print</code> function">

Actually, the `rich` package provides many functions such as `print` and `inspect`.

</opt>

<opt text="<code>rich</code> is a package that many extra functions like <code>print</code> and <code>inspect</code>" correct="true">

Yes, the `rich` package provides many functions such as `print` and `inspect`.

</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="7" title="Stretch: How to Create a Program with Functions?">

```python
from rich import print
from rich import inspect

def mean(numbers):
    # add the numbers together
    numbers_sum = sum(numbers)
    # count the values in numbers
    numbers_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = numbers_sum / numbers_count
    return arithmetic_mean

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# display a message and a magnifying glass emoji
print("Inspecting the list! :mag_right:")
# inspect the list of numbers
inspect(numbers_one, methods=True)
```

- This source code segment illustrates the following parts of a program:
  - External packages like `rich` that provide helpful functions like `print` and `inspect`
  - A user-defined function like `mean` that produces a number when provided a list as input
  - An encoding of an emoji in `:mag_right:` that the `print` function in `rich` can decode
- The user-defined function in this program has the following components:
    - Name: `mean`
    - Input: `numbers`
    - Output: `arithmetic_mean`
    - A `return` statement that provides the output
    - A body with three comments and four executable statements
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

</exercise>

<!-- EXERCISE } -->
