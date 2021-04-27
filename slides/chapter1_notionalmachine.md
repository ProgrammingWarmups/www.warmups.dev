---
type: slides
---

# What happens when a Python program runs?

Notes: 🤯 Along with understanding the parts of a Python program, you need to
understand what happens when a specific line of code in the program runs. This
part of the warmup leverages the ideas in a book, called <a href =
"http://teachtogether.tech/en/index.html">Teaching Tech Together</a>, to develop
a *notion* about what happens when a Python program executes on a computer.
Don't forget that a notion is a belief or conception about something. Now, you
are going to learn a *notional machine* for Python. I know, it sounds strange,
but it's simply a way to understand a program's behavior!

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

# Let's practice!

Notes: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tristique
libero at est congue, sed vestibulum tortor laoreet. Aenean egestas massa non
commodo consequat. Curabitur faucibus, sapien vitae euismod imperdiet, arcu erat
semper urna, in accumsan sapien dui ac mi. Pellentesque felis lorem, semper nec
velit nec, consectetur placerat enim.
