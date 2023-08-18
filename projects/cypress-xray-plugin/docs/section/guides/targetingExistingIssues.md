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

<hr/>

## Reuse test execution issues

By default, the plugin will always create a new test execution issue whenever you upload test results.

You can prevent that from happening by specifying [the test execution issue key](../configuration/jira.md#testexecutionissuekey) you want to attach the results to.


