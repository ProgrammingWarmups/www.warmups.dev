---
title: 'Warmup 1: What happens when a Python program runs?'
description:
 'Build and apply a mental model about what happens when you run a Python program'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="What are the Parts of a Python Program?" type="slides">

<slides source="chapter1_programparts">
</slides>

</exercise>

<exercise id="2" title="Check: Parts of a Python program">

Using the example that calculated the arithmetic mean, what can exist in a Python program?

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

<exercise id="3" title="What Happens When a Python Program Runs?" type="slides">

<slides source="chapter1_notionalmachine">
</slides>

</exercise>

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

<exercise id="5" title="Modifying a Python Program">

- You can edit and run this program in your web browser
- The first time you click "Run Code" it may take 60 seconds to run
- Don't worry, every other run will be much faster
- The program should produce the output `Mean: 5.0`
- Questions or comments about this warmup? <a href = "https://github.com/gkapfham/www.warmups.dev/discussions">Join the discussion!</a>

<codeblock id="01_03">

- Fill in the `_` in `numbers = [_, _, _, _]` to make a new list of values
- Fill in the `_` in `mean = _ / _` to compute the arithmetic mean
- Fill in the `_` in `print(f"Mean: {____}")` to display the arithmetic mean
- Don't forget that the program must produce the output of `Mean: 5.0`

</codeblock>

</exercise>

