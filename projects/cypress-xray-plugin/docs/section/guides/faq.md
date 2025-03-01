# FAQ

Here is a list of common concerns or issues and how to deal with them.

<hr/>

## Trusting custom root CAs

In case an Xray instance is set up on an internal network with custom [CA certificates](https://www.ssl.com/faqs/what-is-a-certificate-authority/), you will need to download these certificates and provide them to the Xray plugin.

Error messages requiring you to provide custom SSL certificates may look like any of the following:

!!! failure "**Error: unable to get issuer certificate**"

!!! failure "**Error: unable to verify the first certificate**"

!!! success "Solution"
    Download the SSL certificate of your CA and make sure it is in `.pem` format.
    Then, tell the plugin to trust that CA by providing the certificate's path in [the HTTP options](../configuration/http.md):

    ```js
    import { Agent } from "node:https";

    await configureXrayPlugin(on, config, {
        http: {
            httpsAgent: new Agent({
                ca: "/home/cert.pem",
            }),
        },
    });
    ```

<hr/>

## Providing security options

Some web servers may be running outdated or legacy code, including the one on which your Xray instance is be installed.
Modern HTTP clients usually reject communication attempts to communicate with such servers for security reasons.
However, clients can be instructed to allow insecure communcation by setting appropriate flags.

Error messages that require you to provide security options may look like any of the following:

!!! failure "**Error: unsafe legacy renegotiation disabled**"

!!! success "Solution"
    [Allow legacy insecure renegotiation between OpenSSL and unpatched clients or servers](https://www.openssl.org/docs/man1.1.1/man3/SSL_clear_options.html):

    ```js
    import { constants } from "node:crypto";
    import { Agent } from "node:https";

    await configureXrayPlugin(on, config, {
        http: {
            httpsAgent: new Agent({
                secureOptions: constants.SSL_OP_LEGACY_SERVER_CONNECT,
            }),
        },
    });
    ```

## Configuring a proxy

Depending on your network infrastructure, you may need to configure proxy servers for the web requests that the plugin makes.

Error messages that require you to configure proxies may look like any of the following:

!!! failure "**Error: Request failed with status code 502**"

!!! success "Solution"

    You can configure a single proxy for all requests:

    ```js
    await configureXrayPlugin(on, config, {
        http: {
            proxy: {
                host: 'http://1.2.3.4',
                port: 12345,
                auth: {
                    username: 'johndoe',
                    password: 'supersecret'
                }
            }
        },
    });
    ```

    You can configure a proxy for Jira only (and similarly for Xray):

    ```js
    await configureXrayPlugin(on, config, {
        http: {
            jira: {
                proxy: {
                    host: 'http://1.2.3.4',
                    port: 12345,
                    auth: {
                        username: 'johndoe',
                        password: 'supersecret'
                    }
                }
            }
        },
    });
    ```

    You can also define different proxies for Jira and Xray:

    ```js
    await configureXrayPlugin(on, config, {
        http: {
            jira: {
                proxy: {
                    host: 'http://1.2.3.4',
                    port: 12345,
                    auth: {
                        username: 'johndoe',
                        password: 'supersecret'
                    }
                }
            },
            xray: {
                proxy: {
                    host: 'http://9.8.7.6',
                    port: 98765,
                    auth: {
                        username: 'johndoeAdmin',
                        password: 'supersecretButAdmin'
                    }
                }
            }
        },
    });
    ```

## Assigning issues

The way issues can be assigned may vary depending on your Jira version.
Typically, Jira Cloud requires the assignee's _account ID_, whereas Jira Server requires the _username_ (used to log in) instead.

The easiest way to retrieve this information is to find an existing issue where the desired assignee already appears _somewhere_ in the fields (reporter, assignee) and then to export the issue to XML.
You can then search the XML document for the desired person, which will usually appear in an HTML element.

!!! example "Jira Server"

    Assuming that the XML export contains the following line...

    ```xml
    <reporter username="jane.doe">Jane Doe</reporter>
    ```

    ... you may need to assign your test execution issues as follows:

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                fields: {
                    assignee: {
                        name: 'jane.doe'
                    }
                }
            }
        },
    });
    ```
!!! example "Jira Cloud"

    Assuming that the XML export contains the following line...

    ```xml
    <reporter accountid="12345:4762614f-a4ea-42ad-ae93-e094702190d6">Jane Doe</reporter>
    ```

    ... you may need to assign your test execution issues as follows:

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                fields: {
                    assignee: {
                        accountId: '12345:4762614f-a4ea-42ad-ae93-e094702190d6'
                    }
                }
            }
        },
    });
    ```


!!! failure "**Error assembling issue data: expected Object containing a `name` property**"

!!! success "Solution"

    Instead of assigning issues using the assignee's Jira ID or email address, you'll need to use their username instead (which they e.g. use to log in):

    ```js
    await configureXrayPlugin(on, config, {
        jira: {
            testExecutionIssue: {
                fields: {
                    assignee: {
                        name: 'username'
                    }
                }
            }
        },
    });
    ```

## Rate limiting

[Jira Cloud](https://developer.atlassian.com/cloud/jira/platform/rate-limiting/) and [Xray Cloud](https://docs.getxray.app/display/ProductKB/%5BXray+Cloud%5D+Rest+API+Limit) use rate limiting in their APIs.
If you're using Jira/Xray Server, your local server instance may also be rate limiting network requests.
This can be a problem for larger projects, as the plugin processes as much concurrently as possible.
For example, Cucumber feature files are all imported at the same time, as their imports do not affect each other.

!!! failure "**Request failed with status code 429**"

!!! success

    An easy way to avoid hitting API rate limits is to set a maximum number of requests per second.

    The following configuration ensures that _all_ requests (regardless of which API they are targeting) are sent every 200ms.

    ```js

    await configureXrayPlugin(on, config, {
        http: {
            rateLimiting: {
                requestsPerSecond: 5
            }
        },
    });
    ```

    The following configuration ensures that Jira requests are sent every 200ms, while Xray requests are sent once per second.

    ```js

    await configureXrayPlugin(on, config, {
        http: {
            jira: {
                rateLimiting: {
                    requestsPerSecond: 5
                }
            },
            xray: {
                rateLimiting: {
                    requestsPerSecond: 1
                }
            }
        },
    });
    ```

## Handling large uploads

Large test suites can cause problems when trying to upload their results to Xray, especially if screenshots are included as evidence.

!!! failure "**RangeError: Invalid string length**"

!!! success

    The plugin is able to split result uploads into multiple requests using the [`splitUploads`](../configuration/plugin.md#splitupload) setting.

    If enabled, this will cause the plugin to dispatch several upload requests requests instead of a single, large one:

    - the initial status upload (pass/fail/...)

    - one request per test evidence (screenshot, ...)

    ```js

    await configureXrayPlugin(on, config, {
        plugin: {
            splitUpload: true
        },
    });
    ```
