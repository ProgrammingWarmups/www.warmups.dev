---
type: slides
---

# What are the key parts of a Python program?

Notes: 👏 You're going exploring some basic constructs in the Python programming
language and learn more about what happens when a developer runs a Python
program. As you study these examples, look for source code segments that make
sense and take a guess at what they do. Instead of getting overwhelmed when you
encounter a technical concept or Python source code that looks confusing, make a
note of why it looks strange and remember that you will understand it soon!

---

# Calculating the arithmetic mean of a list of numbers

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

```out
Mean: 4.0
```

- **Variables**: `numbers`, `s`, `N`, and `mean`
- **Functions**: `sum`, `len`, and `print`
- **Comments**: `# create a list of numbers`
- When a developer runs this Python program, it produces output
- Okay, try to answer these questions:
  - What is the purpose of a variable?
  - What is the output produced by this program?
  - What are the input(s), output(s), and behavior of functions like `sum`,
  `len`, and `print`?

Notes: 🤩 This Python program calculates the arithmetic mean, or the average, of
a list of numbers. Without getting caught up in the details, can you determine
the purpose of each line of source code? Go ahead, say your guess out loud!

---

# Ready to gauge your understanding?

Notes: ⏱  Before moving onto the fitness check, make sure that you have an
intuitive understanding of variables, functions, and comments and how they
worked in the Python program that calculated the arithmetic mean.
