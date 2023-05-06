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

### `attachVideo`
: Whether any videos Cypress captured during test execution should be attached to the test execution issue on results upload.
    !!! note
        If set to `#!js true`, requires the [Jira URL](#serverurl) and valid [Jira credentials](authentication.md#jira) to be set.
    !!! note
        This option only takes effect once [`uploadResults`](xray.md#uploadresults) is turned on.
        It is not possible to attach videos without uploading results.
: ***Environment variable***
    : `JIRA_ATTACH_VIDEO`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            jira: {
                attachVideo: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_ATTACH_VIDEO=true
        ```
