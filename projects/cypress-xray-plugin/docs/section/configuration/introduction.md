# Introduction

Apart from authentication, all configuration takes place using the `#!js configureXrayPlugin()` method in your cypress configuration file:

```js
async setupNodeEvents(on, config) {
    await configureXrayPlugin(config, {
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

<hr/>

## Separation of Xray and Jira

You will probably wonder at some point why there's a split between Jira and Xray for some options, although they might be doing similar things, such as Jira's [`attachVideos`](jira.md#attachvideos) and Xray's [`uploadScreenshots`](xray.md#uploadscreenshots).
The reason for this are the two different APIs which need to be worked with behind the scenes.

On the one hand, there is the Xray API for dealing with tasks specific to Xray which don't exist in native Jira, such as test steps or screenshot evidence.
On the other hand, there is the Jira API for tasks Jira handles natively, such as attaching files to arbitrary issues.

An option's category is therefore simply determined by whichever API needs to be used to fulfill its tasks.

!!! abstract "Feedback"
    Feel free to [create an issue](https://github.com/Qytera-Gmbh/cypress-xray-plugin/issues) for options where you find the split confusing or unnecessary, so that potential clarifications can be discussed.