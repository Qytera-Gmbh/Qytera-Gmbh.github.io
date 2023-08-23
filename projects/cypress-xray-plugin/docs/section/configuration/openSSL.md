# OpenSSL

!!! tip
    Make sure to check out the [examples](../guides/openSSL.md) to see in which scenarios changing OpenSSL configuration might make sense.

Sometimes it is necessary to configure OpenSSL if your Xray instance sits behind a proxy or uses dedicated root certificates that aren't available by default.
In this case, you can set the following options prior to running your Cypress tests to configure the plugin's internal OpenSSL setup.

## Optional settings

### `rootCAPath`

Specify the path to a root CA in `.pem` format.
This will then be used during authentication & communication with the Xray instance.

***Environment variable***
: `OPENSSL_ROOT_CA_PATH`

***Type***
: `string`

***Default***
: `#!js undefined`

??? example
    === "Cypress configuration"
        ```js
        await configureXrayPlugin(config, {
            openSSL: {
                rootCAPath: "/home/cert.pem"
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env OPENSSL_ROOT_CA_PATH="/home/cert.pem"
        ```

<hr/>

### `secureOptions`

A [crypto constant](https://nodejs.org/api/crypto.html#crypto-constants) (see list below) that will be used to configure the `#!js securityOptions` of the [`https.Agent`](https://nodejs.org/api/https.html#class-httpsagent) used for sending requests to your Xray instance.
!!! note
    Compute their bitwise OR if you need to set more than one option.
??? abstract "List of Security Options"
    The following list of OpenSSL security option constants can be obtained by running the following code in a node environment:

    ```js
    import { constants } from "crypto";
    console.log(constants);
    ```

    | Name                                            | Value      |
    | ----------------------------------------------- | ---------- |
    | `OPENSSL_VERSION_NUMBER`                        | 805306480  |
    | `SSL_OP_ALL`                                    | 2147485776 |
    | `SSL_OP_ALLOW_NO_DHE_KEX`                       | 1024       |
    | `SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION`      | 262144     |
    | `SSL_OP_CIPHER_SERVER_PREFERENCE`               | 4194304    |
    | `SSL_OP_CISCO_ANYCONNECT`                       | 32768      |
    | `SSL_OP_COOKIE_EXCHANGE`                        | 8192       |
    | `SSL_OP_CRYPTOPRO_TLSEXT_BUG`                   | 2147483648 |
    | `SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS`            | 2048       |
    | `SSL_OP_EPHEMERAL_RSA`                          | 0          |
    | `SSL_OP_LEGACY_SERVER_CONNECT`                  | 4          |
    | `SSL_OP_MICROSOFT_BIG_SSLV3_BUFFER`             | 0          |
    | `SSL_OP_MICROSOFT_SESS_ID_BUG`                  | 0          |
    | `SSL_OP_MSIE_SSLV2_RSA_PADDING`                 | 0          |
    | `SSL_OP_NETSCAPE_CA_DN_BUG`                     | 0          |
    | `SSL_OP_NETSCAPE_CHALLENGE_BUG`                 | 0          |
    | `SSL_OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG`        | 0          |
    | `SSL_OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG`       | 0          |
    | `SSL_OP_NO_COMPRESSION`                         | 131072     |
    | `SSL_OP_NO_ENCRYPT_THEN_MAC`                    | 524288     |
    | `SSL_OP_NO_QUERY_MTU`                           | 4096       |
    | `SSL_OP_NO_RENEGOTIATION`                       | 1073741824 |
    | `SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION` | 65536      |
    | `SSL_OP_NO_SSLv2`                               | 0          |
    | `SSL_OP_NO_SSLv3`                               | 33554432   |
    | `SSL_OP_NO_TICKET`                              | 16384      |
    | `SSL_OP_NO_TLSv1`                               | 67108864   |
    | `SSL_OP_NO_TLSv1_1`                             | 268435456  |
    | `SSL_OP_NO_TLSv1_2`                             | 134217728  |
    | `SSL_OP_NO_TLSv1_3`                             | 536870912  |
    | `SSL_OP_PKCS1_CHECK_1`                          | 0          |
    | `SSL_OP_PKCS1_CHECK_2`                          | 0          |
    | `SSL_OP_PRIORITIZE_CHACHA`                      | 2097152    |
    | `SSL_OP_SINGLE_DH_USE`                          | 0          |
    | `SSL_OP_SINGLE_ECDH_USE`                        | 0          |
    | `SSL_OP_SSLEAY_080_CLIENT_DH_BUG`               | 0          |
    | `SSL_OP_SSLREF2_REUSE_CERT_TYPE_BUG`            | 0          |
    | `SSL_OP_TLS_BLOCK_PADDING_BUG`                  | 0          |
    | `SSL_OP_TLS_D5_BUG`                             | 0          |
    | `SSL_OP_TLS_ROLLBACK_BUG`                       | 8388608    |
    | `ENGINE_METHOD_RSA`                             | 1          |
    | `ENGINE_METHOD_DSA`                             | 2          |
    | `ENGINE_METHOD_DH`                              | 4          |
    | `ENGINE_METHOD_RAND`                            | 8          |
    | `ENGINE_METHOD_EC`                              | 2048       |
    | `ENGINE_METHOD_CIPHERS`                         | 64         |
    | `ENGINE_METHOD_DIGESTS`                         | 128        |
    | `ENGINE_METHOD_PKEY_METHS`                      | 512        |
    | `ENGINE_METHOD_PKEY_ASN1_METHS`                 | 1024       |
    | `ENGINE_METHOD_ALL`                             | 65535      |
    | `ENGINE_METHOD_NONE`                            | 0          |
    | `DH_CHECK_P_NOT_SAFE_PRIME`                     | 2          |
    | `DH_CHECK_P_NOT_PRIME`                          | 1          |
    | `DH_UNABLE_TO_CHECK_GENERATOR`                  | 4          |
    | `DH_NOT_SUITABLE_GENERATOR`                     | 8          |
    | `ALPN_ENABLED`                                  | 1          |
    | `RSA_PKCS1_PADDING`                             | 1          |
    | `RSA_NO_PADDING`                                | 3          |
    | `RSA_PKCS1_OAEP_PADDING`                        | 4          |
    | `RSA_X931_PADDING`                              | 5          |
    | `RSA_PKCS1_PSS_PADDING`                         | 6          |
    | `RSA_PSS_SALTLEN_DIGEST`                        | -1         |
    | `RSA_PSS_SALTLEN_MAX_SIGN`                      | -2         |
    | `RSA_PSS_SALTLEN_AUTO`                          | -2         |
    | `TLS1_VERSION`                                  | 769        |
    | `TLS1_1_VERSION`                                | 770        |
    | `TLS1_2_VERSION`                                | 771        |
    | `TLS1_3_VERSION`                                | 772        |
    | `POINT_CONVERSION_COMPRESSED`                   | 2          |
    | `POINT_CONVERSION_UNCOMPRESSED`                 | 4          |
    | `POINT_CONVERSION_HYBRID`                       | 6          |

***Environment variable***
: `OPENSSL_SECURE_OPTIONS`

***Type***
: `number`

***Default***
: `#!js undefined`

??? example
    === "Cypress configuration"
        ```js
        import { constants } from "crypto";

        await configureXrayPlugin(config, {
            openSSL: {
                secureOptions: constants.SSL_OP_LEGACY_SERVER_CONNECT | constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION; // 262148
            },
        });
        ```
    === "Environment variable"
        ```sh
        npx cypress run --env OPENSSL_SECURE_OPTIONS=262148
        ```
