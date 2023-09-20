# Configuration

All Xray plugin options can be specified within the `#!json xray` property of the configuration JSON:

```json
"xray": {
	"service": "cloud",
	"url": {
		"xray": null,
		"jira": null
	}
},
```

<hr/>

## Mandatory settings

Some settings are mandatory if the plugin [is enabled](#enabled). Without the settings listed here, the plugin cannot function properly.

<hr/>

### `projectKey`

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

### `authentication`

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

#### `xray`

Xray server or Xray cloud credentials can be specified here.

!!! note
    Consult Xray's official documentation on how to set up:

    - :fontawesome-solid-cloud:{ title="Xray cloud" } [Cloud API keys](https://docs.getxray.app/display/XRAYCLOUD/Global+Settings%3A+API+Keys)
    - :fontawesome-solid-server:{ title="Xray server" } [Server tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)

<hr/>

##### `bearerToken` :fontawesome-solid-server:{ title="Xray server" }

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

##### `clientId` :fontawesome-solid-cloud:{ title="Xray cloud" }

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

##### `clientSecret` :fontawesome-solid-cloud:{ title="Xray cloud" }

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

#### `jira`

Additional Jira credentials might be necessary too, depending on how you configure the plugin.

<hr/>

##### `username` :fontawesome-solid-cloud:{ title="Xray cloud" }

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

##### `apiToken`

The API token granting access to the API of the Jira instance.
More information:

- :fontawesome-solid-cloud:{ title="Xray cloud" } [Documentation](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)
- :fontawesome-solid-server:{ title="Xray server" } [Documentation](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)

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

## Optional settings

The settings listed here are optional. They are still very useful in influencing the plugin's behaviour.

<hr/>

### `enabled`

Enables or disables the plugin entirely.
If set to `#!java false`, the plugin will be skipped completely and no results will be uploaded.

***Environment variable***
: `XRAY_ENABLED`

***Type***
: `boolean`
: Accepted strings (case-insensitive):

    - `"true"`
      `"1"`
      `"y"`

    - `"false"`
      `"0"`
      `"n"`

***Default***
: `#!java false`

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

### `resultsUpload`

These settings determine the plugin's behaviour regarding the results upload.

#### `assignee`

The Jira user to assign created test executions to.
The following values should be provided here:

- :fontawesome-solid-cloud:{ title="Xray cloud" } The account ID, usually of the form `61f8f589e688d6007068a792`.
  You can retrieve account IDs by exporting an issue as XML where the user is visible (reporter, assignee, ...). The XML element containing the account ID will then look something like this:
  ```xml
  <assignee accountid="61f8f589e688d6007068a792">John Miller</assignee>
  ```
- :fontawesome-solid-server:{ title="Xray server" } The username used for login, for example `miller_j`.
  You can retrieve usernames of other users by exporting an issue as XML where the user is visible (reporter, assignee, ...). The XML element will then look something like this:
  ```xml
  <assignee>miller_j</assignee>
  ```

!!! note
    If the configured assignee is `#!json null`, the test execution issues will not be assigned to anyone.

***Environment variable***
: `XRAY_RESULTS_UPLOAD_ASSIGNEE`

***Type***
: `string`

***Default***
: `#!java null`

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
        XRAY_RESULTS_UPLOAD_ASSIGNEE="61f8f589e688d6007068a792"
        ```




```json
"resultsUpload": {
	"customStatus": {
		"testExecutionIssue": {
			"passed": null,
			"failed": null
		},
		"test": {
			"passed": null,
			"failed": null,
			"pending": null,
			"skipped": null
		},
		"step": {
			"passed": null,
			"failed": null,
			"pending": null,
			"skipped": null,
			"undefined": null
		}
	},
	"environments": {
		"enabled": true,
		"os": true,
		"driver": true
	},
	"scenarioImageEvidence": true,
	"scenarioReportEvidence": true,
	"testPlanKey": null,
	"tests": {
		"info": {
			"keepJiraSummary": false,
			"steps": {
				"update": false,
				"merge": false
			}
		},
		"iterations": {
			"parameters": {
				"maxLength": {
					"name": null,
					"value": null
				}
			}
		}
	}
}
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