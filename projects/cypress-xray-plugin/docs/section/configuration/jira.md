# Jira

In order to access Xray, some Jira configuration is mandatory.

## Mandatory settings

### `projectKey`
: The key of the Jira project.
    This option is mandatory since otherwise Xray would not know which project to save the results to.
    It is used in many places throughout the plugin, for example for mapping Cypress tests to existing test issues in Xray (see [targeting existing test issues](../guides/targetingExistingIssues.md)).
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

### `serverUrl`
: When using a server-based Jira/Xray instance, use this parameter to specify the URL of your instance.
: ***Environment variable***
    : `JIRA_SERVER_URL`
: ***Type***
    : `string`
: ***Default***
    : `#!js undefined`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            jira: {
                serverUrl: "https://example.org/development/jira"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_SERVER_URL="https://example.org/development/jira"
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
