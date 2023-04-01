# Plugin

The plugin offers several options for customizing the upload further.

## Optional settings

### `overwriteIssueSummary`
: Decide whether to keep the issues' existing summaries or whether to overwrite them with each upload.
: ***Environment variable***
    : `PLUGIN_OVERWRITE_ISSUE_SUMMARY`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            plugin: {
                overwriteIssueSummary: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_OVERWRITE_ISSUE_SUMMARY=true
        ```

### `normalizeScreenshotNames`
: Some Xray setups might struggle with uploaded evidence if the filenames contain non-ASCII characters.
    With this option enabled, the plugin only keeps characters `a-zA-Z0-9.` in screenshot names and replaces all other sequences with `_`.
: ***Environment variable***
    : `PLUGIN_NORMALIZE_SCREENSHOT_NAMES`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin({
            plugin: {
                normalizeScreenshotNames: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_NORMALIZE_SCREENSHOT_NAMES=true
        ```

