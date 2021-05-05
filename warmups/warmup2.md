---
title: 'Warmup 2: How to Create a Program with Functions?'
description:
  'Learn how to organize a program into separate functions with distinguished behavior'
prev: /warmup1
next: /warmup3
type: chapter
id: 2
---

<!-- EXERCISE -->

<exercise id="1" title="Creating a Function">

- Using the following source code, can you find these parts of a program?
  - User-defined function:
      - Name: `mean`
      - Input: `numbers`
      - Output: `arithmetic_mean`
      - Body of the `mean` method
  - Lists: `numbers_one` and `numbers_two`
  - Language-defined functions: `sum`, `len`, and `print`
- What are the similarities and differences between `mean` and `sum`?
- Complete the task near the `TODO` markers, removing the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="02_01">

- Fill in the `_` to record the program's output
- Answer these questions as you study this program:
  - What is the output produced by this program?
  - What is the purpose of a user-defined function?
  - What is the input, output, and behavior of `mean`?

</codeblock>

</exercise>

<!-- EXERCISE -->

<exercise id="2" title="Check: Creating a Function">

```python
def mean(numbers):
    """Compute the arithmetic mean of the values in numbers."""
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

<!-- EXERCISE -->

<exercise id="3" title="Creating Multiple Functions">

- Using the following source code, can you find these parts of a program?
  - User-defined function:
      - Name: `mean`
      - Input: `numbers`
      - Output: `arithmetic_mean`
      - Body of the `mean` method
  - Lists: `numbers_one` and `numbers_two`
  - Language-defined functions: `sum`, `len`, and `print`
- What are the similarities and differences between `mean` and `sum`?
- Complete the task near the `TODO` markers, removing the `TODO` when finished
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
