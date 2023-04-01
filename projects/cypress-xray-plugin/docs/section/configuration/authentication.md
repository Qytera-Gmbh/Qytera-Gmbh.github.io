# Authentication

To use this plugin, you need to authenticate against your Xray instance.
You must do this by setting up specific environment variables, e.g. a client ID and a client secret when using a cloud based Xray instance.

To avoid adding your secrets to system environment variables, simply pass them to Cypress as a comma-separated list in the command line:

```sh
npx cypress run --env XRAY_CLIENT_ID="ABCDEF",XRAY_CLIENT_SECRET="XYZ"
```

Depending on the provided combinations of environment variables, the plugin will automatically know which Xray API type to use.

When providing more than one valid combination of variables, evaluation precedence of the authentication methods is as follows:

1. Cloud authentication
2. PAT authentication
3. Basic authentication

This way, the cloud version will always be chosen in favor of the server version.

Below you will find all Xray authentication configurations that are currently supported and the environment variables you need to set to authenticate against their respective APIs.

## Xray cloud

For the cloud version of Xray, the plugin expects the following environment variables to be set:

- `XRAY_CLIENT_ID`
- `XRAY_CLIENT_SECRET`

!!! info
    Consult Xray's [official documentation](https://docs.getxray.app/display/XRAYCLOUD/Global+Settings%3A+API+Keys) on how to set up cloud API keys.

!!! example
    ```sh
    npx cypress run --env XRAY_CLIENT_ID="ABCDEF",XRAY_CLIENT_SECRET="XYZ"
    ```

## Xray server

Depending on your Jira version, you may either need to use *Personal Access Tokens* (PATs) for authenticating against Xray, or *Basic Authentication* using your Jira username and password.

!!! tip
    If you do not know which one you should be using, simply try PAT authentication first.
    If it works, great!
    You should stick to it, as PATs are a safer alternative to using usernames and passwords.

    If PAT-based authentication does not work or you cannot even create tokens, you will need to use basic authentication.

!!! note
    In addition to setting up your credentials, working with server instances requires you to provide the [Jira server URL](jira.md#serverurl) in the plugin's [Jira options](jira.md).

### PAT authentication

For server versions of Xray, the plugin expects the following environment variables to be set:

- `XRAY_API_TOKEN`

!!! info
    Consult Xray's [official documentation](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) on how to set up server API tokens.

!!! example
    ```sh
    npx cypress run --env XRAY_API_TOKEN="XYZ"
    ```

### Basic authentication

For server versions of Xray, the plugin expects the following environment variables to be set:

- `XRAY_USERNAME`
- `XRAY_PASSWORD`

!!! example
    ```sh
    npx cypress run --env XRAY_USERNAME="Bob",XRAY_PASSWORD="superSecure!unhaxx0rable"
    ```
