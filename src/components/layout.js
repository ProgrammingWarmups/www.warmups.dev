import React from 'react'
import { StaticQuery, graphql } from 'gatsby'

import SEO from './seo'
import { Link } from './link'
import { H3 } from './typography'
import Logo from '../../static/logo.svg'

import '../styles/index.sass'
import classes from '../styles/layout.module.sass'

const Layout = ({ isHome, title, description, children }) => {
    return (
        <StaticQuery
            query={graphql`
                {
                    site {
                        siteMetadata {
                            title
                            description
                            bio
                            showProfileImage
                            footerLinks {
                                text
                                url
                            }
                        }
                    }
                }
            `}
            render={data => {
                const meta = data.site.siteMetadata
                return (
                    <>
                        <SEO title={title} description={description} />
                        <main className={classes.root}>
                            {!isHome && (
                                <h1 className={classes.logo}>
                                    <Link hidden to="/">
                                        <Logo width={75} height={75} aria-label={meta.title} />
                                    </Link>
                                </h1>
                            )}
                            <div className={classes.content}>
                                {(title || description) && (
                                    <header className={classes.header}>
                                        {title && <h1 className={classes.title}>{title}</h1>}
                                        {description && (
                                            <p className={classes.description}>{description}</p>
                                        )}
                                    </header>
                                )}
                                {children}
                            </div>

                            <footer className={classes.footer}>
                                <div className={classes.footerContent}>
                                    <section className={classes.footerSection}>
                                      <H3><em>Wait</em>, what is this?</H3>

                                      <p>Building on a framework developed by <Link variant="secondary" to="https://ines.io">Ines Montani</Link>, the <Link variant="secondary" to="https://warmups.dev">warmups.dev</Link> platform offers emerging and experienced developers the opportunity to practice programming in Python. Offering a variety of exercises that stretch your programming muscles, <Link variant="secondary" to="https://warmups.dev">warmups.dev</Link> leverages insights from educational research to help you to effectively master programming skills.</p>

                                    </section>

                                    <section className={classes.footerSection}>
                                      <H3><em>Okay</em>, who created it?</H3>
                                        {meta.showProfileImage && (
                                            <img
                                                src="/profile.jpg"
                                                alt=""
                                                className={classes.profile}
                                            />
                                        )}

                                            <p>An innovator in technical areas such as software engineering and software testing, <Link variant="secondary" to="https://www.gregorykapfhammer.com">Gregory M. Kapfhammer</Link> develops and maintains <Link variant="secondary" to="https://warmups.dev">warmups.dev</Link>. No stranger to being stuck on a programming problem, Gregory hopes that this platform will help learners to explore the field of software development. Have a question or comment for Gregory? Send him <Link variant="secondary" to="https://www.gregorykapfhammer.com/contact/">feedback</Link>!</p>

                                    </section>

                                    {meta.footerLinks && (
                                        <ul className={classes.footerLinks}>
                                            {meta.footerLinks.map(({ text, url }, i) => (
                                                <li key={i} className={classes.footerLink}>
                                                    <Link variant="secondary" to={url}>
                                                        {text}
                                                    </Link>
                                                </li>
                                            ))}
                                        </ul>
                                    )}
                                </div>
                            </footer>
                        </main>
                    </>
                )
            }}
        />
    )
}

export default Layout
