# Authentication

To use this plugin, you need to authenticate to your Xray instance and &mdash; depending on the options you configured &mdash; your Jira instance as well.
You *must* do this by setting up specific environment variables, e.g. a client ID and a client secret when using a cloud based Xray instance.

To avoid adding your secrets to system environment variables, simply pass them to Cypress as a comma-separated list in the command line:

```sh
npx cypress run --env XRAY_CLIENT_ID="ABCDEF",XRAY_CLIENT_SECRET="XYZ"
```

!!! tip
    Have a look at this graph to quickly set up **_both_** Xray and Jira authentication.
    Note that Xray server does **_not_** require dedicated credentials in addition to the Jira credentials, effectively setting up both at the same time.
    ```mermaid
    graph TD
        A{Xray<br/>instance};
        B("XRAY_CLIENT_ID=<i>id</i><br>XRAY_CLIENT_SECRET=<i>secret</i><br><hr>JIRA_USERNAME=<i>user@company.com</i><br>JIRA_API_TOKEN=<i>token</i>");
        C{Jira<br/>auth};
        A --->|Cloud| B;
        A --->|Server| C;
        C --->|PAT| D;
        C --->|Basic| E;
        D("JIRA_API_TOKEN=<i>token</i>");
        E("JIRA_USERNAME=<i>user</i><br>JIRA_PASSWORD=<i>password</i>");
        classDef code-node font-family:monospace,text-align:left;
        class B,D,E code-node;
    ```

## Xray

Depending on the provided combinations of environment variables, the plugin will automatically know which Xray API type to use.

??? info "Providing multiple combinations"

    When providing more than one valid combination of variables, evaluation precedence of the authentication methods is as follows:

    1. Cloud authentication
    2. PAT authentication
    3. Basic authentication

    This way, the cloud version will always be chosen in favor of the server version.

Below you will find all Xray authentication configurations that are currently supported and the environment variables you need to set to authenticate to their respective APIs.

### Xray cloud

For the cloud version of Xray, the plugin expects the following environment variables to be set:

- `XRAY_CLIENT_ID`
- `XRAY_CLIENT_SECRET`

!!! info
    Consult Xray's [official documentation](https://docs.getxray.app/display/XRAYCLOUD/Global+Settings%3A+API+Keys) on how to set up cloud API keys.

!!! example
    ```sh
    npx cypress run --env XRAY_CLIENT_ID="ABCDEF",XRAY_CLIENT_SECRET="XYZ"
    ```

In contrast to Xray server, a [Jira URL](jira.md#url) is not necessary by default.
This can change however, depending on your [configuration](#jira).

### Xray server

For setting up Xray server authentication, see [Jira server authentication](#jira-server).
Additionally, you must provide the [Jira URL](jira.md#url) of the Jira instance Xray is installed on.

## Jira

Some options require a direct connection to the underlying Jira instance, such as [`attachVideos`](jira.md#attachvideos).
These options address things which work natively in Jira and more importantly, independently of the features introduced by Xray add-ons.
Jira-native features are things like issue assignment or uploading issue attachments, whereas those introduced by Xray are features like test steps, test execution tracking or test evidence upload.

If you do not plan on using Jira-native features you can skip setting up Jira credentials.

!!! tip
    You don't have to learn by heart which options require the Jira connection.
    In case you unknowingly enable one of them in the future without having set up the Jira credentials, the plugin will tell you in great detail which options have caused it to look for the credentials (before running any tests).
    Should you encounter such an error message, you can then either turn off the corresponding options or provide the credentials.

As with Xray authentication, the plugin will automatically choose the authentication method depending on the provided environment variables.

??? info "Providing multiple combinations"

    When providing more than one valid combination of variables, evaluation precedence of the authentication methods is as follows:

    1. Basic authentication (Jira cloud)
    2. PAT authentication (Jira server)
    3. Basic authentication (Jira server)

Below you will find all currently supported Jira authentication configurations and the environment variables you need to set.

### Jira cloud

For the cloud version of Jira, the plugin expects the following environment variables to be set:

- `JIRA_USERNAME`
- `JIRA_API_TOKEN`

!!! info
    Consult Jira's [official documentation](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/) on how to set up cloud credentials.

!!! example
    ```sh
    npx cypress run --env JIRA_USERNAME="user@company.com",JIRA_API_TOKEN="XYZ"
    ```

### Jira server

Depending on your Jira version, you may either need to use Jira's *Personal Access Tokens* (PATs) to authenticate to Jira, or *Basic Authentication* using your Jira username and password.

!!! tip
    If you do not know which one you should be using, simply try PAT authentication first.
    If it works, great!
    You should stick to it, as PATs are a safer alternative to using usernames and passwords.

    If PAT-based authentication does not work or you cannot even create tokens, you will need to use basic authentication.

#### PAT authentication

For PAT authentication, the plugin expects the following environment variables to be set:

- `JIRA_API_TOKEN`

!!! info
    Consult Jira's [official documentation](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) on how to set up server API tokens.

!!! example
    ```sh
    npx cypress run --env JIRA_API_TOKEN="XYZ"
    ```

#### Basic authentication

For basic authentication, the plugin expects the following environment variables to be set:

- `JIRA_USERNAME`
- `JIRA_PASSWORD`

!!! example
    ```sh
    npx cypress run --env JIRA_USERNAME="Bob",JIRA_PASSWORD="superSecure!unhaxx0rable"
    ```