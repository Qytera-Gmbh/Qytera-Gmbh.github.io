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

### `preferences`

Additional browser preferences to pass to the web driver options on instantiation.

!!! info
    These preferences will be passed to the driver options as follows:

    - Chromium: as [experimental options](https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/chromium/ChromiumOptions.html#setExperimentalOption(java.lang.String,java.lang.Object))
    - Firefox: as a [firefox profile](https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/firefox/FirefoxProfile.html)

***Environment variable***
: `DRIVER_PREFERENCES`

***Type***
: `JSON object`

??? example
    === "QTAF JSON"

        The following will set the download directory in [Chromium-based browsers](https://chromedriver.chromium.org/capabilities) to `/home/me/downloads`.

        ```json
        "driver": {
          "preferences": {
            "prefs": {
              "download.default_directory": "/home/me/downloads"
            }
          }
        }
        ```

    === "Environment variable"
        ```sh
        DRIVER_PREFERENCES="{prefs: {download.default_directory: /home/me/downloads}}"
        ```

### Download Directory

#### Chromium-based drivers

You can set the download directory for Chrome and Edge in the following way:

```json
"preferences": {
  "download": {
    "default_directory": "C:\\Users\\your_username",
    "prompt_for_download": false,
    "directory_upgrade": true
  }
}
```

#### Firefox

When using the firefox webdriver you can change the download directory in the following way:

```json
"preferences": {
  "browser.download.folderList": 2,
  "browser.download.manager.showWhenStarting": false,
  "browser.download.dir": "C:\\Users\\your_username",
}
```

#### Using variables

You can also use the expressions `$USER_DIR` and `$USER_HOME` in your download path. `$USER_HOME` will be replaced by the home directory of the currently logged in user and `$USER_DIR` by the directory where the QTAF project is stored in.

For example you can save the downloads (for Chromium based drivers) in the `resources` directory of your project with the following configuration:

```json
"preferences": {
  "download": {
    "default_directory": "$USER_DIR/src/test/resources",
}
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
