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
        await configureXrayPlugin(on, config, {
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
        await configureXrayPlugin(on, config, {
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
        When the plugin tries to access the test environments of issues, it will look for a field with name `Test Environments` by default.
        However, if Jira is set to French for example, it will return a field called `Environnements de Test` instead.

        In these situations, the plugin will display an error message containing the fields it received and their IDs. The ID of field `Environnements de Test` could then be copied to the [`testEnvironments` option](#testenvironments), fixing the error in future uploads:

        ```hl_lines="5"
        Failed to fetch Jira field ID for field with name: Test Environments
        Make sure the field actually exists and that your Jira language settings did not modify the field's name

        Available fields:
          name: Environnements de Test, id: customfield_11805
          name: Type de Test,           id: customfield_42069
          ...
        ```

- Your Jira project contains several fields with identical names

    !!! example
        Jira does not prohibit configuring multiple fields with the same name.
        There might be multiple fields called `Test Environments` for example, the default Xray one and another one for descriptions of defects reported by customers in user acceptance tests.

        In these situations, the plugin will display an error message containing the duplicates it detected and their properties, including the field IDs.
        The ID of Jira's test environments field could then again be copied to the [`testEnvironments` option](#testenvironments), fixing the error in future uploads:

        ```hl_lines="5"
        Failed to fetch Jira field ID for field with name: Test Environments
        There are multiple fields with this name

        Duplicates:
          id: customfield_11805, name: Test Environments, clauseNames: Test Environments
          id: customfield_12345, name: Test Environments, clauseNames: Test Environments (user acceptance)
          ...
        ```

!!! info
    Please consult the official documentation for more information about field IDs: [https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html)

<hr/>

#### ~~`description`~~

!!! warning "Deprecated since `7.2.0`"
    Will be removed in version `9.0.0`.
    Field `description` is a system field and will always have the ID `description`.
    It is no longer necessary to specify this field ID.

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
        await configureXrayPlugin(on, config, {
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

#### ~~`labels`~~

!!! warning "Deprecated since `7.2.0`"
    Will be removed in version `9.0.0`.
    Field `labels` is a system field and will always have the ID `labels`.
    It is no longer necessary to specify this field ID.

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
        await configureXrayPlugin(on, config, {
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

#### ~~`summary`~~

!!! warning "Deprecated since `7.2.0`"
    Will be removed in version `9.0.0`.
    Field `summary` is a system field and will always have the ID `summary`.
    It is no longer necessary to specify this field ID.

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
        await configureXrayPlugin(on, config, {
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
        await configureXrayPlugin(on, config, {
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

The Jira field ID of test plans in Xray test (execution) issues.

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
        await configureXrayPlugin(on, config, {
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

### `testExecutionIssue`

This option can be used to configure the test execution issue that the plugin will either create or modify with the run results.
The value must match the format of Jira's issue create/update payloads:

- [Jira Cloud](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)
- [Jira Server](https://developer.atlassian.com/server/jira/platform/rest/v10000/api-group-issue/#api-api-2-issue-post)

!!! note
    Because the data here has to go through Xray first, it is possible that some fields that Jira normally is happy to accept will be rejected by Xray.
    For example, the assignee may need to be set using the `name` property instead of account IDs (see [FAQ](../guides/faq.md#assigning-issues)).

You can do cool things here, including:

- [setting assignees](../guides/faq.md#assigning-issues)
- [setting custom fields](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html) (any fields actually)
- performing issue transitions
- ...

Almost everything you can do when you create Jira issues using the Jira API, you can also do here.
Make sure to check out the Jira API documentation for more information.

!!! tip

    The plugin also accepts a function that allows you to specify dynamic values based on the Cypress results.

    ```ts
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: ({ results }) => {
                if (results.totalFailed > 0) {
                    return {
                        fields: {
                            summary: "Failed test execution"
                        }
                    };
                }
                return {
                    fields: {
                        summary: "Perfect test execution"
                    }
                };
            }
        }
    });
    ```

!!! warning "Warning (affected versions: `7.2.0` &leq; version &lt; `9.0.0`)"
    While conflicting options such as [`testExecutionIssueDescription`](#testexecutionissuedescription) or [`testExecutionIssueSummary`](#testexecutionissuesummary) are still available, the fields and values defined in `testExecutionIssue` will take precedence over all options marked as deprecated.
    The following code configuration will create test executions with `Blue summary` and `Blue description` fields:

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                fields: {
                    summary: "Blue summary",
                    description: "Blue description"
                }
            },
            testExecutionIssueSummary: "Red summary", // ignored
            testExecutionIssueDescription: "Red description", // ignored
        },
    });
    ```

***Environment variable***
: `JIRA_TEST_EXECUTION_ISSUE`

***Type***
: [`object`](./types.md#object)

***Default***
: `#!js undefined`

!!! example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            jira: {
                testExecutionIssue: {
                    key: "PRJ-16",
                    fields: {
                        summary: "My execution issue summary",
                        description: "My execution issue description",
                        assignee: {
                            name: "cool.turtle@company.com"
                        },
                        customfield_12345: "Sprint 17"
                    }
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE='{"key":"PRJ-16","fields":{"summary":"My execution issue summary","description":"My execution issue description","assignee":{"name":"cool.turtle@company.com"},"customfield_12345":"Sprint 17"}}'
        ```

<hr/>

#### `fields`

These options modify the fields of the test execution issue that is either created or modified by each test run.

##### `description`

The description of test execution issues, which will be used both for new test execution issues as well as for updating existing issues (if one was provided through [`key`](#key)).

If the [`key`](#key) is configured but `description` is omitted, the existing test execution issue's description will not be modified.

***Environment variable***
: [`JIRA_TEST_EXECUTION_ISSUE`](#testexecutionissue)

***Type***
: `string`

***Default***
: ``#!js `Cypress version: ${version} Browser: ${name} (${version})` `` with values depending on Cypress and the chosen browser

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            jira: {
                testExecutionIssue: {
                    fields: {
                        description: "Release Test Results for v42.0"
                    }
                }
            }
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE='{"fields":{"description":"Release Test Results for v42.0"}}'
        ```
<hr/>

##### `issuetype`

The issue type of test executions.
By default, Xray calls them `Test Execution`, but it's possible that they have been renamed or translated in your Jira instance.

Use this option to specify the type of the test executions the plugin should create for each run.

***Environment variable***
: [`JIRA_TEST_EXECUTION_ISSUE`](#testexecutionissue)

***Type***
: `string`

***Default***
: `#!js 'Test Execution'`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            jira: {
                testExecutionIssue: {
                    fields: {
                        issuetype: {
                            id: "12345",
                            name: "Xray Test Execution",
                            // ... more properties to uniquely identify the issue type
                        }
                    }
                }
            }
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE='{"fields":{"issuetype":{"id":"12345","name":"Xray Test Execution"}}}'
        ```
<hr/>

##### `summary`

The summary of test execution issues, which will be used both for new test execution issues as well as for updating existing issues provided through [`key`](#key).

If the [`key`](#key) is configured but the `summary` is omitted, the existing test execution issue's summary will not be modified.

***Environment variable***
: [`JIRA_TEST_EXECUTION_ISSUE`](#testexecutionissue)

***Type***
: `string`

***Default***
: ``#!js `Execution Results [${t}]` `` with `t` being a Unix timestamp when Cypress started testing

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            jira: {
                testExecutionIssue: {
                    fields: {
                        summary: "my summary"
                    }
                }
            }
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE='{"fields":{"summary":"my summary"}}'
        ```
<hr/>

#### `key`

The key of the test execution issue to attach the run results to.
If omitted, Jira will always create a new test execution issue with each upload.

***Environment variable***
: [`JIRA_TEST_EXECUTION_ISSUE`](#testexecutionissue)

***Type***
: `string`

***Default***
: `#!js undefined`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            jira: {
                testExecutionIssue: {
                    key: "PRJ-123"
                }
            }
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_EXECUTION_ISSUE='{"key":"PRJ-123"}'
        ```
<hr/>

### ~~`testExecutionIssueDescription`~~

!!! warning "Deprecated since `7.2.0`"
    Will be removed in version `9.0.0`.
    To define a description, please use [`description`](#description_1) instead:

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                fields: {
                    description: "my description"
                }
            }
        },
    });
    ```

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
        await configureXrayPlugin(on, config, {
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

### ~~`testExecutionIssueKey`~~

!!! warning "Deprecated since `7.2.0`"
    Will be removed in version `9.0.0`.
    To reuse a test execution issue, please use [`key`](#key) instead:

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                key: "PRJ-123"
            }
        },
    });
    ```

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
        await configureXrayPlugin(on, config, {
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

### ~~`testExecutionIssueSummary`~~

!!! warning "Deprecated since `7.2.0`"
    Will be removed in version `9.0.0`.
    To define a summary, please use [`summary`](#summary_1) instead:

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                fields: {
                    summary: "my summary"
                }
            }
        },
    });
    ```

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
        await configureXrayPlugin(on, config, {
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

### ~~`testExecutionIssueType`~~

!!! warning "Deprecated since `7.2.0`"
    Will be removed in version `9.0.0`.
    To define a test execution issue type, please use [`issuetype`](#issuetype) instead:

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                fields: {
                    issuetype: {
                        // whatever is necessary to uniquely identify the issue type, e.g:
                        name: "Xray Test Execution",
                        id: "12345"
                    }
                }
            }
        },
    });
    ```

The issue type name of test executions.
By default, Xray calls them `Test Execution`, but it's possible that they have been renamed or translated in your Jira instance.

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
        await configureXrayPlugin(on, config, {
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
A test plan issue to attach the execution to.

***Environment variable***
: `JIRA_TEST_PLAN_ISSUE_KEY`

***Type***
: `string`

***Default***
: `#!js undefined`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
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

!!! warning "Deprecated since `7.4.0`"
    Will be removed in version `9.0.0`.
    Unused.

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
        await configureXrayPlugin(on, config, {
            jira: {
                testPlanIssueType: "Plan de test" // 🇫🇷
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env JIRA_TEST_PLAN_ISSUE_TYPE="Plan de test"
        ```
