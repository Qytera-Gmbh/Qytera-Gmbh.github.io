![plugin header](assets/images/headerDark.svg#only-light)
![plugin header](assets/images/headerLight.svg#only-dark)

# Home

<figure markdown>
   <video controls autoplay muted>
       <source src="assets/videos/guides_results_upload_00.mp4" type="video/mp4">
       Your browser does not support the video tag.
   </video>
  <figcaption>Two passing tests and one failing test for <a href="https://example.org">https://example.org</a>. More info <a href="section/guides/uploadTestResults/">here</a>.</figcaption>
</figure>

**A plugin for coupling together Cypress and Xray.**

- [x] Upload test results to Xray
- [X] Attach screenshots as defect evidence
- [X] Attach results to existing test execution issues
- [X] Reuse existing test plan issues

**Cucumber support**

- [x] Automatic synchronization of Xray step definitions based on your feature files
- [ ] Automatic execution of tests based on Xray step definitions (:fontawesome-solid-person-digging:{ .development })

!!! note
    This plugin only works when running Cypress through the CLI (i.e. `#!sh npx cypress run`).
