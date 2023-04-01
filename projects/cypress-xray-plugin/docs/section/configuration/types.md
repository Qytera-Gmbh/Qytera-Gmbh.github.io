# Option types

Below you will find accepted values of custom option types you can use when providing values to options through environment variables.

## Boolean
***Accepted values***
: - `true`
    `1`
    `yes`
    `y`
    `on`

: - `false`
    `0`
    `no`
    `n`
    `off`

!!! example
    ```sh
    npx cypress run --env XRAY_UPLOAD_RESULTS=yes
    ```