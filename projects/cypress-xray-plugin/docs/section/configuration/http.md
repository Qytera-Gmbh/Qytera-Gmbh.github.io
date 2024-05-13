# HTTP

Sometimes it's necessary to configure HTTP communication if your Xray instance sits behind a proxy or uses special root certificates that are not available by default.

!!! info
    The plugin uses [`axios`](https://www.npmjs.com/package/axios) for making requests.
    Please refer to the official documentation to see all available options.


There are three ways to specify the plugin's HTTP configuration:

- common options to use for all HTTP requests
- options to use for Jira requests only
- options to use for Xray requests only

The common options are automatically inherited by the Jira or Xray options, with the specific options overriding the common ones if repeated.

!!! example

    The following example defines a maximum timeout of 5000 milliseconds for all HTTP requests:

    ```js
    await configureXrayPlugin(on, config, {
        http: {
            timeout: 5000
        }
    });
    ```

    The following example defines:

    - a default maximum timeout of 5000 milliseconds for all HTTP requests
    - a maximum timeout of 30000 milliseconds for all HTTP requests directed at Jira

    ```js
    await configureXrayPlugin(on, config, {
        http: {
            timeout: 5000,
            jira: {
                timeout: 30000
            }
        }
    });
    ```

    The following example defines:

    - a default maximum timeout of 5000 milliseconds for all HTTP requests
    - a maximum timeout of 30000 milliseconds for all HTTP requests directed at Jira
    - a proxy configuration for HTTP requests directed at Xray

    ```js
    await configureXrayPlugin(on, config, {
        http: {
            timeout: 5000,
            jira: {
                timeout: 30000
            },
            xray: {
                proxy: {
                    host: 'http://1.2.3.4',
                    port: 12345,
                    auth: {
                        username: 'johndoe',
                        password: 'supersecret'
                    }
                }
            }
        }
    });
    ```

!!! info
    Mainly coming from an external dependency, HTTP options cannot be set via environment variables without additional configuration within the Cypress configuration file.

    ```js
    await configureXrayPlugin(on, config, {
        http: {
            timeout: process.env.HTTP_TIMEOUT ?? 5000
        }
    });
    ```