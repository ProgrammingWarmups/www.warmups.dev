import React from 'react'
import { graphql } from 'gatsby'

import Layout from '../components/layout'
import { Link } from '../components/link'
import Logo from '../../static/logo.svg'

import classes from '../styles/index.module.sass'

export default ({ data }) => {
  const siteMetadata = data.site.siteMetadata
  const chapters = data.allMarkdownRemark.edges.map(({ node }) => ({
    slug: node.fields.slug,
    title: node.frontmatter.title,
    description: node.frontmatter.description,
  }))
  return (
    <Layout isHome>
      <Logo className={classes.logo} aria-label={siteMetadata.title} />

      <section>
        <h1 className={classes.subtitle}>Warmups, <em>for Developers</em></h1>
        <div className={classes.introduction}>
          <p> If you are like many developers, you may find it frustrating when you are starting to program for the first time &mdash; or returning to your code after the weekend. <span role="img" aria-label="wink">😉</span> Whether you are procrastinating or overwhelmed by a task, <Link variant="secondary" to="https:warmups.dev"> warmups.dev</Link> helps you to review basic programming skills and rev up your mind. Ready, set, go! <span role="img" aria-label="rocket">🚀</span> </p>
        </div>
      </section>

  {chapters.map(({ slug, title, description }) => (
    <section key={slug} className={classes.chapter}>
      <h2 className={classes.chapterTitle}>
        <Link hidden to={slug}>
          {title}
        </Link>
      </h2>
      <p className={classes.chapterDesc}>
        <Link hidden to={slug}>
          {description}
        </Link>
      </p>
    </section>
  ))}
  </Layout>
  )
}

export const pageQuery = graphql`
    {
        site {
            siteMetadata {
                title
            }
        }
        allMarkdownRemark(
            sort: { fields: [frontmatter___title], order: ASC }
            filter: { frontmatter: { type: { eq: "chapter" } } }
        ) {
            edges {
                node {
                    fields {
                        slug
                    }
                    frontmatter {
                        title
                        description
                    }
                }
            }
        }
    }
`
