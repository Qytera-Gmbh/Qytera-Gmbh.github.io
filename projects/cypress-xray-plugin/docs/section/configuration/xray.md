# Xray

You can provide a bunch of Xray settings which might become necessary depending on your project configuration.

## Optional settings

### `status`

These status options represent mapping of Cypress statuses to corresponding Xray statuses.
If you have custom statuses setup in Xray, you should provide their names here.

<hr/>

#### `failed`

The Xray status name of a test marked as failed by Cypress.

***Environment variable***
: `XRAY_STATUS_FAILED`

***Type***
: `string`

***Default***
: `#!js "FAIL"` (when providing Xray server credentials)
: `#!js "FAILED"` (when providing Xray cloud credentials)

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                status: {
                    failed: "FAILURE"
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_FAILED=FAILURE
        ```

<hr/>

#### `passed`

The Xray status name of a test marked as passed by Cypress.

***Environment variable***
: `XRAY_STATUS_PASSED`

***Type***
: `string`

***Default***
: `#!js "PASS"` (when providing Xray server credentials)
: `#!js "PASSED"` (when providing Xray cloud credentials)

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                status: {
                    passed: "SUCCESS"
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_PASSED=SUCCESS
        ```

<hr/>

#### `pending`

The Xray status name of a test marked as pending by Cypress.

***Environment variable***
: `XRAY_STATUS_PENDING`

***Type***
: `string`

***Default***
: `#!js "TODO"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                status: {
                    pending: "AWAITING EXECUTION"
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_PENDING="AWAITING EXECUTION"
        ```

<hr/>

#### `skipped`

The Xray status name of a test marked as skipped by Cypress.

***Environment variable***
: `XRAY_STATUS_SKIPPED`

***Type***
: `string`

***Default***
: `#!js "FAILED"`

    !!! note
        Defaults to `#!js "FAILED"` because Cypress only skips test cases if errors occur, as described [here](https://docs.cypress.io/guides/core-concepts/writing-and-organizing-tests#Skipped).

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            xray: {
                status: {
                    skipped: "IGNORED"
                }
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_SKIPPED="IGNORED"
        ```

<hr/>

### `uploadResults`

Turns execution results upload on or off.
Useful when switching upload on or off from the command line (via environment variables).

***Environment variable***
: `XRAY_UPLOAD_RESULTS`

***Type***
: [`boolean`](types.md#boolean)

***Default***
: `#!js true`

??? example
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

<hr/>

### `uploadScreenshots`

Turns on or off the upload of screenshots Cypress takes during test execution.
!!! note
    This option only takes effect once [`uploadResults`](#uploadresults) is turned on.
    It is not possible to upload screenshots without uploading results.

***Environment variable***
: `XRAY_UPLOAD_SCREENSHOTS`

***Type***
: [`boolean`](types.md#boolean)

***Default***
: `#!js true`

??? example
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
