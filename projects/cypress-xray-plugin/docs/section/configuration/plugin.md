# Plugin

The plugin offers several options for customizing the upload further.

## Optional settings

### `debug`

Turns on or off extensive debugging output.

***Environment variable***
: `PLUGIN_DEBUG`

***Type***
: [`boolean`](types.md#boolean)

***Default***
: `#!js false`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            plugin: {
                debug: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_DEBUG=true
        ```

<hr/>

### `enabled`

Enables or disables the entire plugin.
Setting this option to `false` disables all plugin functions, including authentication checks, uploads or feature file synchronization.

***Environment variable***
: `PLUGIN_ENABLED`

***Type***
: [`boolean`](types.md#boolean)

***Default***
: `#!js true`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            plugin: {
                enabled: false
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_ENABLED=false
        ```

<hr/>

### `listener`

A listener function for handling plugin events, similar to the Cypress's `setupNodeEvents` function.

***Type***
: `function`

??? example

    ```js
    await configureXrayPlugin(on, config, {
        plugin: {
            listener: ({ on }) => {
                // Will be invoked as soon as the results have been uploaded:
                on("upload:cypress", (data) => {
                    console.log(data.testExecutionIssueKey);
                });

                // Supports async callbacks, too:
                on("upload:cucumber", async (data) => {
                    await writeFile("data.json", JSON.stringify(data));
                });
            }
        }
    });
    ```

<hr/>

### `logDirectory`

The directory which all error and debug log files will be written to.

***Environment variable***
: `PLUGIN_LOG_DIRECTORY`

***Type***
: `string`

***Default***
: `#!js "logs"`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            plugin: {
                logDirectory: "/home/logs"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_LOG_DIRECTORY="/home/logs"
        ```

<hr/>

### `logger`

A custom logger function that replaces the default ANSI-based logger for the plugin.
If specified, this logger will completely replace the default plugin logger.

Messages passed to this function:

- will not contain the prefix `│ Cypress Xray Plugin │`

- will not contain ANSI escape characters

- may contain line break characters

***Type***
: `function`

??? example

    The following example produces log messages with custom prefixes and debug messages that are only output if a corresponding environment variable is defined.

    ```js
    await configureXrayPlugin(on, config, {
        plugin: {
            logger: (level, ...text) => {
                switch (level) {
                    case "debug":
                        if (process.env.DEBUG) {
                          console.debug(...text);
                        }
                        break;
                    case "error":
                        console.error("oh no", ...text);
                        break;
                    case "info":
                        console.info("fyi", ...text);
                        break;
                    case "notice":
                        console.log("please beware", ...text);
                        break;
                    case "warning":
                        console.warn("danger", ...text);
                        break;
                }
            }
        },
    });
    ```

<hr/>

### `normalizeScreenshotNames`

Some Xray setups might struggle with uploaded evidence if the filenames contain non-ASCII characters.
With this option enabled, the plugin only keeps characters `a-zA-Z0-9.` in screenshot names and replaces all other sequences with `_`.

***Environment variable***
: `PLUGIN_NORMALIZE_SCREENSHOT_NAMES`

***Type***
: [`boolean`](types.md#boolean)

***Default***
: `#!js false`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            plugin: {
                normalizeScreenshotNames: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_NORMALIZE_SCREENSHOT_NAMES=true
        ```

<hr/>

### `splitUpload`

Enables split upload mode for evidence files such as screenshots and videos, which are then uploaded in multiple smaller requests rather than in a single large request.
This approach helps to avoid server-side request size limitations, and can also be useful for avoiding `JSON.stringify` token length errors.

If set to `true`, evidence uploads will be sent concurrently for each test issue.
This may cause them to appear out of order in Xray.
If the order is important, but split uploads are still desired, the `sequential` setting can be used.

***Environment variable***
: `PLUGIN_SPLIT_UPLOAD`

***Type***
: [`boolean`](types.md#boolean) or `#!js "sequential"`

***Default***
: `#!js false`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            plugin: {
                splitUpload: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_SPLIT_UPLOAD=true
        ```

<hr/>

### `uploadLastAttempt`

If set to `true` and [test retries](https://docs.cypress.io/app/guides/test-retries) are enabled in Cypress, failed test attempts and their associated screenshots will be omitted from the upload to Xray, i.e. only the _last_ attempt of each test will be included.

***Environment variable***
: `PLUGIN_UPLOAD_LAST_ATTEMPT`

***Type***
: [`boolean`](types.md#boolean)

***Default***
: `#!js false`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(on, config, {
            plugin: {
                uploadLastAttempt: true
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env PLUGIN_UPLOAD_LAST_ATTEMPT=true
        ```

