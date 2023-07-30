# Targeting existing issues

The plugin does not upload any results unless you reuse existing Jira issues to not clutter up your projects with unnecessary test case (or test execution) issues.
This section teaches you everything you need to know to target such existing issues.

## Reuse Cypress issues

To link Cypress tests to Jira issues, simply add the test case issue's key *anywhere* in the name of the *innermost* `#!js it()` function (or corresponding alternatives like `#!js specify()`):

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

        <video preload="none" poster="../../../assets/videos/guides_targeting_issues_00.jpg" controls muted>
            <source src="../../../assets/videos/guides_targeting_issues_00.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

## Reuse Cucumber issues

To link your Cucumber feature files to existing Jira issues, you need to tag both scenario (outlines) and backgrounds.
The tagging schemes follow the schemes Xray expects when importing feature files (see [here](https://docs.getxray.app/display/XRAY/Testing+using+Cypress+and+Cucumber+in+JavaScript) or [here](https://docs.getxray.app/display/XRAY/Importing+Cucumber+Tests+-+REST)).

### Test issues

In feature files, you must annotate scenarios (or scenario outlines) with a [tag](https://cucumber.io/docs/cucumber/api/?lang=java#tags) containing the corresponding test case issue key.

=== "Xray server"

    ```gherkin
    Feature: Shopping cart

    @CYP-129
    Scenario: Add socks
        Given Bob is logged in
        When three socks are added from the shop
        Then the shopping cart should contain three socks
    ```

=== "Xray cloud"

    ```gherkin
    Feature: Shopping cart

    @TestName:CYP-129
    Scenario: Add socks
        Given Bob is logged in
        When three socks are added from the shop
        Then the shopping cart should contain three socks
    ```

### Precondition issues

In feature files, you must add a comment to a background's *very first step* containing the [tag](https://cucumber.io/docs/cucumber/api/?lang=java#tags) for a corresponding precondition issue key.

!!! note
    You can find more information about preconditions [here](https://docs.getxray.app/display/XRAY/Pre-Condition) for Xray server and [here](https://docs.getxray.app/display/XRAYCLOUD/Precondition) for Xray cloud.

=== "Xray server"

    ```gherkin
    Feature: Big feature on lovely page

    Background:
        #@CYP-332
        Given a browser
        Then the lovely page should open
    ```

=== "Xray cloud"

    ```gherkin
    Feature: Big feature on lovely page

    Background:
        #@Precondition:CYP-332
        Given a browser
        Then the lovely page should open
    ```

## Reuse test execution issues

By default, the plugin will always create a new test execution issue whenever you upload test results.

You can prevent that from happening by specifying [the test execution issue key](../configuration/jira.md#testexecutionissuekey) you want to attach the results to.


