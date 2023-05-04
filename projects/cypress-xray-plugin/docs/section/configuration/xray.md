# Xray

You can provide a bunch of Xray settings which might become necessary depending on your project configuration.

## Optional settings

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
        await configureXrayPlugin({
            xray: {
                uploadResults: false
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_UPLOAD_RESULTS=false
        ```

### `statusPassed`
: The status name of a test marked as passed in Xray.
    Should be used when custom status names have been setup in Xray.
: ***Environment variable***
    : `XRAY_STATUS_PASSED`
: ***Type***
    : `string`
: ***Default***
    : `#!js "PASSED"`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            xray: {
                statusPassed: "SUCCESS"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_PASSED=SUCCESS
        ```

### `statusFailed`
: The status name of a test marked as failed in Xray.
    Should be used when custom status names have been setup in Xray.
: ***Environment variable***
    : `XRAY_STATUS_FAILED`
: ***Type***
    : `string`
: ***Default***
    : `#!js "FAILED"`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            xray: {
                statusFailed: "FAILURE"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_STATUS_FAILED=FAILURE
        ```

### `testType`
: The test type of the test issues.
    This option will be used to set the corresponding field on Xray issues created during upload (happens when a test does not yet have a corresponding Xray issue).
: ***Environment variable***
    : `XRAY_TEST_TYPE`
: ***Type***
    : `string`
: ***Default***
    : `#!js "Manual"`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            xray: {
                testType: "Cucumber"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env XRAY_TEST_TYPE=Cucumber
        ```
