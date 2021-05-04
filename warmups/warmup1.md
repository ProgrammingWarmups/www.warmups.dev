---
title: 'Warmup 1: What Happens When a Program Runs?'
description:
 'Investigate the static structure and dynamic behavior of a program'
prev: null
next: /warmup2
type: chapter
id: 1
---

<!-- EXERCISE -->

<exercise id="1" title="Parts of a Program">

- Using the following source code, can you find these parts of a program?
  - Variables: `numbers`, `s`, `N`, and `mean`
  - Functions: `sum`, `len`, and `print`
  - Comments: `# create a list of numbers`
- What do you think is the purpose of these program parts?
- Complete the task near the `TODO` marker, removing the `TODO` when finished!
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="01_01">

- Fill in the `_` to record the program's output
- Answer these questions as you study this Python program:
  - What is the output produced by this program?
  - What is the purpose of a variable, function, or comment?
  - What are the input(s), output(s), and behavior of functions like `sum`,
  `len`, and `print`?

</codeblock>

</exercise>

<!-- EXERCISE -->

<exercise id="2" title="Check: Parts of a Program">

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

<!-- EXERCISE -->

<exercise id="3" title="Running a Program">

- A [notional machine for Python](http://teachtogether.tech/en/#s:models-notional) explains what Python programs do when they are run
- The notational machine has twelve concepts. Can you grasp the basics of each one?
- Excerpts of three of the twelve notions about Python programs:
  - **Notion 5**: "Lists, sets, and other collections store references to other data rather ..."
  - **Notion 7**: "When code is executed, Python steps through the instructions, doing ..."
  - **Notion 8**: "Some instructions make Python read data, do calculations, and
create new data."
- Descriptions of the behavior of lines in this Python program:
  - `numbers = [2, 4, 6, 8]` creates a list that contains four numbers in it
  - `s = sum(numbers)` stores the output of `sum` in a new variable called `s`
  - `mean = s / N` divides `s` by `N` and stores the result in a new variable called `mean`
- Complete the tasks indicated by the `TODO` marker, removing the `TODO` when finished!
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="01_03">

- Fix the mistakes in the program so that it outputs `Mean: 5.0`
- Answer these questions as you study this program:
  - What is the purpose of the `len` and `sum` functions?
  - What values should the variables `s` and `N` contain?
  - Why don't developers keep `TODO` markers in source code?

</codeblock>

</exercise>

<!-- EXERCISE -->

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

<!-- EXERCISE -->

<exercise id="5" title="Modifying a Program's Source Code">

- Complete the tasks indicated by each `TODO` marker, removing the `TODO` when finished!
  - Ensure that the program produces the output `Mean: 4.0` by adding values to `numbers`
  - Add the correct equation for calculating the arithmetic mean
  - Use the correct `print` statement to display the arithmetic mean
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="01_05">

- Fill in the `_` in `numbers = [_, _, _, _]` to make a new list of values
- Fill in the `_` in `mean = _ / _` to compute the arithmetic mean
- Fill in the `_` in `print(f"Mean: {____}")` to display the arithmetic mean
- Don't forget that the program must produce the output of `Mean: 4.0`

</codeblock>

</exercise>

<!-- EXERCISE -->

<exercise id="6" title="Check: Modifying a Python Program">

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

Using this program as an example, what happens when its statements are run?

<choice>

<opt text="It calculates the arithmetic mean by running <code>N / s</code> and storing it in <code>mean</code>">

No, that is not the correct equation for the arithmetic mean.

</opt>

<opt text="It calculates the arithmetic mean by running <code>s / n</code> and storing it in <code>mean</code>">

No, the Python program does not have a variable called `n`

</opt>

<opt text="It calculates the arithmetic by running <code>s / N</code> and storing it in <code>mean</code>" correct="true">

Yes, that is the correct equation for the arithmetic mean.

</opt>

</choice>

</exercise>
