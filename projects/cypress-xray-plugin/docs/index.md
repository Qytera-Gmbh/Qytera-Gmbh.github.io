---
hide:
  - toc
---

![plugin header](assets/images/headerDark.svg#only-light)
![plugin header](assets/images/headerLight.svg#only-dark)

<h1><!-- no title, the image is title enough --></h1>

<figure markdown>
   <video controls autoplay muted>
     <source src="assets/videos/showcase.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>
  <figcaption>Two passing tests and one failing test for <a href="https://example.org">https://example.org</a>.</figcaption>
</figure>

<h2 style="color:var(--md-default-fg-color--light)"><i>A Cypress plugin for Xray integration. Supports Xray Server/DC and Xray Cloud.</i></h2>

- Upload test results to Xray
- Attach screenshots as test execution evidence
- Attach web requests as test execution evidence
- Attach videos to test execution issues
- Reuse existing test execution and test plan issues
- CI/CD ready
- Cucumber support

:smartbear-cucumber: <span class="cucumber"><i>Cucumber only:</i></span>

- Automatic import of feature files to Jira

:fontawesome-solid-person-digging:{ .development } <span class="development"><i>Future features:</i></span>

- Automatic execution of Cucumber tests based on Xray step definitions

!!! note
    This plugin only works when running Cypress through the CLI (i.e. `#!sh npx cypress run`).
