# Targeting existing issues

Usually, it is best to target and reuse existing Jira issues to not clutter up your projects with unnecessary test case (or test execution) issues.

!!! tip
    Reusing existing test case issues is highly recommended.
    It simplifies test case management *a lot*.

## Reuse test case issues

By default, Xray will always create a new test case issue whenever you execute a test and your project does not contain a test case issue with *the exact name* as your test case.

!!! info
    The exact name of test cases in Cypress is the concatenation of the names of `#!js it()` and `#!js describe()` functions.
    For example, the following test case is called `#!js "a suite has a test case"`:

    ```js
    describe("a suite", () => {
        it("has a test case", () => {
            // ...
        });
    });
    ```

This means, that whenever you change the titles of your test cases in Cypress in `#!js it()` or `#!js describe()` functions, Xray will create new test case issues for you on result upload.
This applies to the other direction, too.
If someone changes test case issue titles in Xray and the test cases in Cypress aren't adapted accordingly, you will end up with new test case issues.

To prevent that from happening, you can include test case issue keys in your test case titles.
Simply add the test case issue's key *anywhere* in the name of the `#!js it()` function:

```js
describe("a suite", () => {
    it("PRJ-123 has a test case", () => {
        // ...
    });
});
```

![retrieving test case issue numbers](../../assets/images/issueKeyLight.png#only-light){ style="float: right; margin-left: 1em; border: 1px solid var(--md-default-fg-color);" }
![retrieving test case issue numbers](../../assets/images/issueKeyDark.png#only-dark){ style="float: right; margin-left: 1em; border: 1px solid var(--md-default-fg-color);" }
The plugin parses all test case names and looks for sequences of the form `#!xml <projectKey>-<number>`, with `#!xml <projectKey>` being the [configured project key](../configuration/jira.md#projectkey) and `#!xml <number>` the issue number.

???+ example

    The following example builds upon the [upload results example](uploadTestResults.md#how-it-works), which created three issues `CYP-124`, `CYP-125` and `CYP-126`.

    For this execution, the test cases have been renamed both in Cypress and Xray (see the video).
    By including the test case issue keys in the titles, Xray will be able to match results to issues even if none of the test case names match anymore.

    === "demo.spec.cy.js"

        ```js
        describe("the upload demo", () => {

            beforeEach(() => {
                cy.visit("https://example.org");
            });

            it("CYP-124 should do something with the title", () => {
                cy.get("h1").should("exist");
            });

            it("CYP-125 should find two lovely paragraphs", () => {
                cy.get("p").should("have.length", 2);
            });

            it("CYP-126 should still be unable to find a delicious span element", () => {
                cy.get("span").should("exist");
            });

        })
        ```

    === "Video"

        <video preload="none" poster="../../../assets/videos/usage_targeting_issues_00.jpg" controls muted>
            <source src="../../../assets/videos/usage_targeting_issues_00.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

### Reuse Cucumber test issues

In feature files, you can annotate scenarios with a [tag](https://cucumber.io/docs/cucumber/api/?lang=java#tags) containing the corresponding test case issue key.
Without tags, the exact names of the test cases [will again be used](https://docs.getxray.app/display/XRAYCLOUD/Importing+Cucumber+Tests+-+REST), this time being the concatenation of the `#!gherkin Feature` and `#!gherkin Scenario` names.

In general, the plugin looks for scenario tags of the form:

- `#!xml @TestName:<projectKey>-<number>`
- `#!xml @<projectKey>-<number>`

!!! tip
    Just stick to this handy chart to decide which tagging scheme you should employ.
    ```mermaid
    graph LR
        classDef codeClass font-family:monospace;
        A{Xray<br/>instance?};
        B["@TestName:CYP-123"];
        C["@CYP-123"];
        A --->|Cloud| B;
        A --->|Server| C;
        class D codeClass;
        class E codeClass;
    ```

??? info "Additional information"
    The reason for the distinction is Xray cloud and Xray server expecting different tags during [feature file import](featureFileSynchronization.md#feature-file-upload) when mapping scenarios to existing test case issues.

    While *the plugin* itself does not care which one you use, you should probably stick to the one that better fits your Xray instance.
    Using the wrong one might not matter in terms of reusing Cucumber test issues, but it is going to matter when enabling [feature file importing](featureFileSynchronization.md#feature-file-upload) in the future, since then you would need to either:

    - Change all existing tags to the right ones, i.e. for Xray cloud:

        ```gherkin
        @CYP-123
        Scenario: A scenario
        ```
        <p style="text-align: center;">&darr;</p>
        ```gherkin
        @TestName:CYP-123
        Scenario: A scenario
        ```

    - Add "the right ones" to your scenarios, i.e. for Xray cloud:

        ```gherkin
        @CYP-123
        Scenario: A scenario
        ```
        <p style="text-align: center;">&darr;</p>
        ```gherkin
        @CYP-123 @TestName:CYP-123
        Scenario: A scenario
        ```

        This has the additional disadvantage that Xray will add the wrong one (`#!xml @CYP-123`) as a label to your test case issue during feature file import.

???+ example

    In the following scenario, the link on [https://example.org](https://example.org) will be clicked and its redirection will be verified.

    === "demo.spec.feature"

        ```gherkin
        Feature: Example page redirection

            @TestName:CYP-129
            Scenario: Redirect by clicking
                Given the example page
                When the link is clicked
                Then a redirect should occur
        ```

    === "demo.spec.js"

        ```js
        import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

        Given("the example page", function () {
            cy.visit("https://example.org");
        });

        When("the link is clicked", function () {
            // Intercept the click, since it unfortunately redirects to a http:// location
            // and causes Cypress to abort the execution.
            cy.intercept("GET", "https://www.iana.org/domains/example", (request) => {
                request.reply("link was clicked");
            }).as("redirect");
            cy.get("a").click();
        });

        Then("a redirect should occur", function () {
            cy.wait("@redirect").then((request) => {
                expect(request.response.body).to.eq("link was clicked");
            });
        });
        ```

    === "cypress.config.js"

        See [Cucumber installation](../setup/installation.md#cucumber-support).

        ```js
        import { addCucumberPreprocessorPlugin } from "@badeball/cypress-cucumber-preprocessor";
        import createEsbuildPlugin from "@badeball/cypress-cucumber-preprocessor/esbuild";
        import * as createBundler from "@bahmutov/cypress-esbuild-preprocessor";
        import { addXrayResultUpload, configureXrayPlugin, syncFeatureFile } from "cypress-xray-plugin/plugin";

        // ...
            async setupNodeEvents(on, config) {
                await configureXrayPlugin({
                    jira: {
                        projectKey: "CYP"
                    }
                });
                await addCucumberPreprocessorPlugin(on, config, {
                    omitBeforeRunHandler: true,
                    omitAfterRunHandler: true,
                    omitBeforeSpecHandler: true,
                    omitAfterSpecHandler: true,
                    omitAfterScreenshotHandler: true,
                });
                await addXrayResultUpload(on);
                on("file:preprocessor", async (file) => {
                    await syncFeatureFile(file);
                    const cucumberPlugin = createBundler({
                        plugins: [createEsbuildPlugin(config)],
                    });
                    return cucumberPlugin(file);
                });
                return config;
            }
        // ...
        ```

    === "Video"

        <video preload="none" poster="../../../assets/videos/usage_targeting_issues_02.jpg" controls muted>
            <source src="../../../assets/videos/usage_targeting_issues_02.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>


## Reuse test execution issues

By default, Xray will always create a new test execution issue whenever you upload test results.

You can prevent that from happening by specifying [the test execution issue key](../configuration/jira.md#testexecutionissuekey) you want to attach the results to.

???+ example

    The following example builds upon the [upload results example](uploadTestResults.md#how-it-works), which created test execution issue `CYP-123`.

    By providing the test execution issue key, Xray won't create a new execution issue for this upload.
    To highlight the issue being reused, let's also add a new test case that looks for an `#!xml <a>` element.

    === "demo.spec.cy.js"

        ```js hl_lines="19-21"
        describe("the upload demo", () => {

            beforeEach(() => {
                cy.visit("https://example.org");
            });

            it("CYP-124 should find a title element", () => {
                cy.get("h1").should("exist");
            });

            it("CYP-125 should find two paragraph elements", () => {
                cy.get("p").should("have.length", 2);
            });

            it("CYP-126 should fail to find a span element", () => {
                cy.get("span").should("exist");
            });

            it("should find an anchor element", () => {
                cy.get("a").should("exist");
            });

        })
        ```

    === "cypress.config.js"

        ```js hl_lines="8"
        import { addXrayResultUpload, configureXrayPlugin } from "cypress-xray-plugin/plugin";

        // ...
            async setupNodeEvents(on, config) {
                await configureXrayPlugin({
                    jira: {
                        projectKey: "CYP",
                        testExecutionIssueKey: "CYP-123"
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

        <video preload="none" poster="../../../assets/videos/usage_targeting_issues_01.jpg" controls muted>
            <source src="../../../assets/videos/usage_targeting_issues_01.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

