# Xray

You can provide a bunch of Xray settings which might become necessary depending on your project configuration.

## Optional settings

### `statusFailed`
: The Xray status name of a test marked as failed by Cypress.
    Should be used when custom status names have been setup in Xray.
: ***Environment variable***
    : `XRAY_STATUS_FAILED`
: ***Type***
    : `string`
: ***Default***
    : `#!js "FAIL"` (when providing Xray server credentials)
    : `#!js "FAILED"` (when providing Xray cloud credentials)
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                statusFailed: "FAILURE"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_FAILED=FAILURE
        ```

### `statusPassed`
: The Xray status name of a test marked as passed by Cypress.
    Should be used when custom status names have been setup in Xray.
: ***Environment variable***
    : `XRAY_STATUS_PASSED`
: ***Type***
    : `string`
: ***Default***
    : `#!js "PASS"` (when providing Xray server credentials)
    : `#!js "PASSED"` (when providing Xray cloud credentials)
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                statusPassed: "SUCCESS"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_PASSED=SUCCESS
        ```

### `statusPending`
: The Xray status name of a test marked as pending by Cypress.
    Should be used when custom status names have been setup in Xray.
: ***Environment variable***
    : `XRAY_STATUS_PENDING`
: ***Type***
    : `string`
: ***Default***
    : `#!js "TODO"`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                statusPending: "AWAITING EXECUTION"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_PENDING="AWAITING EXECUTION"
        ```

### `statusSkipped`
: The Xray status name of a test marked as skipped by Cypress.
    Should be used when custom status names have been setup in Xray.
: ***Environment variable***
    : `XRAY_STATUS_SKIPPED`
: ***Type***
    : `string`
: ***Default***
    : `#!js "FAILED"`

    !!! note
        Defaults to `#!js "FAILED"` because Cypress only skips test cases if errors occur, as described [here](https://docs.cypress.io/guides/core-concepts/writing-and-organizing-tests#Skipped).
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                statusSkipped: "IGNORED"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_SKIPPED="IGNORED"
        ```

### `steps`

All options related to manual test issue steps.

#### `maxLengthAction`
: The maximum length a step's action description can have in terms of characters. Some Xray instances might enforce limits on the length and reject step updates in case the action's description exceeds said limit.
: ***Environment variable***
    : `XRAY_STEPS_MAX_LENGTH_ACTION`
: ***Type***
    : `number`
: ***Default***
    : `#!js 8000` ([more info](https://github.com/Qytera-Gmbh/cypress-xray-plugin/issues/50))
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                steps: {
                    maxLengthAction: 1234
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STEPS_MAX_LENGTH_ACTION=1234
        ```

#### `update`
: Whether to update a manual test issue's test steps during execution results upload.
    !!! warning
        If set to true (default), ***all*** existing steps will be replaced with the plugin's steps.
    !!! note
        The plugin currently creates only one step containing the code of the corresponding Cypress test function.
: ***Environment variable***
    : `XRAY_STEPS_UPDATE`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                steps: {
                    update: true
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STEPS_UPDATE=true
        ```

### `uploadResults`
: Turns execution results upload on or off.
    Useful when switching upload on or off from the command line (via environment variables).
: ***Environment variable***
    : `XRAY_UPLOAD_RESULTS`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js true`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                uploadResults: false
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_UPLOAD_RESULTS=false
        ```

### `uploadScreenshots`
: Turns on or off the upload of screenshots Cypress takes during test execution.
    !!! note
        This option only takes effect once [`uploadResults`](#uploadresults) is turned on.
        It is not possible to upload screenshots without uploading results.
: ***Environment variable***
    : `XRAY_UPLOAD_SCREENSHOTS`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js true`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                uploadScreenshots: false
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_UPLOAD_SCREENSHOTS_=false
        ```
