# Jira

In order to access Xray, some Jira configuration is mandatory.

## Mandatory settings

### `projectKey`
: The key of the Jira project.
    This option is mandatory since otherwise Xray would not know which project to work with.
    It is used in many places throughout the plugin, for example for [mapping Cypress tests to existing test issues in Xray](../guides/targetingExistingIssues.md).
: ***Environment variable***
    : `JIRA_PROJECT_KEY`
: ***Type***
    : `string`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                projectKey: "PRJ"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_PROJECT_KEY="PRJ"
        ```

### `url`

## Optional settings

### `attachVideos`
: Whether any videos Cypress captured during test execution should be attached to the test execution issue on results upload.
    !!! note
        This option only takes effect once [`uploadResults`](xray.md#uploadresults) is turned on.
        It is not possible to attach videos without uploading results.
: ***Environment variable***
    : `JIRA_ATTACH_VIDEOS`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            jira: {
                attachVideos: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_ATTACH_VIDEOS=true
        ```

### `testExecutionIssueDescription`
: The description of the test execution issue, which will be used both for new test execution issues as well as for updating existing issues (if one was provided through [`testExecutionIssueKey`](#testexecutionissuekey)).
    If the [`testExecutionIssueKey`](#testexecutionissuekey) is configured but the `testExecutionIssueDescription` is omitted, the existing test execution issue's description will not be modified.
: ***Environment variable***
    : `JIRA_TEST_EXECUTION_ISSUE_DESCRIPTION`
: ***Type***
    : `string`
: ***Default***
    : ``#!js `Cypress version: ${version} Browser: ${name} (${version})` `` with values depending on Cypress and the chosen browser
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                testExecutionIssueDescription: "This test run was approved by Mr Anderson."
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE_DESCRIPTION="This test run was approved by Mr Anderson."
        ```

### `testExecutionIssueKey`
: The key of the test execution issue to attach the run results to.
    If undefined, Jira will always create a new test execution issue with each upload.
    !!! note
        Must be prefixed with the [project key](#projectkey).
: ***Environment variable***
    : `JIRA_TEST_EXECUTION_ISSUE_KEY`
: ***Type***
    : `string`
: ***Default***
    : `#!js undefined`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                testExecutionIssueKey: "PRJ-123"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE_KEY="PRJ-123"
        ```

### `testExecutionIssueSummary`
: The summary of the test execution issue, which will be used both for new test execution issues as well as for updating existing issues (if one was provided through [`testExecutionIssueKey`](#testexecutionissuekey)).
    If the [`testExecutionIssueKey`](#testexecutionissuekey) is configured but the `testExecutionIssueSummary` is omitted, the existing test execution issue's summary will not be modified.
: ***Environment variable***
    : `JIRA_TEST_EXECUTION_ISSUE_SUMMARY`
: ***Type***
    : `string`
: ***Default***
    : ``#!js `Execution Results [${t}]` `` with `t` being a Unix timestamp when Cypress started testing
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                testExecutionIssueSummary: "Monday morning regression test"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE_SUMMARY="Monday morning regression test"
        ```

### `testExecutionIssueType`
: The issue type name of test executions. By default, Xray calls them `Test Execution`, but it's possible that they have been renamed or translated in your Jira instance.

    Use this option to specify the type of the test executions the plugin should create for each run (if needed, see [here](#testexecutionissuekey)).

: ***Environment variable***
    : `JIRA_TEST_EXECUTION_ISSUE_TYPE`
: ***Type***
    : `string`
: ***Default***
    : `#!js Test Execution`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                testExecutionIssueType: "Test Run"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE_TYPE="Test Run"
        ```


### `testPlanIssueKey`
: The summary of the test execution issue, which will be used both for new test execution issues as well as for updating existing issues (if one was provided through [`testExecutionIssueKey`](#testexecutionissuekey)).
: ***Environment variable***
    : `JIRA_TEST_EXECUTION_ISSUE_SUMMARY`
: ***Type***
    : `string`
: ***Default***
    : ``#!js `Execution Results [${t}]` `` with `t` being a Unix timestamp when Cypress started testing
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                testExecutionIssueSummary: "Monday morning regression test"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE_SUMMARY="Monday morning regression test"
        ```

### `testPlanIssueType`
: The issue type name of test plans. By default, Xray calls them `Test Plan`, but it's possible that they have been renamed or translated in your Jira instance.

    !!! note
        You can ignore this setting if:

        - you're using Xray cloud or
        - you're not running any Cucumber tests

        The plugin only accesses this option when:

        - you're using Xray server and
        - you're running Cucumber tests and
        - [a test plan issue key](#testplanissuekey) has been specified and it's trying to attach the test execution to it

: ***Environment variable***
    : `JIRA_TEST_PLAN_ISSUE_TYPE`
: ***Type***
    : `string`
: ***Default***
    : `#!js Test Plan`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                testPlanIssueType: "Plan de test" // 🇫🇷
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_PLAN_ISSUE_TYPE="Plan de test"
        ```
