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

- Explore the [notional machine for Python](http://teachtogether.tech/en/#s:models-notional) that reflects what Python programs do when executed
- The notational machine has twelve concepts, can you grasp the basics of each one? **Examples:**
- **Notion 7**: "When code is executed, Python steps through the instructions,
doing what each one tells it to in turn."
- **Notion 8**: "Some instructions make Python read data, do calculations, and
create new data."
- `numbers = [2, 4, 6, 8]` creates a list that contains four numbers in it
- `sum(numbers)` calls the `sum` function to add together the values in `numbers`
- `s = sum(numbers)` stores the resulting sum in a new variable called `s`
- `mean = s / N` divides `s` by `N` and stores the result in a new variable
called `mean`

Notes: 🤩 As before, this Python program calculates the arithmetic mean of a
list of numbers. Leveraging the terms that you read in the [notional machine for
Python](http://teachtogether.tech/en/#s:models-notional), can you explain in
detail the purpose of each line of the program's source code?

---

# Ready to gauge your understanding?

Notes: ⏱  Before moving onto the fitness check, make sure that you can use the
[notional machine for Python](http://teachtogether.tech/en/#s:models-notional)
to explain each step in the Python program that calculates the arithmetic mean.
