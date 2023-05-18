---
hide:
  - toc
---

![plugin header](assets/images/headerDark.svg#only-light)
![plugin header](assets/images/headerLight.svg#only-dark)

<h1><!-- no title, the image is title enough --></h1>

<figure markdown>
   <video controls autoplay muted>
       <source src="assets/videos/guides_results_upload_00.mp4" type="video/mp4">
       Your browser does not support the video tag.
   </video>
  <figcaption>Two passing tests and one failing test for <a href="https://example.org">https://example.org</a>. More info <a href="section/guides/uploadTestResults/">here</a>.</figcaption>
</figure>

**A plugin for coupling together Cypress and Xray.**

- [x] Upload test results to Xray
- [x] Attach screenshots as test execution evidence
- [x] Attach videos to test execution issues
- [x] Reuse existing test execution and test plan issues
- [x] CI/CD ready

**Cucumber support** (<span class="development">experimental</span> :fontawesome-solid-person-digging:{ .development })

- [x] Automatic synchronization of Xray step definitions based on your feature files
- [ ] Automatic execution of tests based on Xray step definitions

!!! note
    This plugin only works when running Cypress through the CLI (i.e. `#!sh npx cypress run`).
