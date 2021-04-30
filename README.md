<p align="center">
<img src = "static/icon.png" width="250" height="250">
<br>
<b>
Programming warmups, for developers
</b>
</p>

# www.warmups.dev

![](../../workflows/build/badge.svg)

## Introduction

Based on the [course framework](https://github.com/ines/spacy-course) that [Ines
Montani](https://ines.io/) developed for her [spaCy
course](https://course.spacy.io). The front-end is powered by
[Gatsby](http://gatsbyjs.org/) and [Reveal.js](https://revealjs.com) and the
back-end code execution uses [Binder](https://mybinder.org). This web site will
only work correctly if it has a build with [Binder](https://mybinder.org) for
the current version of the `binder/requirements.txt` file.

## Running the Site

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
