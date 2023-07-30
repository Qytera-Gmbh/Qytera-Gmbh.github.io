# Plugin

The plugin offers several options for customizing the upload further.

## Optional settings

### `debug`
: Turns on or off extensive debugging output.
: ***Environment variable***
    : `PLUGIN_DEBUG`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js false`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            plugin: {
                debug: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_DEBUG=true
        ```

### `enabled`
: Enables or disables the entire plugin.
    Setting this option to `false` disables all plugin functions, including authentication checks, uploads or feature file synchronization.
: ***Environment variable***
    : `PLUGIN_ENABLED`
: ***Type***
    : [`boolean`](types.md#boolean)
: ***Default***
    : `#!js true`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            plugin: {
                enabled: false
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_ENABLED=false
        ```

### `logDirectory`
: The directory which all error and debug log files will be written to.
: ***Environment variable***
    : `PLUGIN_LOG_DIRECTORY`
: ***Type***
    : `string`
: ***Default***
    : `#!js "logs"`
???+ example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            plugin: {
                logDirectory: "/home/logs"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_LOG_DIRECTORY="/home/logs"
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
