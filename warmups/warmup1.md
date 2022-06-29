---
title: 'What Happens When a Program Runs?'
description:
 'Investigate the static structure and dynamic behavior of a program'
slug: /warmup1
type: chapter
---

<!-- EXERCISE { -->

<exercise id="1" title="Parts of a Program">

- Using the following source code, can you find these parts of a program?
  - Variables: `numbers`, `s`, `N`, and `mean`
  - Functions: `sum`, `len`, and `print`
  - Comments: `# create a list of numbers`
- What do you think is the purpose of these program parts?
- Complete the task near the `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="warmup1_01">

- Fill in the `_` to record the program's output
- Answer these questions as you study this program:
  - What is the output produced by this program?
  - What is the purpose of a variable, function, or comment?
  - What are the input(s), output(s), and behavior of functions like `sum`,
  `len`, and `print`?

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="2" title="Check: Parts of a Program">

```python
# create a list of numbers
numbers = [2, 4, 6, 8]
# add the numbers together
s = sum(numbers)
# count how many values are in numbers
N = len(numbers)
# compute the arithmetic mean
mean = s / N
# display the arithmetic mean
print(f"Mean: {mean}")
```

What constructs are evident in this program?

<choice>

<opt text="Variables that provide a non-executable reminder of the code's behavior">

No, variables store values on behalf of the program.

</opt>

<opt text="Variables that store values used for the program's computation" correct="true">

Yes, variables store values that can then be used in a computation.

</opt>

<opt text="Comments with values that the program displays in its output">

Nope, comments are human-readable reminders of the code's behavior.

</opt>
</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="3" title="Running a Program">

- A [notional machine for Python](http://teachtogether.tech/en/#s:models-notional) explains what programs do when they are run
- The notational machine has twelve concepts. Can you grasp the basics of each one?
- Excerpts of three of the twelve notions about Python programs:
  - **Notion 5**: "Lists, sets, and other collections store references to other data rather ..."
  - **Notion 7**: "When code is executed, Python steps through the instructions, doing ..."
  - **Notion 8**: "Some instructions make Python read data, do calculations, and
create new data."
- Descriptions of the behavior of lines in this program:
  - `numbers = [2, 4, 6, 8]` creates a list that contains four numbers in it
  - `s = sum(numbers)` stores the output of `sum` in a new variable called `s`
  - `mean = s / N` divides `s` by `N` and stores the result in a new variable called `mean`
- Complete the tasks indicated by the `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="warmup1_03">

- Fix the mistakes in the program so that it outputs `Mean: 5.0`
- Answer these questions as you study this program:
  - What is the purpose of the `len` and `sum` functions?
  - What values should the variables `s` and `N` contain?
  - Why don't developers keep `TODO` markers in source code?

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="4" title="Check: Running a Program">

```python
# create a list of numbers
numbers = [2, 4, 6, 8]
# add the numbers together
s = sum(numbers)
# count the values in numbers
N = len(numbers)
# compute the arithmetic mean
mean = s / N
# display the arithmetic mean
print(f"Mean: {mean}")
```

What is the purpose of the statement `s = sum(numbers)` in this program?

<choice>

<opt text="It adds together the values in <code>numbers</code> and stores them in the variable <code>s</code>" correct="true">

Yes, the `sum` functions adds together 2, 4, 6, and 8 and stores 20 in the variable `s`.

</opt>

<opt text="It calculates the mean of the values in <code>numbers</code> and stores it in the variable <code>mean</code>">

No, this line of source code does not calculate the arithmetic mean.

</opt>

<opt text="It calculates the number of values in <code>numbers</code> and stores it in the variable <code>N</code>">

No, this line of source code does not calculate the number of values in the list.

</opt>

</choice>

</exercise>

<!-- EXERCISE { -->

<exercise id="5" title="Modifying a Program's Source Code">

- Modify the program's source code so that it:
  - Produces the output `Mean: 4.0` by adding suitable values to `numbers`
  - Uses the correct equation for calculating the arithmetic mean
  - Uses the correct `print` statement to display the arithmetic mean
- Complete the tasks indicated by each `TODO` marker and remove the `TODO` when finished
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="warmup1_05">

- Fill in the `_` in `numbers = [_, _, _, _]` to make a new list of values
- Fill in the `_` in `mean = _ / _` to compute the arithmetic mean
- Fill in the `_` in `print(f"Mean: {____}")` to display the arithmetic mean
- Don't forget that the program must produce the output of `Mean: 4.0`

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="6" title="Check: Modifying a Program's Source Code">

```python
# create a list of numbers
numbers = [1, 3, 5, 7]
# add the numbers together
s = sum(numbers)
# count the values in numbers
N = len(numbers)
# compute the arithmetic mean
mean = s / N
# display the arithmetic mean
print(f"Mean: {mean}")
```

What happens when the statements of this program are run?

<choice>

<opt text="It calculates the arithmetic mean by running <code>N / s</code> and storing it in <code>mean</code>">

No, that is not the correct equation for the arithmetic mean.

</opt>

<opt text="It calculates the arithmetic mean by running <code>s / n</code> and storing it in <code>mean</code>">

No, the program's source code does not have a variable called `n`

</opt>

<opt text="It calculates the arithmetic mean by running <code>s / N</code> and storing it in <code>mean</code>" correct="true">

Yes, that is the correct description of this program's behavior.

</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="7" title="Stretch: What Happens When a Program Runs?">

```python
# create a list of numbers
numbers = [1, 3, 5, 7]
# add the numbers together
s = sum(numbers)
# count the values in numbers
N = len(numbers)
# compute the arithmetic mean
mean = s / N
# display the arithmetic mean
print(f"Mean: {mean}")
```

- This source code segment illustrates the following parts of a program:
  - Variables like `numbers`, `s`, `N`, and `mean` store values of computations
  - Functions like `sum`, `len`, and `print` accept an input and produce an output
  - Comments like `# create a list of numbers` aid in understanding the program
- A [notional machine for Python](http://teachtogether.tech/en/#s:models-notional) explains what programs do when they are run, such as:
  - Each line of the source code is executed in sequence, performing the specified action
  - The line `numbers = [1, 3, 5, 7]` creates a list that contains the numbers 1, 3, 5, and 7
  - The `sum` functions adds together the values in `numbers` and stores 16 in the variable `s`.
- A developer can modify the source code of a program to change its behavior or fix a problem
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

</exercise>

<!-- EXERCISE } -->
