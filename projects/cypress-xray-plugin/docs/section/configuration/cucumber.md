# Cucumber

When Cucumber is enabled, you can use the following options to configure the way the plugin works with your feature files.

## Mandatory settings

### `featureFileExtension`
: The file extension of feature files you want to run in Cypress.
    The plugin will use this to parse all matching files to extract any tags contained within them.
    Such tags are needed to identify to which test issue a feature file belongs (see [targeting existing test issues with Cucumber](../guides/targetingExistingIssues.md#cucumber)).
: ***Environment variable***
    : `CUCUMBER_FEATURE_FILE_EXTENSION`
: ***Type***
    : `string`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            cucumber: {
                featureFileExtension: ".feature"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env CUCUMBER_FEATURE_FILE_EXTENSION=".feature"
        ```

## Optional settings

### `uploadFeatures`
: Set it to true to automatically create or update existing Xray issues (summary, steps), based on the feature file executed by Cypress.
    !!! note
        Enable this option if the source of truth for test cases are local feature files in Cypress and Xray is only used for tracking execution status/history.
: ***Environment variable***
    : `CUCUMBER_UPLOAD_FEATURES`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            cucumber: {
                uploadFeatures: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env CUCUMBER_UPLOAD_FEATURES=true
        ```

### `downloadFeatures`
!!! development
    This feature will be added in future versions of the plugin.

: Set it to true to automatically download feature files from Xray for Cypress to execute.
    !!! note
        Enable this option if the source of truth for test cases are step definitions in Xray and Cypress is only used for running tests.
: ***Environment variable***
    : `CUCUMBER_DOWNLOAD_FEATURES`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            cucumber: {
                downloadFeatures: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env CUCUMBER_DOWNLOAD_FEATURES=true
        ```
