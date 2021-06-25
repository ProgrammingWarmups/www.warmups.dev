---
title: 'What Are Variables?'
description:
 'Learn about variables and how to use them in your code'
slug: /intro_to_variables
type: chapter
---

<!-- EXERCISE { -->

<exercise id="1" title="Introduction to Variables">

- Variables are containers that store data
- This data can be used or changed later in a program
- Variables are assigned the data they store using the `=` operator

Below, `name` is a variable that is assigned the data `John`:
```
name = "John"
```

The code below computes properties of a cuboid with a length of `10`, width of `11`, and height of `12`.

***Update the code to compute properties of a cuboid with a length of `13`, width of `14`, and height of `15`***

<br>

<codeblock id="intro_to_variables_01a">

- The formula for a cuboid's base area is `length × width`
- The formula for a cuboid's surface area is `2 × (length × width) + 2 × (length × height) + 2 × (width × height)`
- The formula for a cuboid's volume is `length × width × height`

</codeblock>

Here's the same code, but using variables to contain the length, width, and height.

***Update the code to compute properties of a cuboid with a length of `13`, width of `14`, and height of `15`***

<br>

<codeblock id="intro_to_variables_01b">

- Only three values need to be updated

</codeblock>

A bit easier, right? Now, how do you know when to use variables?

**A good rule of thumb is to use variables to store data that could be reused later in the code.**

<br>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="2" title="Check: Introduction to Variables">

Which of the following statements about variables is true?

<choice>

<opt text="Variables provide a non-executable reminder of the code's behavior">
Variables do not provide a non-executable reminder of the code's behavior.
</opt>

<opt text="Variables store data that can be used or changed later in the program" correct="true">
Variables store data that can be used or changed later in the program.
</opt>

<opt text="Variables print output to the console">
Variables do not print output to the console.
</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="3" title="Naming Variables">

- In Python, there are several rules for naming variables:
    - Must start with a letter or underscore (`_`)
    - Can only contain letters, numbers, and underscores
    - Are case-sensitive

<br>

Can you fix the variable naming mistakes below so that the code prints `John is 22 years old and likes to eat apples.`?

<br>

<codeblock id="intro_to_variables_03">

- All three variables have issues with their names

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="4" title="Check: Naming Variables">

Which of the following variables is legally named?

<choice>

<opt text="<code>3rd_item</code>">
Variables can only start with either a letter or underscore.
</opt>

<opt text="<code>third#_item</code>">
Variables can only contain letters, numbers, and underscores.
</opt>

<opt text="<code>thIRD___it3m</code>" correct=true>
As strange as it looks, this is technically a legal variable name!
Now, just because you can doesn't mean you should...
</opt>

</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="5" title="Reserved Words">

- In Python, there are case-sensitive keywords that are "reserved" for specific purposes and cannot be used as variable names. Some examples are:
    - `and`
    - `def`
    - `return`
    - `True`
    - `while`
- No need to memorize these keywords--instead, whenever you suspect that a variable name might be a keyword, refer to online documentation, such as [W3School's List of Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp)

<br>

***Fix the code below so that it prints `My favorite class is CMPSC 100.`***

<br>

<codeblock id="intro_to_variables_05">

- Rename any variables that are listed as keywords in [W3School's List of Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp)

</codeblock>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="6" title="Check: Reserved Words">

Referring to [W3School's List of Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp), which of the following variables is legally named?

<choice>

<opt text="<code>global</code>">
<code>global</code> is a Python keyword.
</opt>

<opt text="<code>from</code>">
<code>from</code> is a Python keyword.
</opt>

<opt text="<code>from_location</code>" correct=true>
While variable names may not <b><i>be</i></b> a keyword, they can certainly contain keywords!
</opt>

<opt text="<code>with</code>">
<code>with</code> is a Python keyword.
</opt>


</choice>

</exercise>

<!-- EXERCISE } -->

<!-- EXERCISE { -->

<exercise id="7" title="Review: What Are Variables?">

- Variables are containers that store data, which can be used or changed later in a program, and are assigned using the `=` operator
- In Python, variable names must start with a letter or underscore, can only contain letters, numbers, and underscores, and are case-sensitive
- Variable names must not be keywords, which are case-sensitive words reserved in Python for specific purposes

<br>

</exercise>

<!-- EXERCISE } -->
