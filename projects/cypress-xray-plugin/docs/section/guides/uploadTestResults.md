# Upload test results

<figure markdown>
  ![standard plugin workflow](../../assets/images/cypressXrayLight.svg#only-light)
  ![standard plugin workflow](../../assets/images/cypressXrayDark.svg#only-dark)
  <figcaption>The plugin allows you to upload Cypress test results to Xray server or Xray cloud.</figcaption>
</figure>

<hr/>

## Setup

To upload your test results to Xray, make sure you have enabled the results upload in your configuration file:

```js
import { configureXrayPlugin } from "cypress-xray-plugin";

async setupNodeEvents(on, config) {
    await configureXrayPlugin(on, config, {
        xray: {
            uploadResults: true
        }
    });
}
```

Afterwards, simply run Cypress:

```sh
npx cypress run
```

!!! note
    Don't forget to provide your [authentication credentials](../configuration/authentication.md).

<hr/>

## How it works

The plugin will only upload results for tests you have linked to existing [test issues](targetingExistingIssues.md).

The plugin will also create a new test execution issue, unless you tell it to [reuse a specific test execution issue](../configuration/jira.md#testexecutionissuekey).

??? abstract "Xray Documentation"
    You can find more information on the mechanisms and constraints regarding imports of test execution results [here](https://docs.getxray.app/display/XRAY/Import+Execution+Results#ImportExecutionResults-XrayJSONformat) for Xray server and [here](https://docs.getxray.app/display/XRAYCLOUD/Using+Xray+JSON+format+to+import+execution+results#UsingXrayJSONformattoimportexecutionresults-XrayJSONformat) for Xray cloud.


???+ example

    The following example consists of three test cases for [https://example.org](https://example.org):

    1. :white_check_mark: The first one tries to find an `#!html <h1>` element with text `Example Domain`.
    2. :white_check_mark: The second one asserts that the page contains an `#!html <a>` element with a `href` attribute.
    3. :x: The third one tries to find an `#!html <img>` element, which does not exist on the page.

    When uploading the results, the plugin will create a test execution issue containing the three executed test issues.
    Since Cypress automatically takes screenshots on failure, the execution will also contain the screenshot as evidence for the failed test case.

    A corresponding video can be seen [here](../../index.md).

    === "demo.spec.cy.js"

        ```js
        describe("the upload demo", () => {

            beforeEach(() => {
                cy.visit("https://example.org");
            });

            it("CYP-410 Contains a title", () => {
                cy.get("h1").should("contain.text", "Example Domain");
            });

            it("CYP-411 Contains a link", () => {
                cy.get("a").should("have.attr", "href");
            });

            it("CYP-412 Fails a test", () => {
                cy.get("img").should("be.visible");
            });

        })
        ```

    === "cypress.config.js"

        ```js
        import { configureXrayPlugin } from "cypress-xray-plugin";

        async setupNodeEvents(on, config) {
            await configureXrayPlugin(on, config, {
                jira: {
                    projectKey: "CYP",
                    url: "https://atlassian.com"
                },
                xray: {
                    uploadResults: true
                }
            });
        }
        ```