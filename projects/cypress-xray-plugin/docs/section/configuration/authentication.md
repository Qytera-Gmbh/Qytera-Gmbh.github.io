# Authentication

To use this plugin, you need to authenticate to your Xray instance and &mdash; depending on the options you configured &mdash; your Jira instance as well.
You *must* do this by setting up specific environment variables, e.g. a client ID and a client secret when using a cloud based Xray instance.

To avoid adding your secrets to system environment variables, simply pass them to Cypress as a comma-separated list in the command line:

```sh
npx cypress run --env XRAY_CLIENT_ID="ABCDEF",XRAY_CLIENT_SECRET="XYZ"
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

### Xray server

For setting up Xray server authentication, see [Jira server authentication](#jira-server).

!!! tip
    Don't forget to provide the [Jira URL](jira.md#serverurl).

## Jira

Some options require a direct connection to the underlying Jira instance (such as [`attachVideo`](jira.md#attachvideo)).
These are options for things related to *Jira*, which aren't introduced by Xray add-ons, for example generic issue attachments.

If you do not use any such option you can skip setting up Jira credentials.

!!! tip
    Don't worry about unknowingly enabling options that require the Jira connection if you've skipped providing Jira credentials so far.
    The plugin will tell you in great detail which options have caused the plugin to look for the missing Jira credentials.

!!! note
    You must provide a [Jira URL](jira.md#serverurl) in the plugin's options if you want to connect to the Jira instance directly.

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