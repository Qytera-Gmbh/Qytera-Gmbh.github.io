# QTAF Drivers

This article explains how to use QTAF to test on different browsers easily and without changing your source code.

## What are drivers?

A driver provides an interface between the test framework and the browser or the device with which a (web) application is to be tested. For example, if a web application is to be developed and it should run on the most common browsers, it is advisable to test the application automatically. This requires an interface between the test framework (for example Selenium) and the browser (Chrome, Firefox, Edge, Safari, ...). For each browser there is a driver that abstracts the details of how the browser is controlled and thus enables the tester to test his test cases with different browsers without changing his code.

QTAF relieves the tester of the initialisation of a driver object. The tester only has to specify via the configuration file which browser he wants to use for testing.  To do this, he enters the name of the driver in the attribute `driver.name` of the configuration file. Alternatively, the environment variable `DRIVER_NAME` can be set or the parameter `-Ddriver.name` can be passed via the command line when executing the test cases.

## List of Selenium driver configurations provided by QTAF.

The following is a list of Selenium drivers provided by the QTAF framework and the names you have to set for the parameter `driver.name`to use these.

|         Driver        |   `driver.name`  |                                     Description                                     |
|:----------------------:|:--------------:|:------------------------------------------------------------------------------------:|
| ChromeDriver           | chrome         | Driver for testing on a Chrome browser.                                              |
| ChromeRemoteDriver     | chrome-remote  | Driver for testing on a Chrome browser that is accessible via a network connection.  |
| EdgeDriver             | edge           | Driver for testing on an Edge browser.                                               |
| EdgeRemoteDriver             | edge-remote           | Driver for testing on an Edge browser that is accessible via a network connection.                                               |
| FirefoxDriver          | firefox        | Driver for testing on a Firefox browser.                                             |
| FirefoxRemoteDriver    | firefox-remote | Driver for testing on a Firefox browser that is accessible via a network connection. |
| OperaDriver            | opera          | Driver for testing on an Opera browser.                                              |
| OperaRemoteBrowser     | opera-remote   | Driver for testing on an Opera browser that is accessible via a network connection.  |
| InternetExplorerDriver | ie             | Driver for testing on an Internet Explorer browser.                                  |
| SaucelabsDriver        | sauce          | Driver for testing on the Saucelabs platform                                         |

## Use a local browser for testing

QTAF uses the <a href="https://github.com/bonigarcia/webdrivermanager" target="_blank">Webdrivermanager</a>, so there is no need to install a Selenium driver on your PC. However, you must ensure that the desired browsers are installed on your PC. To test on a local browser, set the following configuration parameters:

| Configuration parameter |                        Value                        |                 Description                 |
|:-----------------------:|:--------------------------------------------------:|:--------------------------------------------:|
| driver.name             | “chrome” \| “firefox” \| “edge” \| “opera” \| “ie” | Name of the drivers |

This is already sufficient for QTAF to be able to execute the test cases on the desired browser. When executing the test cases, QTAF automatically starts the browser and executes the test cases in it.

## Running test cases on a remote browser

The Selenium driver and QTAF do not have to be on the same computer. It is also possible to connect QTAF to remote drivers via a network connection. Use cases for this include Docker environments or virtual machines running a Selenium driver. To do this, set the following configuration parameters:

| Configuration parameter |                          Value                         |                                 Description                                 |
|:-----------------------:|:-----------------------------------------------------:|:----------------------------------------------------------------------------:|
| driver.name             | “chrome-remote” \| “firefox-remote” \| “opera-remote” | Name des zu verwendenden Browsers / Treibers                                 |
| driver.remoteUrl        | `<remote url>`                                          | URL under which the Selenium driver can be reached, e.g. 10.0.0.1:5555/wd/hub |

For Docker, there are already pre-configured images that you can use out of the box. For example, you can create the following Docker Compose file and then connect to the Selenium containers.

```yaml
version: '3'
services:
  # Selenium chrome
  selenium-chrome:
    image: selenium/standalone-chrome-debug
    ports:
      - '4444:4444'
    restart: always

  # Selenium firefox
  selenium-firefox:
    image: selenium/standalone-firefox-debug
    ports:
      - '4445:4444'
    restart: always

  # Selenium opera
  selenium-opera:
    image: selenium/standalone-opera-debug
    ports:
      - '4446:4444'
    restart: always
```

Assuming that the containers are running on your local machine, you need to set the following values for your configuration parameters:

| Treiber | driver.name |    driver.RemoteUrl   |
|:-------:|:-----------:|:---------------------:|
| Chrome  | chrome      | 127.0.0.1:4444/wd/hub |
| Firefox | firefox     | 127.0.0.1:4445/wd/hub |
| Opera   | opera       | 127.0.0.1:4446/wd/hub |


## Running test cases on the Saucelabs platform

QTAF can also run test cases on virtual machines provided by the Saucelabs platform. In order for QTAF to connect to Saucelabs virtual machines, the following configuration values must be set.

| Configuration parameter |                        Value                        |                                            Description                                            |
|:-----------------------:|:--------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
| driver.remoteUrl        | https://ondemand.eu-central-1.saucelabs.com/wd/hub | URL under which the Selenium driver from Saucelabs can be reached. See also the following <a href="https://docs.saucelabs.com/basics/data-center-endpoints/" target="_blank">link</a>. |
| driver.name             | sauce                                              |                                                                                                    |
| driver.version          | `<driver_version>`                                   | version of the driver / browsers                                                                    |
| sauce.browserName       | `<browser_name>`                                      | Name of the browser (Chrome, Firefox, …), see <a href="https://saucelabs.com/platform/supported-browsers-devices" target="_blank">link                                                 |</a>
| driver.platform         | `<platform_name>`                                     | Name of the platform (Windows 10, Windows 11, …), siehe <a href="https://saucelabs.com/platform/supported-browsers-devices" target="_blank">link</a>                                         |
| sauce.username          | `<username>`                                         | Saucelabs username (use environment variables for this configuration parameter for security reasons)                      |
| sauce.accessKey         | `<access_key>`                                       | Saucelabs access key (use environment variables for this configuration parameter for security reasons)                    |

## Writing your own drivers

In some scenarios, QTAF's pre-configured drivers may not meet the tester's needs. In this case, QTAF offers the possibility to write your own driver class and use it during testing. 

Let us assume for the following scenario that you want to test on a browser for which Qtaf does not provide a corresponding driver. However, you have found a library that provides such a Selenium-compatible driver and now want to use this driver with Qtaf. Proceed as follows:

Create a package in your Java project in which you want to write the driver class. In this example, this is the package `org.acme.driver`.

In this package, create a class that implements the class `de.qytera.qtaf.core.driver.AbstractDriver`. In our example, this class is called `MyDriver`. Now you have to implement the following methods: `getName` and `getDriver`. The method `getName` returns the name of the browser to be used in the configuration file. The `getDriver` method returns a driver object that implements the `WebDriver` interface of the Selenium framework.

```java
package org.acme;

import de.qytera.qtaf.core.driver.AbstractDriver;
import org.openqa.selenium.WebDriver;

public class MyDriver extends AbstractDriver {
    @Override
    public String getName() {
        return "my-driver"; // Replace this with your own name
    }

    @Override
    public WebDriver getDriver() {
        return new SampleDriver(); // Replace this with your own driver implementation
    }
}
```

In order for QTAF to be able to find your implementation of the driver, you must also enter the name of the package in which the driver is to be found in the configuration file. You can also enter several packages here. Qtaf will scan this package for all classes that implement the `AbstractDriver` interface.

```json
{
  "framework": {
    "packageNames": [
      "org.acme.driver"
    ]
  }
}
```

Now you have to enter the name of your driver in the configuration file.

```json
{
  "driver": {
    "name": "my-driver"
  }
}
```

Now you can run your tests with the new driver.

<hr>
<a href="https://github.com/Qytera-Gmbh/QTAF" target="_blank">QTAF Repository</a><br>
<a href="https://www.qytera.de" target="_blank">Developed with love by Qytera, Germany</a>