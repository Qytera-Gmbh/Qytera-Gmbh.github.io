# Configuration

Here you can find descriptions, examples and use cases for all global QTAF settings.

## `driver`

The driver settings are essential for the web driver to properly interact with your application.

### `options`

A list of [browser options](https://www.selenium.dev/documentation/webdriver/drivers/options/) to pass to the web driver on instantiation.

***Environment variable***
: `DRIVER_OPTIONS`

***Type***
: `string[]`

??? example
    === "QTAF JSON"

        ```json
        "driver": {
          "options": [
            "--headless",
            "--disable-gpu",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
          ]
        }
        ```

    === "Environment variable"
        ```sh
        DRIVER_OPTIONS="[--headless, --disable-gpu, --ignore-certificate-errors, --disable-extensions, --no-sandbox, --disable-dev-shm-usage]"
        ```

<hr/>

### `capabilities`

A [capabilities](https://w3c.github.io/webdriver/#capabilities) object to pass to the web driver on instantiation.

***Environment variable***
: `DRIVER_CAPABILITIES`

***Type***
: `JSON object`

??? example
    === "QTAF JSON"

        ```json
        "driver": {
          "capabilities": {
            "acceptInsecureCerts": true,
            "elementScrollBehavior": 1,
            "customCapability": [42, "yes", false]
          }
        }
        ```

    === "Environment variable"
        ```sh
        DRIVER_CAPABILITIES="{acceptInsecureCerts: true, elementScrollBehavior: 1, customCapability: [42, yes, false]}"
        ```

<hr/>

<div style="display: flex; flex-direction: row; justify-content: space-between">
  <a href="https://www.qytera.de" target="_blank">Developed with love by Qytera, Germany</a>
  <span>|</span>
  <a href="https://www.qytera.de/testautomatisierung-workshop" target="_blank">Support & Service</a>
  <span>|</span>
  <a href="https://github.com/Qytera-Gmbh/QTAF" target="_blank">QTAF Repository</a>
  <span>|</span>
  <a href="https://www.qytera.de/kontakt" target="_blank">Contact</a><br>
</div>
