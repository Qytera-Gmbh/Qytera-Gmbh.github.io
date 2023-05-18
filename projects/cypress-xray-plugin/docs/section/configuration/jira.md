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
        await configureXrayPlugin({
            jira: {
                projectKey: "PRJ"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_PROJECT_KEY="PRJ"
        ```

## Optional settings

### `attachVideos`
: Whether any videos Cypress captured during test execution should be attached to the test execution issue on results upload.
    !!! note
        If set to `#!js true`, requires the [Jira URL](#serverurl) and valid [Jira credentials](authentication.md#jira) to be set.
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

### `createTestIssues`
: Whether the plugin should create test issues for Cypress tests that have not been mapped to existing test issues (see [targeting existing issues](../guides/targetingExistingIssues.md)) when importing test results to Xray.
: ***Environment variable***
    : `JIRA_CREATE_TEST_ISSUES`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js true`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            jira: {
                createTestIssues: false
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_CREATE_TEST_ISSUES=false
        ```

### `testExecutionIssueDescription`
: The description of the test execution issue, which will be used both for new test execution issues as well as for updating existing issues (if one was provided through [`testExecutionIssueKey`](#testexecutionissuekey)).
: ***Environment variable***
    : `JIRA_TEST_EXECUTION_ISSUE_DESCRIPTION`
: ***Type***
    : `string`
: ***Default***
    : ``#!js `Cypress version: ${version} Browser: ${name} (${version})` `` with values depending on Cypress and the chosen browser
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
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
        await configureXrayPlugin({
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
: ***Environment variable***
    : `JIRA_TEST_EXECUTION_ISSUE_SUMMARY`
: ***Type***
    : `string`
: ***Default***
    : ``#!js `Execution Results [${t}]` `` with `t` being a Unix timestamp when Cypress started testing
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            jira: {
                testExecutionIssueSummary: "Monday morning regression test"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE_SUMMARY="Monday morning regression test"
        ```

### `testPlanIssueKey`
: A test plan issue key to attach the execution to.
    !!! note
        Must be prefixed with the [project key](#projectkey).
: ***Environment variable***
    : `JIRA_TEST_PLAN_ISSUE_KEY`
: ***Type***
    : `string`
: ***Default***
    : `#!js undefined`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            jira: {
                testPlanIssueKey: "PRJ-456"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_PLAN_ISSUE_KEY="PRJ-456"
        ```

### `url`
: Use this parameter to specify the base URL of your Jira instance.

    For Jira cloud, it is usually of the form `https://your-domain.atlassian.net` (without the `/jira` part, see [here](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#ad-hoc-api-calls/)).

    For Jira server, you can have a look [here](https://confluence.atlassian.com/adminjiraserver/configuring-the-base-url-938847830.html) to determine your base URL.
: ***Environment variable***
    : `JIRA_URL`
: ***Type***
    : `string`
: ***Default***
    : `#!js undefined`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            jira: {
                url: "https://example.org/development/jira"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_URL="https://example.org/development/jira"
        ```
