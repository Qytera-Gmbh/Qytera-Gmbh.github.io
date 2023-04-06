# Upload test results

<figure markdown>
  ![standard plugin workflow](../../assets/images/cypressXrayLight.svg#only-light)
  ![standard plugin workflow](../../assets/images/cypressXrayDark.svg#only-dark)
  <figcaption>The plugin allows you to upload Cypress test results to Xray server or Xray cloud.</figcaption>
</figure>

## Setup

To upload your test results to Xray, make sure you have enabled the results upload in your configuration file:

```js
import { addXrayResultUpload, configureXrayPlugin } from "cypress-xray-plugin/plugin";

// ...
    async setupNodeEvents(on, config) {
        await configureXrayPlugin({
            xray: {
                uploadResults: true
            }
        });
        await addXrayResultUpload(on);
    }
// ...
```

Afterwards, simply run Cypress:

```sh
npx cypress run
```

!!! note
    Don't forget to provide your [authentication credentials](../configuration/authentication.md).

## How it works

When uploading results, Xray will create a new test issue for each executed test unless any of the following apply:

* there already exists a test issue with the *exact* name as the executed test
* you have [provided a test issue key](targetingExistingIssues.md) to tell Xray which issue to reuse

Xray will also create a new test execution issue, unless you tell Xray to [reuse a specific test execution issue](../configuration/jira.md#testexecutionissuekey).

??? abstract "Xray Documentation"
    You can find more information on the mechanisms and constraints regarding imports of test execution results [here](https://docs.getxray.app/display/XRAY/Import+Execution+Results#ImportExecutionResults-XrayJSONformat) for Xray server and [here](https://docs.getxray.app/display/XRAYCLOUD/Using+Xray+JSON+format+to+import+execution+results#UsingXrayJSONformattoimportexecutionresults-XrayJSONformat) for Xray cloud .


???+ example

    The following example consists of three test cases for [https://example.org](https://example.org):

    1. :white_check_mark: The first one tries to find a `#!html <h1>` element.
    2. :white_check_mark: The second one asserts that the page contains two `#!html <p>` elements.
    3. :x: The third one tries to find a `#!html <span>` element, which does not exist on the page.

    When uploading the results, Xray will create three test case issues corresponding to the test cases that have been executed.
    Additionally, a test execution issue will be created containing the three executed test issues.
    Since Cypress automatically takes screenshots on failure, the execution will also contain the screenshot as evidence for the failed test case.

    === "demo.spec.cy.js"

        ```js
        describe("the upload demo", () => {

            beforeEach(() => {
                cy.visit("https://example.org");
            });

            it("should find a title element", () => {
                cy.get("h1").should("exist");
            });

            it("should find two paragraph elements", () => {
                cy.get("p").should("have.length", 2);
            });

            it("should fail to find a span element", () => {
                cy.get("span").should("exist");
            });

        })
        ```

    === "cypress.config.js"

        ```js
        import { addXrayResultUpload, configureXrayPlugin } from "cypress-xray-plugin/plugin";

        // ...
            async setupNodeEvents(on, config) {
                await configureXrayPlugin({
                    jira: {
                        projectKey: "CYP"
                    },
                    xray: {
                        uploadResults: true
                    }
                });
                await addXrayResultUpload(on);
            }
        // ...
        ```

    === "Video"

        <video preload="none" poster="../../../assets/videos/guides_results_upload_00.jpg" controls muted>
            <source src="../../../assets/videos/guides_results_upload_00.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
