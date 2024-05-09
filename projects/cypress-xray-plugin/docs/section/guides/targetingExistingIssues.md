# Targeting existing issues

The plugin does not upload any results unless you reuse existing Jira issues to not clutter up your projects with unnecessary test case (or test execution) issues.
This section teaches you everything you need to know to target such existing issues.

<hr/>

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

<hr/>

## Reuse Cucumber issues

To link your Cucumber feature files to existing Jira issues, you need to tag both scenario (outlines) and backgrounds.
The tagging schemes follow the schemes Xray expects when importing feature files (see [here](https://docs.getxray.app/display/XRAY/Testing+using+Cypress+and+Cucumber+in+JavaScript) or [here](https://docs.getxray.app/display/XRAY/Importing+Cucumber+Tests+-+REST)).

### Test issues

In feature files, you must annotate scenarios (or scenario outlines) with a [tag](https://cucumber.io/docs/cucumber/api/?lang=java#tags) containing the corresponding test case issue key.
The tag's prefix must match the one configured in your Xray settings (see [here](../configuration/cucumber.md#prefixes)).

=== "Feature (prefix)"

    ```gherkin
    Feature: Example page redirection

    @MyTestPrefix:CYP-129
    Scenario: Redirect by clicking
        Given the example page
        When the link is clicked
        Then a redirect should occur
    ```

=== "cypress.config.js (prefix)"

    ```js
    await configureXrayPlugin(on, config, {
        cucumber: {
            prefixes: {
                test: "MyTestPrefix:"
            }
        },
    });
    ```

=== "Feature (no prefix)"

    ```gherkin
    Feature: Example page redirection

    @CYP-129
    Scenario: Redirect by clicking
        Given the example page
        When the link is clicked
        Then a redirect should occur
    ```

=== "cypress.config.js (no prefix)"

    ```js
    await configureXrayPlugin(on, config, {
        cucumber: {
            prefixes: {
                test: undefined // or omit it entirely
            }
        },
    });
    ```

### Precondition issues

In feature files, you must add a comment to a background's *very first step* containing the [tag](https://cucumber.io/docs/cucumber/api/?lang=java#tags) for a corresponding precondition issue key.
The tag's prefix must match the one configured in your Xray settings (see [here](../configuration/cucumber.md#prefixes)).

!!! note
    You can find more information about preconditions [here](https://docs.getxray.app/display/XRAY/Pre-Condition) for Xray server and [here](https://docs.getxray.app/display/XRAYCLOUD/Precondition) for Xray cloud.

=== "Feature (prefix)"

    ```gherkin
    Feature: Big feature on lovely page

    Background:
        #@MyPreconditionPrefix:CYP-332
        Given a browser
        Then the lovely page should open
    ```

=== "cypress.config.js (prefix)"

    ```js
    await configureXrayPlugin(on, config, {
        cucumber: {
            prefixes: {
                precondition: "MyPreconditionPrefix:"
            }
        },
    });
    ```

=== "Feature (no prefix)"

    ```gherkin
    Feature: Big feature on lovely page

    Background:
        #CYP-332
        Given a browser
        Then the lovely page should open
    ```

=== "cypress.config.js (no prefix)"

    ```js
    await configureXrayPlugin(on, config, {
        cucumber: {
            prefixes: {
                precondition: undefined // or omit it entirely
            }
        },
    });
    ```

<hr/>

## Reuse test execution issues

By default, the plugin will always create a new test execution issue whenever you upload test results.

You can prevent that from happening by specifying [the test execution issue key](../configuration/jira.md#testexecutionissuekey) you want to attach the results to.


