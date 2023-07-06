# Installation

This plugin can either be run:

- *without* Cucumber support (standard): when you keep all your Cypress test cases in plain JavaScript/TypeScript files
- *with* Cucumber support: when using Cucumber feature files for running tests

!!! tip
    You can always switch between both setups later on.
    If you are unsure and want to try things out first, do not setup Cucumber for now.

Run the following command to add the plugin to your Cypress project:

```sh
npm i -D cypress-xray-plugin
```

and register the plugin's event listeners in the `e2e.js` file:

```js
import "cypress-xray-plugin/register";
```

## Standard installation

Modify the `#!js setupNodeEvents()` function in your Cypress configuration file as follows:

```js
import { addXrayResultUpload, configureXrayPlugin } from "cypress-xray-plugin/plugin";

// ...
    async setupNodeEvents(on, config) {
        await configureXrayPlugin({
            jira: {
                projectKey: "PRJ" // just a placeholder
            }
        });
        await addXrayResultUpload(on);
    }
// ...
```

!!! tip
    Check out the [configuration](../configuration/introduction.md) for more information on how you should configure the plugin to make it work within *your* infrastructure.
    You can also shoot a glance at the [examples](../guides/uploadTestResults.md#how-it-works) for a more hands-on approach.

## Cucumber support

!!! development
    Please note that Cucumber support is still in an experimental development stage.
    You should probably expect Cucumber features to not work consistently for the time being.

For Cucumber support, this plugin builds upon the [`cypress-cucumber-preprocessor`](https://github.com/badeball/cypress-cucumber-preprocessor) plugin for executing Cucumber feature files.

With added Xray synchronization, this plugin allows you to automatically download or upload feature files to Xray when running your Cypress tests and to track their execution results in Xray.

Run the following commands to add Cucumber executability to your project:

```sh
npm i -D @badeball/cypress-cucumber-preprocessor
npm i -D @bahmutov/cypress-esbuild-preprocessor
npm i -D cypress-on-fix
```

!!! note
    Package `cypress-on-fix` is required for registering multiple event handlers to Cypress's events (see [here](https://github.com/badeball/cypress-cucumber-preprocessor/blob/master/docs/event-handlers.md)).

To enable the plugin, modify the `#!js setupNodeEvents()` function in your Cypress configuration file as follows:

```js hl_lines="10-17 19 21"
import { addCucumberPreprocessorPlugin } from "@badeball/cypress-cucumber-preprocessor";
import createEsbuildPlugin from "@badeball/cypress-cucumber-preprocessor/esbuild";
import * as createBundler from "@bahmutov/cypress-esbuild-preprocessor";
import { addXrayResultUpload, configureXrayPlugin, syncFeatureFile } from "cypress-xray-plugin/plugin";
import fix from "cypress-on-fix";

// ...
    async setupNodeEvents(on, config) {
        const fixedOn = fix(on);
        await configureXrayPlugin({
            jira: {
                projectKey: "PRJ"
            },
            cucumber: {
                featureFileExtension: ".feature"
            }
        });
        await addCucumberPreprocessorPlugin(fixedOn, config);
        await addXrayResultUpload(fixedOn);
        fixedOn("file:preprocessor", async (file) => {
            await syncFeatureFile(file);
            const cucumberPlugin = createBundler({
                plugins: [createEsbuildPlugin(config)],
            });
            return cucumberPlugin(file);
        });
        return config;
    }
// ...
```

The highlighted lines are the ones addressing Xray support.

??? info "Lines 10-17"
    Here you should configure the Xray plugin the way you want it to work with your Xray instance.
    Read [this](../configuration/introduction.md) for more information.

??? info "Line 19"
    This line enables the upload of test results to your Xray instance when Cypress is done running your tests.

??? info "Line 21"
    This line enables upstream and downstream synchronization of your feature files with your Xray instance.
    See [here](../guides/featureFileSynchronization.md) for more information.
