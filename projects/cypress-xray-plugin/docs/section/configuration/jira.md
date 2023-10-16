# Jira

In order to access Xray, some Jira configuration is mandatory.

## Mandatory settings

### `projectKey`

The key of the Jira project.
This option is mandatory since otherwise Xray would not know which project to work with.
It is used in many places throughout the plugin, for example for [mapping Cypress tests to existing test issues in Xray](../guides/targetingExistingIssues.md).

***Environment variable***
: `JIRA_PROJECT_KEY`

***Type***
: `string`

??? example
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

<hr/>

### `url`

Use this parameter to specify the base URL of your Jira instance.

For Jira cloud, it is usually of the form `https://your-domain.atlassian.net` (without the `/jira` part, see [here](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#ad-hoc-api-calls/)).

For Jira server, you can have a look [here](https://confluence.atlassian.com/adminjiraserver/configuring-the-base-url-938847830.html) to determine your base URL.

***Environment variable***
: `JIRA_URL`

***Type***
: `string`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                url: "https://example.org/development/jira"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_URL="https://example.org/development/jira"
        ```

## Optional settings

### `attachVideos`

Whether any videos Cypress captured during test execution should be attached to the test execution issue on results upload.
!!! note
    This option only takes effect once [`uploadResults`](xray.md#uploadresults) is turned on.
    It is not possible to attach videos without uploading results.

***Environment variable***
: `JIRA_ATTACH_VIDEOS`

***Type***
: [`boolean`](types.md#boolean)

***Default***
: `#!js false`

??? example
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

<hr/>

### `fields`

Jira Field IDs to make all fields required during the upload process uniquely identifiable.
By default, the plugin accesses field information using the fields' names (ignoring case). Therefore, providing Jira field IDs can make sense in the following scenarios:

- Your Jira language setting is a language other than English

    !!! example
        When the plugin tries to access the summary of some issues, it will look for a field with name `summary` by default.
        However, if Jira is set to French for example, it will return a field called `résumé` instead.

        In these situations, the plugin will display an error message containing the fields it received and their IDs. The ID of field `Résumé` could then be copied to the [`summary` option](#summary), fixing the error in future uploads:

        ```hl_lines="5"
        Failed to fetch Jira field ID for field with name: summary
        Make sure the field actually exists and that your Jira language settings did not modify the field's name

        Available fields:
          name: Résumé, id: summary
          name: Type de Test, id: customfield_42069
          ...
        ```

- Your Jira project contains several fields with identical names

    !!! example
        Jira does not prohibit configuring multiple fields with the same name.
        There might be multiple fields called `summary` for example, the default Jira one and another one for descriptions of defects reported by customers.

        In these situations, the plugin will display an error message containing the duplicates it detected and their properties, including the field IDs.
        The ID of Jira's summary field could then again be copied to the [`summary` option](#summary), fixing the error in future uploads:

        ```hl_lines="5"
        Failed to fetch Jira field ID for field with name: summary
        There are multiple fields with this name

        Duplicates:
          id: summary,           name: summary, clauseNames: summary
          id: customfield_12345, name: Summary, clauseNames: summary (defect)
          ...
        ```

!!! info
    Please consult the official documentation for more information about field IDs: [https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html)

<hr/>

#### `description`
The description field ID of Jira issues.

***Environment variable***
: `JIRA_FIELDS_DESCRIPTION`

***Type***
: `string`

***Default***
: `#!js "description"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                fields: {
                    description: "Beschreibung" // German
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_FIELDS_DESCRIPTION=Beschreibung
        ```

<hr/>

#### `labels`
The labels field ID of Jira issues.

***Environment variable***
: `JIRA_FIELDS_LABELS`

***Type***
: `string`

***Default***
: `#!js "labels"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                fields: {
                    labels: "Stichworte" // German
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_FIELDS_LABELS=Stichworte
        ```

<hr/>

#### `summary`
The summary field ID of Jira issues.

***Environment variable***
: `JIRA_FIELDS_SUMMARY`

***Type***
: `string`

***Default***
: `#!js "summary"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                fields: {
                    summary: "Beschreibung" // German
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_FIELDS_SUMMARY=Beschreibung
        ```

<hr/>

#### `testEnvironments`
The Xray test environments field ID (i.e. the test environments associated with test execution issues).

!!! note
    This option is required for server instances only.
    Xray cloud provides ways to retrieve test environment field information independently of Jira.

***Environment variable***
: `JIRA_FIELDS_TEST_ENVIRONMENTS`

***Type***
: `string`

***Default***
: `#!js "test environments"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                fields: {
                    testEnvironments: "customfield_12345"
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_FIELDS_TEST_ENVIRONMENTS=customfield_12345
        ```

<hr/>

#### `testPlan`
The test plan field ID of Xray test (execution) issues.

!!! note
    This option is necessary for server instances only.
    Xray cloud provides ways to retrieve test plan field information independently of Jira.

***Environment variable***
: `JIRA_FIELDS_TEST_PLAN`

***Type***
: `string`

***Default***
: `#!js "test plan"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                fields: {
                    testPlan: "customfield_12345"
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_FIELDS_TEST_PLAN=customfield_12345
        ```

<hr/>

#### `testType`
The test type field ID of Xray test issues.

!!! note
    This option is necessary for server instances only.
    Xray cloud provides ways to retrieve test type field information independently of Jira.

***Environment variable***
: `JIRA_FIELDS_TEST_TYPE`

***Type***
: `string`

***Default***
: `#!js "test type"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                fields: {
                    testPlan: "customfield_42069"
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_FIELDS_TEST_TYPE=customfield_42069
        ```

<hr/>

### `testExecutionIssueDescription`
The description of test execution issues, which will be used both for new test execution issues as well as for updating existing issues (if one was provided through [`testExecutionIssueKey`](#testexecutionissuekey)).

If the [`testExecutionIssueKey`](#testexecutionissuekey) is configured but the `testExecutionIssueDescription` is omitted, the existing test execution issue's description will not be modified.

***Environment variable***
: `JIRA_TEST_EXECUTION_ISSUE_DESCRIPTION`

***Type***
: `string`

***Default***
: ``#!js `Cypress version: ${version} Browser: ${name} (${version})` `` with values depending on Cypress and the chosen browser

??? example
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

<hr/>

### `testExecutionIssueKey`
The key of the test execution issue to attach the run results to.
If omitted, Jira will always create a new test execution issue with each upload.
!!! note
    Must be prefixed with the [project key](#projectkey).

 ***Environment variable***
: `JIRA_TEST_EXECUTION_ISSUE_KEY`

***Type***
: `string`

***Default***
: `#!js undefined`

??? example
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

<hr/>

### `testExecutionIssueSummary`
The summary of test execution issues, which will be used both for new test execution issues as well as for updating existing issues (if one was provided through [`testExecutionIssueKey`](#testexecutionissuekey)).

If the [`testExecutionIssueKey`](#testexecutionissuekey) is configured but the `testExecutionIssueSummary` is omitted, the existing test execution issue's summary will not be modified.

***Environment variable***
: `JIRA_TEST_EXECUTION_ISSUE_SUMMARY`

***Type***
: `string`

***Default***
: ``#!js `Execution Results [${t}]` `` with `t` being a Unix timestamp when Cypress started testing

??? example
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

<hr/>

### `testExecutionIssueType`
The issue type name of test executions. By default, Xray calls them `Test Execution`, but it's possible that they have been renamed or translated in your Jira instance.

Use this option to specify the type of the test executions the plugin should create for each run (if needed, see [here](#testexecutionissuekey)).

***Environment variable***
: `JIRA_TEST_EXECUTION_ISSUE_TYPE`

***Type***
: `string`

***Default***
: `#!js Test Execution`

??? example
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

<hr/>

### `testPlanIssueKey`
A test plan issue key to attach the execution to.

!!! note
    Must be prefixed with the [project key](#projectkey).

***Environment variable***
: `JIRA_TEST_PLAN_ISSUE_KEY`

***Type***
: `string`

***Default***
: `#!js undefined`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            jira: {
                testPlanIssueKey: "PRJ-456"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_PLAN_ISSUE_KEY="PRJ-456"
        ```

<hr/>

### `testPlanIssueType`
The issue type name of test plans. By default, Xray calls them `Test Plan`, but it's possible that they have been renamed or translated in your Jira instance.

!!! note
    You can ignore this setting if:

    - you're using Xray cloud or
    - you're not running any Cucumber tests

    The plugin only accesses this option when:

    - you're using Xray server and
    - you're running Cucumber tests and
    - [a test plan issue key](#testplanissuekey) has been specified and it's trying to attach the test execution to it

***Environment variable***
: `JIRA_TEST_PLAN_ISSUE_TYPE`

***Type***
: `string`

***Default***
: `#!js Test Plan`

??? example
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
