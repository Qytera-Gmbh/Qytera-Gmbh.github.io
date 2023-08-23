# Authentication

To use this plugin, you need to authenticate to both your Xray instance and your Jira instance.
You *must* do this by setting up specific environment variables, e.g. a client ID and a client secret when using a cloud based Xray instance.

To avoid adding your secrets to system environment variables, simply pass them to Cypress as a comma-separated list in the command line:

```sh
npx cypress run --env XRAY_CLIENT_ID="ABCDEF",XRAY_CLIENT_SECRET="XYZ"
```

!!! tip
    Have a look at this graph to quickly set up Xray and Jira authentication.
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

### Xray server

For setting up Xray server authentication, see [Jira server authentication](#jira-server).

!!! note
    Xray server does not require any additional credentials.

## Jira

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