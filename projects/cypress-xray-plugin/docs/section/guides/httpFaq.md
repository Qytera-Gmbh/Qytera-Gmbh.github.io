# HTTP FAQ

It is not unlikely that you are behind a proxy or that your Xray instance is only accessible via a VPN.
In such scenarios, standard HTTP requests may fail due to security concerns.

Here is a list of common HTTP concerns or security issues and how to deal with them.

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