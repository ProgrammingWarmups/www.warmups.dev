<p align="center">
<img src = "static/icon.png" width="250" height="250">
<br>
<b>
Programming warmups, for developers
</b>
</p>

![](../../workflows/build/badge.svg)

# www.warmups.dev

## Introduction

Based on the [course framework](https://github.com/ines/spacy-course) that [Ines
Montani](https://ines.io/) developed for her [spaCy
course](https://course.spacy.io). The front-end is powered by
[Gatsby](http://gatsbyjs.org/) and [Reveal.js](https://revealjs.com) and the
back-end code execution uses [Binder](https://mybinder.org). This web site will
only work correctly if it has a build with [Binder](https://mybinder.org) for
the current version of the `binder/requirements.txt` file.

## Running the app

To start the local development server, install [Gatsby](https://gatsbyjs.org)
and then all other dependencies. This should serve up the app on
`localhost:8000`.

```bash
npm install -g gatsby-cli  # Install Gatsby globally
npm install                # Install dependencies
npm run dev                # Run the development server
npm run build              # Build the entire site
```

## Setting up Binder

The [`requirements.txt`](binder/requirements.txt) in the repository defines the
packages that are installed when building it with Binder. You can specify the
binder settings like repo, branch and kernel type in the `"juniper"` section of
the `meta.json`. You can run the very first build via the interface on
the [Binder website](https://mybinder.org), as this gives you a detailed build
log and feedback on whether everything worked as expected.

## Adding Tests

To validate the code when the user hits "Submit", we're currently using a
slightly hacky trick. Since the Python code is sent back to the kernel as a
string, we can manipulate it and add tests – for example, exercise
`exc_01_02_01.py` will be validated using `test_01_02_01.py` (if available). The
user code and test are combined using a string template. At the moment, the
`testTemplate` in the `meta.json` looks like this:

```
from wasabi import Printer
__msg__ = Printer()
__solution__ = """${solution}"""
${solution}

${test}
try:
    test()
except AssertionError as e:
    __msg__.fail(e)
```

If present, `${solution}` will be replaced with the string value of the
submitted user code. In this case, we're inserting it twice: once as a string so
we can check whether the submission includes something, and once as the code, so
we can actually run it and check the objects it creates. `${test}` is replaced
by the contents of the test file. It's also making
[`wasabi`](https://github.com/ines/wasabi)'s printer available as `__msg__`, so
we can easily print pretty messages in the tests. Finally, the `try`/`accept`
block checks if the test function raises an `AssertionError` and if so, displays
the error message. This also hides the full error traceback (which can easily
leak the correct answers).

A test file could then look like this:

```python
def test():
    assert "spacy.load" in __solution__, "Are you calling spacy.load?"
    assert nlp.meta["lang"] == "en", "Are you loading the correct model?"
    assert nlp.meta["name"] == "core_web_sm", "Are you loading the correct model?"
    assert "nlp(text)" in __solution__, "Are you processing the text correctly?"
    assert "print(doc.text)" in __solution__, "Are you printing the Doc's text?"

    __msg__.good(
        "Well done! Now that you've practiced loading models, let's look at "
        "some of their predictions."
    )
```

The string answer is available as `__solution__`, and the test also has access
to the solution code.
