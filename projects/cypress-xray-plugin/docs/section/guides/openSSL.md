# OpenSSL

It is not unlikely that you will find yourself sitting behind a proxy or for your Xray instance to be accessible through VPN only.
In such scenarios, default HTTP requests might fail because of security concerns.

Here, you will find a list of common security issues and how to approach them.

<hr/>

## Trusting custom root CAs

In case an Xray instance is setup on an internal network with custom [CA certificates](https://www.ssl.com/faqs/what-is-a-certificate-authority/), you will need to download these certificates and provide them to the Xray plugin.

Error messages requiring you to provide custom SSL certificates might look like any of the following:

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

Some webservers might run outdated or legacy code, including the one where your Xray instance might be installed.
Modern HTTP clients usually reject communication attempts to such servers out of security considerations.
The clients can however be told to allow insecure communcation by setting appropriate flags.

Error messages requiring you to provide security options might look like any of the following:

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