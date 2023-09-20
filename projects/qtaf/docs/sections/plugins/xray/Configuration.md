# Configuration

All Xray plugin options can be specified within the `#!json xray` object of the configuration JSON.

## `authentication`

In order to upload results to Xray, QTAF needs to authenticate to it.

!!! tip
    Have a look at this graph to quickly set up Xray and Jira authentication.
    ```mermaid
    graph LR
        A{Xray<br/>instance};
        B("xray.clientId=<i>id</i><br>xray.clientSecret=<i>secret</i><br><hr>jira.username=<i>user@company.com</i><br>jira.apiToken=<i>token</i>");
        A --->|&nbsp cloud &nbsp| B;
        A --->|&nbsp server &nbsp| D;
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

    - :fontawesome-solid-cloud:{ title="Xray cloud" } [Cloud API keys](https://docs.getxray.app/display/XRAYCLOUD/Global+Settings%3A+API+Keys)
    - :fontawesome-solid-server:{ title="Xray server" } [Server tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)

<hr/>

#### `bearerToken` :fontawesome-solid-server:{ title="Xray server" }

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

#### `clientId` :fontawesome-solid-cloud:{ title="Xray cloud" }

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

#### `clientSecret` :fontawesome-solid-cloud:{ title="Xray cloud" }

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

#### `username` :fontawesome-solid-cloud:{ title="Xray cloud" }

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

<div style="display: flex; flex-direction: row; justify-content: space-between">
  <a href="https://www.qytera.de" target="_blank">Developed with love by Qytera, Germany</a>
  <span>|</span>
  <a href="https://www.qytera.de/testautomatisierung-workshop" target="_blank">Support & Service</a>
  <span>|</span>
  <a href="https://github.com/Qytera-Gmbh/QTAF" target="_blank">QTAF Repository</a>
  <span>|</span>
  <a href="https://www.qytera.de/kontakt" target="_blank">Contact</a><br>
</div>
