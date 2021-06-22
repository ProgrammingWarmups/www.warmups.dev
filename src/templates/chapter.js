import React, { useState } from 'react'
import { graphql, navigate } from 'gatsby'
import useLocalStorage from '@illinois/react-use-local-storage'

import { renderAst } from '../markdown'
import { ChapterContext } from '../context'
import Layout from '../components/layout'
import { Button } from '../components/button'

import classes from '../styles/chapter.module.sass'

import warmupOrder from '../../warmups/order'

const Template = ({ data }) => {
    const { markdownRemark, site } = data
    const { courseId } = site.siteMetadata
    const { frontmatter, htmlAst, fields } = markdownRemark
    const { title, description, id } = frontmatter
    const [activeExc, setActiveExc] = useState(null)
    const [completed, setCompleted] = useLocalStorage(`${courseId}-completed-${id}`, [])
    const html = renderAst(htmlAst)
    const slug = fields.slug
    const warmupIndex = warmupOrder.indexOf(slug)
    if (warmupIndex < 0) {
        console.error(`Could not find ${slug} in warmup order.
        Please add to warmup order file to ensure that 'Previous Warmup' and 'Next Warmup' buttons behave as expected.`)
    }
    const prev = warmupIndex <= 0 ? null // If first warmup, no 'Previous Warmup' button
        : warmupOrder[warmupIndex - 1]
    const next = warmupIndex >= warmupOrder.length - 1 ? null // If last warmup, no 'Next Warmup' button
        : warmupOrder[warmupIndex + 1]
    const buttons = [
        { slug: prev, text: '« Previous Warmup' },
        { slug: next, text: 'Next Warmup »' },
    ]

    return (
        <ChapterContext.Provider value={{ activeExc, setActiveExc, completed, setCompleted }}>
            <Layout title={title} description={description}>
                {html}

                <section className={classes.pagination}>
                    {buttons.map(({ slug, text }) => (
                        <div key={slug}>
                            {slug && (
                                <Button variant="secondary" small onClick={() => navigate(slug)}>
                                    {text}
                                </Button>
                            )}
                        </div>
                    ))}
                </section>
            </Layout>
        </ChapterContext.Provider>
    )
}

export default Template

export const pageQuery = graphql`
    query($slug: String!) {
        site {
            siteMetadata {
                courseId
            }
        }
        markdownRemark(fields: { slug: { eq: $slug } }) {
            htmlAst
            frontmatter {
                id
                title
                description
            },
            fields {
                slug
            }
        }
    }
`
