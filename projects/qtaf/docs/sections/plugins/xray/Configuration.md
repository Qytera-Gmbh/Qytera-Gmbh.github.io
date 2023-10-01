# Configuration

All Xray plugin options can be specified within the `#!json xray` property of the configuration JSON.

!!! note
    The following icons describe whether the individual settings apply to Xray server or Xray cloud only:

    - :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } Setting applicable to/relevant for Xray cloud only
    - :fontawesome-solid-server:{ title="Xray server" .xray-icon } Setting applicable to/relevant for Xray server only

    All settings without such icons are applicable to both versions.

<hr/>

## `authentication`

In order to upload results to Xray, QTAF needs to authenticate to it.

!!! tip
    Have a look at this graph to quickly set up Xray and Jira authentication.
    ```mermaid
    graph LR
        A{Xray<br/>instance};
        B("xray.clientId=<i>id</i><br>xray.clientSecret=<i>secret</i><br><hr>jira.username=<i>user@company.com</i><br>jira.apiToken=<i>token</i>");
        A ---->|&nbsp cloud &nbsp| B;
        A ---->|&nbsp server &nbsp| D;
        D("xray.bearerToken=<i>token</i><br><hr>jira.apiToken=<i>token</i>");
        classDef code-node text-align:left;
        class B,D,E code-node;
    ```

    Please note that basic authentication for Xray server and Jira server is not supported by QTAF.

<hr/>

### `xray`

Xray server or Xray cloud credentials can be specified here.

!!! note
    Consult Xray's official documentation on how to set up:

    - :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } [Cloud API keys](https://docs.getxray.app/display/XRAYCLOUD/Global+Settings%3A+API+Keys)
    - :fontawesome-solid-server:{ title="Xray server" .xray-icon } [Server tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)

<hr/>

#### `bearerToken` :fontawesome-solid-server:{ title="Xray server" .xray-icon }

The Jira PAT of the user QTAF should use for interacting with Xray.

***Environment variable***
: `XRAY_AUTHENTICATION_XRAY_BEARERTOKEN`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "authentication": {
            "xray": {
              "bearerToken": "BigSecretToken"
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_AUTHENTICATION_XRAY_BEARERTOKEN="BigSecretToken"
        ```

<hr/>

#### `clientId` :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon }

The ID of the user all requests will be done in behalf of.

***Environment variable***
: `XRAY_AUTHENTICATION_XRAY_CLIENTID`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "authentication": {
            "xray": {
              "clientId": "12345ABCDEF"
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_AUTHENTICATION_XRAY_CLIENTID="12345ABCDEF"
        ```

<hr/>

#### `clientSecret` :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon }

The secret of the user all requests will be done in behalf of.

***Environment variable***
: `XRAY_AUTHENTICATION_XRAY_CLIENTSECRET`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "authentication": {
            "xray": {
              "clientSecret": "xyzSuperSecretxyz"
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_AUTHENTICATION_XRAY_CLIENTSECRET="xyzSuperSecretxyz"
        ```

<hr/>

### `jira`

Additional Jira credentials might be necessary too, depending on how you configure the plugin.

<hr/>

#### `username` :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon }

The username for Jira Cloud authentication.
It is usually the Email address of the user, as described [here](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).

***Environment variable***
: `XRAY_AUTHENTICATION_JIRA_USERNAME`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "authentication": {
            "jira": {
              "username": "fred@example.com"
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_AUTHENTICATION_JIRA_USERNAME="fred@example.com"
        ```

<hr/>

#### `apiToken`

The API token granting access to the API of the Jira instance.
More information:

- :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } [Xray documentation](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)
- :fontawesome-solid-server:{ title="Xray server" .xray-icon } [Xray documentation](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)

***Environment variable***
: `XRAY_AUTHENTICATION_JIRA_APITOKEN`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "authentication": {
            "jira": {
              "apiToken": "MyLittleJiraSecret"
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_AUTHENTICATION_JIRA_APITOKEN="MyLittleJiraSecret"
        ```

<hr/>

## `enabled`

Enables or disables the plugin entirely.
If set to `#!java false`, the plugin will be skipped completely and no results will be uploaded.

***Environment variable***
: `XRAY_ENABLED`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json false`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "enabled": "y"
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_ENABLED="y"
        ```

<hr/>

## `projectKey`

The Jira key of the project to upload results to.
It is used for identification of relevant test cases, meaning that only test cases with an `#!java @XrayTest` annotation containing the project key will be tracked and eventually uploaded to Xray.

***Environment variable***
: `XRAY_PROJECTKEY`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "projectKey": "PRJ"
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_PROJECTKEY="PRJ"
        ```

<hr/>

## `resultsUpload`

These settings determine the plugin's behaviour regarding the results upload.

### `assignee`

The Jira user to assign created test executions to.
The following values should be provided here:

- :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } The account ID, usually of the form `61f8f589e688d6007068a792`.
  You can retrieve account IDs by exporting an issue as XML where the user is visible (reporter, assignee, ...). The XML element containing the account ID will then look something like this:
  ```xml
  <assignee accountid="61f8f589e688d6007068a792">John Miller</assignee>
  ```
- :fontawesome-solid-server:{ title="Xray server" .xray-icon } The username used for login, for example `miller_j`.
  You can retrieve usernames of other users by exporting an issue as XML where the user is visible (reporter, assignee, ...). The XML element will then look something like this:
  ```xml
  <assignee>miller_j</assignee>
  ```

!!! note
    If the configured assignee is `#!json null`, the test execution issues will not be assigned to anyone.

***Environment variable***
: `XRAY_RESULTSUPLOAD_ASSIGNEE`

***Type***
: `string`

***Default***
: `#!json null`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "assignee": "61f8f589e688d6007068a792"
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_ASSIGNEE="61f8f589e688d6007068a792"
        ```

<hr/>

### `customStatus`

These status settings map QTAF test (execution) statuses to corresponding Jira issue or Xray test and step statuses.

<hr/>

#### `step`

These settings allow mapping QTAF test _steps_ to Xray _step_ statuses.

!!! tip
    If you have custom step statuses set up in Xray, you should provide their names here.

<hr/>

##### `failed`

The Xray status of failed steps.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_FAILED`

***Type***
: `string`

***Default***
: :fontawesome-solid-server:{ title="Xray server" .xray-icon } `#!json "FAIL"`
: :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } `#!json "FAILED"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "step": {
                "failed": "ERROR"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_FAILED="ERROR"
        ```

<hr/>

##### `passed`

The Xray status of passed steps.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_PASSED`

***Type***
: `string`

***Default***
: :fontawesome-solid-server:{ title="Xray server" .xray-icon } `#!json "PASS"`
: :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } `#!json "PASSED"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "step": {
                "passed": "DONE"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_PASSED="DONE"
        ```

<hr/>

##### `pending`

The Xray status of pending steps.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_PENDING`

***Type***
: `string`

***Default***
: `#!json "EXECUTING"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "step": {
                "pending": "EXECUTING"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_PENDING="EXECUTING"
        ```

<hr/>

##### `skipped`

The Xray status of skipped steps.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_SKIPPED`

***Type***
: `string`

***Default***
: `#!json "TODO"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "step": {
                "skipped": "TODO"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_STEP_SKIPPED="TODO"
        ```

<hr/>

#### `test`

These settings allow mapping QTAF _test_ statuses to Xray statuses, for example when setting the status of a test inside a test test execution issue.

!!! tip
    If you have custom statuses set up in Xray, you should provide their names here.

<hr/>

##### `failed`

The Xray status of failed tests.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_FAILED`

***Type***
: `string`

***Default***
: :fontawesome-solid-server:{ title="Xray server" .xray-icon } `#!json "FAIL"`
: :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } `#!json "FAILED"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "test": {
                "failed": "ERROR"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_FAILED="ERROR"
        ```

<hr/>

##### `passed`

The Xray status of passed tests.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_PASSED`

***Type***
: `string`

***Default***
: :fontawesome-solid-server:{ title="Xray server" .xray-icon } `#!json "PASS"`
: :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } `#!json "PASSED"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "test": {
                "passed": "DONE"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_PASSED="DONE"
        ```

<hr/>

##### `pending`

The Xray status of pending tests.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_PENDING`

***Type***
: `string`

***Default***
: `#!json "EXECUTING"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "test": {
                "pending": "EXECUTING"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_PENDING="EXECUTING"
        ```

<hr/>

##### `skipped`

The Xray status of skipped tests.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_SKIPPED`

***Type***
: `string`

***Default***
: `#!json "TODO"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "test": {
                "skipped": "TODO"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_SKIPPED="TODO"
        ```

<hr/>

#### `testExecutionIssue`

The Jira status of test execution issues created during upload.

<hr/>

##### `failed`

The Jira status to transition test execution issues to if tests failed.
If the status is `#!json null`, the issue will have the default issue status of issues created in the project.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_EXECUTION_ISSUE_FAILED`

***Type***
: `string`

***Default***
: `#!json null`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "testExecutionIssue": {
                "failed": "Review"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_EXECUTION_ISSUE_FAILED="Review"
        ```

<hr/>

##### `passed`

The Jira status to transition test execution issues to if all tests passed.
If the status is `#!json null`, the issue will have the default issue status of issues created in the project.

***Environment variable***
: `XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_EXECUTION_ISSUE_PASSED`

***Type***
: `string`

***Default***
: `#!json null`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "customStatus": {
              "testExecutionIssue": {
                "passed": "Done"
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_CUSTOMSTATUS_TEST_EXECUTION_ISSUE_PASSED="Done"
        ```

<hr/>

### `environments`

QTAF can add test environments to created test execution issues.
The following settings can be used to control the way QTAF assigns test environments.

!!! info
    For more information about test environments, please see:

    - :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAYCLOUD/Working+with+Test+Environments)
    - :fontawesome-solid-server:{ title="Xray server" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAY/Working+with+Test+Environments)

<hr/>

#### `driver`

Toggles whether QTAF should add the name of the Selenium driver used to execute the tests as test environment.

***Environment variable***
: `XRAY_RESULTSUPLOAD_ENVIRONMENTS_DRIVER`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json true`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "environments": {
              "driver": false
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_ENVIRONMENTS_DRIVER="false"
        ```

<hr/>

#### `enabled`

Toggles whether QTAF should include test environments during test execution issue creation.
Setting this option to `false` will result in no test environments being added to the test execution issue.

***Environment variable***
: `XRAY_RESULTSUPLOAD_ENVIRONMENTS_ENABLED`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json true`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "environments": {
              "enabled": false
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_ENVIRONMENTS_ENABLED="n"
        ```

<hr/>

#### `os`

Toggles whether QTAF should add the name of the operating system the tests were executed on as test environment.

***Environment variable***
: `XRAY_RESULTSUPLOAD_ENVIRONMENTS_OS`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json true`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "environments": {
              "os": false
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_ENVIRONMENTS_OS="0"
        ```

<hr/>

### `scenarioImageEvidence`

Toggles whether QTAF should attach screenshot evidence to the test execution issue.
Setting this to `true` will result in QTAF adding all screenshots it takes during a test to the test case inside the test execution.

!!! info
    For more information about test execution evidence, please see:

    - :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAYCLOUD/Execute+Tests#ExecuteTests-Evidence)
    - :fontawesome-solid-server:{ title="Xray server" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAY/Execute+Tests#ExecuteTests-Evidence)

***Environment variable***
: `XRAY_RESULTSUPLOAD_SCENARIOIMAGEEVIDENCE`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json false`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "scenarioImageEvidence": true
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_SCENARIOIMAGEEVIDENCE="y"
        ```

<hr/>

### `scenarioReportEvidence`

Toggles whether QTAF should attach the HTML report it generates as evidence to the test execution issue.

!!! info
    For more information about test execution evidence, please see:

    - :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAYCLOUD/Execute+Tests#ExecuteTests-Evidence)
    - :fontawesome-solid-server:{ title="Xray server" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAY/Execute+Tests#ExecuteTests-Evidence)

***Environment variable***
: `XRAY_RESULTSUPLOAD_SCENARIOREPORTEVIDENCE`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json false`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "scenarioReportEvidence": true
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_SCENARIOREPORTEVIDENCE="1"
        ```

<hr/>

### `testPlanKey`

Test executions can automatically be assigned to an existing test plan.
QTAF uses this setting to retrieve such configured test plans.
When set to `#!json null`, QTAF will not add created test execution issues to any test plan.

***Environment variable***
: `XRAY_RESULTSUPLOAD_TESTPLANKEY`

***Type***
: `string`

***Default***
: `#!json null`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "testPlanKey": "PRJ-123"
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_TESTPLANKEY="PRJ-123"
        ```

<hr/>

### `tests`

The settings below allow configuring the way test cases themselves are updated during test results upload.

#### `iterations`

When uploading data-driven test results, QTAF will automatically use Xray's iterations in test executions.
Settings related to these iterations are listed here.

##### `parameters`

Xray can add parameters to data-driven test iteration results, which provide information about the names and values of the concrete test case parameters.
Parameter settings are listed here.

!!! info
    For more information about iteration parameters, please see:

    - :fontawesome-solid-cloud:{ title="Xray cloud" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAYCLOUD/Execute+Tests#ExecuteTests-Iterations)
    - :fontawesome-solid-server:{ title="Xray server" .xray-icon } [Xray documentation](https://docs.getxray.app/display/XRAY/Execute+Tests#ExecuteTests-Iterations)



###### `maxLength`

Xray enforces a hard limit on the length of both parameter names and values, which is different for Xray cloud and Xray server and from version to version.
It is recommended to provide reasonable values like `#!json 30` here for both `#!json name` and `#!json value` to keep things readable and to prevent Xray from rejecting test result uploads altogether.
QTAF will automatically truncate parameter names and values of the iterations to the numbers provided here.

!!! warning
    If set to `#!json null`, QTAF will not truncate parameter names or values whatsoever, possibly resulting in failed result uploads.
    Make sure to manually identify the limit your Xray instance is enforcing through the UI!

***Environment variables***
: `XRAY_RESULTSUPLOAD_TESTS_ITERATIONS_PARAMETERS_MAX_LENGTH_NAME`
: `XRAY_RESULTSUPLOAD_TESTS_ITERATIONS_PARAMETERS_MAX_LENGTH_VALUE`

***Type***
: `number`

***Default***
: `#!json null`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "tests": {
              "iterations": {
                "parameters": {
                  "maxLength": {
                    "name": 42,
                    "value": 50
                  }
                }
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_TESTS_ITERATIONS_PARAMETERS_MAX_LENGTH_NAME=42
        XRAY_RESULTSUPLOAD_TESTS_ITERATIONS_PARAMETERS_MAX_LENGTH_VALUE=50
        ```

<hr/>

#### `info`

Settings regarding general test case information.

##### `keepJiraSummary`

When uploading test results, QTAF can automatically rename existing test issues to the test case's name defined within QTAF.
This setting toggles whether this is allowed to happen or whether the test case's existing summaries should be kept.

***Environment variable***
: `XRAY_RESULTSUPLOAD_TESTS_INFO_KEEPJIRASUMMARY`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json false`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "tests": {
              "info": {
                "keepJiraSummary": true
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_TESTS_INFO_KEEPJIRASUMMARY="y"
        ```

<hr/>

##### `steps`

When uploading test results, QTAF can automatically update or change the steps defined within existing test issues with the steps it executed itself.
These settings control how and whether this is allowed to happen.

###### `update`

Toggles whether QTAF is allowed to update existing test issue steps in Xray.
Setting this to `#!json true` will result in QTAF replacing _all_ existing steps with the ones it executed itself.
To not modify any existing steps, set this to `#!json false`.

***Environment variable***
: `XRAY_RESULTSUPLOAD_TESTS_STEPS_UPDATE`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json false`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "tests": {
              "info": {
                "steps": {
                  "update": true
                }
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_TESTS_STEPS_UPDATE="true"
        ```

<hr/>

###### `merge`

Toggles whether QTAF should merge all steps it executed into a single step before updating test case steps in Xray.
The merged step will then contain _a list of steps_, possibly for all test case iterations if a test was executed more than once:

```md
# Step 1 (the only remaining step)
  == ITERATION 1 username="denise" password="xyz12" address="main avenue"
    1. Click register
    2. Enter username
    3. Enter password
    4. Enter address
    5. Click submit
  == ITERATION 2 username="george" password="12345" address=""
    1. Click register
    2. Enter username
    3. Enter password
    4. Click submit
```
In situations like above where individual test runs might not _always_ consist of exactly the same steps (for example when skipping empty form fields), Xray would not be able to properly display the test results inside the test execution issue without the merged steps:

<table>
  <thead>
    <tr>
      <th>Steps defined in test case issue</th>
      <th>Steps reported in test execution (iteration 1)</th>
      <th>Steps reported in test execution (iteration 2)</th>
      <th>Problem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ol>
          <li>Click register</li>
          <li>Enter username</li>
          <li>Enter password</li>
          <li>Click submit</li>
        </ol>
      </td>
      <td>
        <ol>
          <li style="color:green">Click register</li>
          <li style="color:green">Enter username</li>
          <li style="color:green">Enter password</li>
          <li style="color:green">Enter address</li>
        </ol>
      </td>
      <td>
        <ol>
          <li style="color:green">Click register</li>
          <li style="color:green">Enter username</li>
          <li style="color:green">Enter password</li>
          <li style="color:green">Click submit</li>
        </ol>
      </td>
      <td>Fifth step truncated in iteration 1 by Xray.</td>
    </tr>
    <tr>
      <td>
        <ol>
          <li>Click register</li>
          <li>Enter username</li>
          <li>Enter password</li>
          <li>Enter address</li>
          <li>Click submit</li>
        </ol>
      </td>
      <td>
        <ol>
          <li style="color:green">Click register</li>
          <li style="color:green">Enter username</li>
          <li style="color:green">Enter password</li>
          <li style="color:green">Enter address</li>
          <li style="color:green">Click submit</li>
        </ol>
      </td>
      <td>
        <ol>
          <li style="color:green">Click register</li>
          <li style="color:green">Enter username</li>
          <li style="color:green">Enter password</li>
          <li style="color:green">Enter address</li>
          <li style="color:gray">Click submit</li>
        </ol>
      </td>
      <td>Mismatched steps in interation 2: the address was never actually entered and Xray marked the fifth step as TODO because only four steps were actually executed in iteration 2.</td>
    </tr>
  </tbody>
</table>

Merging the iterations' steps can therefore help for data-driven testing.

***Environment variable***
: `XRAY_RESULTSUPLOAD_TESTS_STEPS_MERGE`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `#!json "true"`
      `#!json "1"`
      `#!json "y"`

    - `#!json "false"`
      `#!json "0"`
      `#!json "n"`

***Default***
: `#!json false`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "resultsUpload": {
            "tests": {
              "info": {
                "steps": {
                  "merge": true
                }
              }
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_RESULTSUPLOAD_TESTS_STEPS_MERGE="true"
        ```

<hr/>

## `service`

Defines whether the targeted Xray instance is an Xray cloud or Xray server instance.
QTAF requires this setting because Xray's APIs need to be addressed slightly differently.

***Environment variable***
: `XRAY_SERVICE`

***Type***
: `#!json "cloud"` or `#!json "server"`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "service": "server"
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_SERVICE="server"
        ```

<hr/>

## `url`

To properly connect to Xray, QTAF needs to know where the Xray and Jira instances can be found.

<hr/>

### `jira`

Defines the base URL of the Jira instance.
For Jira cloud, it is usually of the form `https://your-domain.atlassian.net` (without the `/jira` part, see [here](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#ad-hoc-api-calls/)).
For Jira server, you can have a look [here](https://confluence.atlassian.com/adminjiraserver/configuring-the-base-url-938847830.html) to determine your base URL.

***Environment variable***
: `XRAY_URL_JIRA`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "url": {
            "jira": "https://example.org/development/jira"
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_URL_JIRA="https://example.org/development/jira"
        ```

<hr/>

### `xray` :fontawesome-solid-server:{ title="Xray server" .xray-icon }

Defines the base URL of the Xray instance.

***Environment variable***
: `XRAY_URL_XRAY`

***Type***
: `string`

??? example
    === "QTAF JSON"

        ```json
        "xray": {
          "url": {
            "xray": "https://xray.jira.company.com"
          }
        }
        ```

    === "Environment variable"
        ```sh
        XRAY_URL_XRAY="https://xray.jira.company.com"
        ```

<hr/>

<div style="display: flex; flex-direction: row; justify-content: space-between">
  <a href="https://www.qytera.de" target="_blank">Developed with love by Qytera, Germany</a>
  <span>|</span>
  <a href="https://www.qytera.de/testautomatisierung-workshop" target="_blank">Support & Service</a>
  <span>|</span>
  <a href="https://github.com/Qytera-Gmbh/QTAF" target="_blank">QTAF Repository</a>
  <span>|</span>
  <a href="https://www.qytera.de/kontakt" target="_blank">Contact</a><br>
</div>
