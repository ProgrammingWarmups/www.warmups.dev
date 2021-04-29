---
title: 'Warmup 1: What happens when a Python program runs?'
description:
 'Build and apply a mental model about what happens when you run a Python program'
prev: null
next: /chapter2
type: chapter
id: 1
---

<!-- EXERCISE -->

<exercise id="1" title="What are Some Parts of Python Program?">

- Can you find these parts a Python program?
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

<exercise id="2" title="Check: Parts of a Python Program">

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

Using this Python program that calculates the arithmetic mean, what can exist in a Python program?

<choice>

<opt text="Variables that provide a non-executable reminder of the code's behavior">

Nope, variables store values on behalf of the Python program.

</opt>

<opt text="Variables that store values used for the Python program's computation" correct="true">

Yep, variables store values that can then be used in a computation.

</opt>

<opt text="Comments with values that the Python program displays in its output">

Nope, comments are human-readable reminders of the code's behavior.

</opt>
</choice>

</exercise>

<!-- EXERCISE -->

<exercise id="3" title="What Happens When a Python Program Runs?">

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
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<hr>

<codeblock id="01_03">

- Fill in the `_` to record the program's output
- Answer these questions as you study this program:
  - What is the purpose of a variable?
  - What is the output produced by this program?
  - What are the input(s), output(s), and behavior of functions like `sum`,
  `len`, and `print`?

</codeblock>

</exercise>


<!-- EXERCISE -->

<exercise id="4" title="Check: Running a Python Program">

Using the Python program that calculated the arithmetic mean, what happens when the program runs?

<choice>

<opt text="It calculates the arithmetic mean by running <code>N / s</code> and storing it in <code>mean</code>">

Nope, that is not the correct equation for the arithmetic mean.

</opt>

<opt text="It calculates the arithmetic by running <code>s \ n</code> and storing it in <code>mean</code>">

Nope, the Python program does not have a variable called `n`

</opt>

<opt text="It calculates the arithmetic by running <code>s / N</code> and storing it in <code>mean</code>" correct="true">

Yep, that is the correct equation for the arithmetic mean.

</opt>

</choice>

</exercise>

<!-- EXERCISE -->

<exercise id="5" title="Improving a Python Program">

- You can edit and run this program in your web browser
- The first time you click "Run Code" it may take 60 seconds to run
- Don't worry, every other run will be much faster
- The program should produce the output `Mean: 5.0`
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<codeblock id="01_05">

- Fill in the `_` in `numbers = [_, _, _, _]` to make a new list of values
- Fill in the `_` in `mean = _ / _` to compute the arithmetic mean
- Fill in the `_` in `print(f"Mean: {____}")` to display the arithmetic mean
- Don't forget that the program must produce the output of `Mean: 5.0`

</codeblock>

</exercise>
