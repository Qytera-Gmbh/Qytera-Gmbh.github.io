# Introduction

Apart from authentication, all configuration takes place using the `#!js configureXrayPlugin()` method in your cypress configuration file:

```js
async setupNodeEvents(on, config) {
    await configureXrayPlugin({
        jira: {
            // ...
        },
        plugin: {
            // ...
        },
        xray: {
            // ...
        },
        cucumber: {
            // ...
        },
        openSSL: {
            // ...
        },
    });
}
```

Every option can also be set via environment variables:
```sh
npx cypress run --env JIRA_PROJECT_KEY="PRJ",\
                      JIRA_TEST_EXECUTION_ISSUE_KEY="PRJ-123",\
                      XRAY_STATUS_PASSED="SUCCESS"
```
Alternatively (see [Cypress documentation](https://docs.cypress.io/guides/guides/environment-variables#Setting)):
```sh
CYPRESS_JIRA_PROJECT_KEY="PRJ" \
CYPRESS_JIRA_TEST_EXECUTION_ISSUE_KEY="PRJ-123" \
CYPRESS_XRAY_STATUS_PASSED="SUCCESS" \
npx cypress run
```

!!! note
    If you specify options in this method **and** provide their respective environment variables, the environment variable will take precedence over the option specified in the method.

!!! tip
    Use `#!js configureXrayPlugin()` to specify defaults when running and developing tests locally and environment variables in CI/CD setups to override these defaults.