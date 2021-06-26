<p align="center">
<img src = "static/icon.png" width="250" height="250">
<br>
<b>
Programming warmups, for developers
</b>
</p>

# www.warmups.dev

![](../../workflows/build/badge.svg) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gkapfham/www.warmups.dev/binder) [![Netlify Status](https://api.netlify.com/api/v1/badges/0a36441a-791b-40d0-a582-256dffd69514/deploy-status)](https://app.netlify.com/sites/warmups/deploys)

## Introduction

Based on the [course framework](https://github.com/ines/spacy-course) that [Ines
Montani](https://ines.io/) developed for her [spaCy
course](https://course.spacy.io), this repository contains the source code for
the [www.warmups.dev](https://www.warmups.dev/) platform that offers developers
the opportunity to master basic programming skills and rev up their minds. The
front-end is powered by [Gatsby](http://gatsbyjs.org/) and
[Reveal.js](https://revealjs.com) and the back-end code execution uses
[Binder](https://mybinder.org). This web site will only work correctly if it has
a build with [Binder](https://mybinder.org) for the current version of the
`binder/requirements.txt` file.

## Running the Site

This Node.js needs to be version 10.22.0, so you first have to make sure that you're entering these commands with that
version. To do that, in your bash terminal, enter the following to install that version and use it:

```bash
nvm install 10.22.0
```

[nvm](https://heynode.com/tutorial/install-nodejs-locally-nvm) stands for Node Version Manager, and it acts like pipenv for Python, which allows you to switch between different `Node.js` versions. `Node.js` is a runtime environment that runs websites by executing Javascript code. [npm](https://www.npmjs.com) stands for Node Package Manager, which keeps track of all of the modules within a web application.

To start the local development server, install [Gatsby](https://gatsbyjs.org)
and then all other dependencies. This should serve up the app on
`localhost:8000`.

```bash
npm install -g gatsby-cli  # Install Gatsby globally
npm install                # Install dependencies
npm run dev                # Run the development server
npm run build              # Build the entire site
```

## Setup for and Use of Binder

The [`requirements.txt`](binder/requirements.txt) in the repository defines the
packages that are installed when building it with Binder. You can specify the
binder settings like repo, branch and kernel type in the `"juniper"` section of
the `meta.json`. You can run the very first build via the interface on
the [Binder website](https://mybinder.org), as this gives you a detailed build
log and feedback on whether everything worked as expected. Importantly, a push
to the `binder` branch of this repository will automatically build and deploy a
Binder image for use with the deployed version of the web site.

## Adding a New Warmup

1. Create a new Markdown (MD) document in `warmups/` by copying an existing
warmup.
2. Update the `title`, `description`, and `slug` fields in the frontmatter.
`slug` is the path at which the warmup will be located on the site. It can
usually just be the name of the warmup MD document. 
3. Add the `slug` to `warmups/order.js` in the position it belongs.
4. Within the new `warmups/` MD document, the `<codeblock>` elements
should have an `id` that reflects the name of the MD document.
5. When adding Python exercises in `exercises/`, use this `<codeblock>` `id` in
the names of the corresponding starter, solution, and test files.
