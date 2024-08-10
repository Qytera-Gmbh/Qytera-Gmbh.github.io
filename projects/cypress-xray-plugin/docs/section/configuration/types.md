# Option types

Below you will find accepted values of custom option types you can use when providing values to options through environment variables.

## `boolean`

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

## `string[]`

***Accepted values***
: A JSON parseable list of strings.

!!! info
    Parsing is done by Cypress, so it's difficult to actually describe [the parsing rules](https://github.com/cypress-io/cypress/blob/fd2a27d62077f138b9bb8df5716e72b9f52be431/packages/server/lib/util/args.js) it applies.
    The most important rules seem to be:

    - add quotes if your string contains whitespace
    - add quotes if your string contains a comma
    - no whitespace outside quotes

!!! example
    ```sh
    npx cypress run --env XRAY_TEST_ENVIRONMENTS=[DEV,"Cool Test Environment",2.3]

## `object`

***Accepted values***
: A JSON parseable object.

!!! info
    Parsing is done by Cypress, so it's difficult to actually describe [the parsing rules](https://github.com/cypress-io/cypress/blob/fd2a27d62077f138b9bb8df5716e72b9f52be431/packages/server/lib/util/args.js) it applies.
    The most important rules seem to be:

    - add quotes if your string contains whitespace
    - add quotes if your string contains a comma
    - no whitespace outside quotes

!!! example
    ```sh
    npx cypress run --env JIRA_TEST_EXECUTION='{"fields":{"summary":"My execution!"}}'
    ```