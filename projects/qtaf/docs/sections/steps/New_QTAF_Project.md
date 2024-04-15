# How to create a new QTAF project

This article shows how a new project can be set up using the QTAF framework. First, we will show you how to install QTAF using Maven. Then we will create our first test case using QTAF.

## Set up a new project with IntelliJ

### Create new Project

To create a new project, we use the IntelliJ IDE from Jetbrains. Here we navigate in the menu to `File > New > Project` and then select `Maven` in the left selection menu and click on `Next`.

Chose a name for the project. The name can be chosen freely, but in this example we use the name "QtafProject". It is recommended to also specify the GroupId of the project. This is an identifier for the creator of the project. It is common to choose the company's domain for this, but starting with the country- or organisation-specific ending of the domain. For a company domain "acme.org", one would choose the GroupId "org.acme" according to this standard. The GroupId can be found in the sub-item Artifact Coordinates. Then we click on Finish. The new project should now have been created in the folder `~\IdeaProjects\QtafProject`, where `~` is a placeholder for the root directory of the currently logged in user.

### Customise Pom to add QTAF to the project

After creating the project, a file called `pom.xml` should have been created 
in the root directory of the project. 
This file is used to configure Maven projects, i.e. to load external libraries,
to control the build process, etc.
The file should have a similar content as the example below:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.acme</groupId>
    <artifactId>QtafProject</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

This file can be used to manage plug-ins and extensions of the project. 

#### Add the QTAF dependency

To set up QTAF you only have to include QTAF as a dependency in the project. 
To do this, add the following code to pom.xml:

```xml
<dependency>
    <groupId>de.qytera</groupId>
    <artifactId>qtaf-core</artifactId>
    <version>${qtafVersion}</version>
</dependency>
```

#### Add the current version

Replace `${qtafVersion}` by the version number with the latest version of QTAF.
You can find the available versions in the Central Maven Repository under the following link:
<a href="https://mvnrepository.com/artifact/de.qytera/qtaf-core" target="_blank">QTAF Central Repository</a>

#### Where to place your dependencies

All individual dependencies are inserted between an opening and a closing dependencies tag.
If the `<dependencies>  <!dependencies>` tag is not yet available, you can create it manually.
The structure would look something like this

```xml
<dependencies>
    <dependency>
        <!--dependency 1 -->
    </dependency>
    <dependency>
        <!--dependency 2 -->
    </dependency>
    <dependency>
        <!--dependency 3 -->
    </dependency>
</dependencies>
```
If you have a project where you just want to add QTAF as a dependency, 
it would look like this:

```xml
<dependencies>
    <dependency>
        <groupId>de.qytera</groupId>
        <artifactId>qtaf-core</artifactId>
        <version>${qtafVersion}</version>
    </dependency>
</dependencies>
```

#### Refresh the project

Every time the pom.xml file is changed, 
the project must be reloaded manually to implement the changes.
In intellij, a button to reload the dependencies is displayed in the upper right corner,
if this might be necessary.
The shortcut for Windows is `CTR + Shift + O`.

#### Check QTAF installation

The appropriate dependencies should now have been installed 
under External Libraries. 
This includes QTAF. 
To check this, search in External Libraries for libaries 
that start as follows `de.qytera:qtaf...`

### Create first test case and test class

Now the project should be initialised. We can now devote ourselves to creating the first test case.

First we create the package `org.acme.tests` in the directrory `src/test/java`, where we will store our test case classes in the future. Create a class `TestOne` in this package with the following content:

```java
package org.acme.tests;

import de.qytera.qtaf.core.config.annotations.TestFeature;
import de.qytera.qtaf.testng.context.QtafTestNGContext;
import org.testng.annotations.Test;

@TestFeature(
        name = "TestCase One",
        description = "First test"
)
public class TestOne extends QtafTestNGContext {

    @Test(testName = "Test Success", description = "This test should pass")
    public void testSuccess() {
        assertEquals(2 * 2, 4);
    }

    @Test(testName = "Test Failure", description = "This test should fail")
    public void testFailure() {
        assertEquals(2 * 2, 3);
    }
}
```

## Run tests

You can run the tests in two ways. In the first case, you can run the tests via the command line with the command `mvn clean test`. In our example, one test should succeed and the second test should fail. The output on the command line should end with the following text:

```
Results :

Failed tests:   testFailure(org.acme.tests.TestOne): expected [3] but found [4]

Tests run: 2, Failures: 1, Errors: 0, Skipped: 0

[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  15.570 s
[INFO] Finished at: 2023-01-01T11:04:36+01:00
[INFO] ------------------------------------------------------------------------
```

The second option is to run tests using the IntelliJ IDE. To do this, click on the green triangles next to the test methods in the `TestOne` class to run individual tests or on the green triangle next to the `TestOne` class itself and then click on Run test in the menu that opens to run all tests.

You will now see the following things: New directories and files have been created in your project. A new file named `qtaf.json` has been created in the resource directory. Within this file you can define parameters for the test execution.

A new directory called `logs` has also been created. In this directory, you can now observe that for each test run, a subdirectory is created that contains information about the test run.

### Create a Selenium test case

QTAF has been developed with a particular focus on web application testing and therefore offers special support for Selenium test cases. The Selenium library has already been installed by including QTAF as a dependency in your Maven project. To create a new Selenium test case, we proceed as in the example shown earlier. First we create a test class called `SeleniumTest` and let this class inherit from `QtafTestNGContext`. Now we again create a method within this class and provide it again with the annotation `@Test`from TestNG.

The class `QtafTestNGContext` provides us with the `driver` object, with which we can control our browser. The `driver`object is an ordinary Selenium web driver object, which we can work with as usual from other Selenium projects. The documentation of the Selenium driver for Java including a small example can be found on the following website: <a href="https://www.selenium.dev/documentation/" target="_blank">Selenium Documentation</a>

We would now like to look at how we would write the test case described in the Selenium documentation using QTAF. The Selenium test case without QTAF looks like this:


```java
import org.testng.Assert;
import org.testng.annotations.Test;

public class HelloSeleniumTest {
    By headlineSelector = By.cssSelector("h1.d-1");

    @Test(
      testName = "Open browser and visit selenium documentation",
      description = "Open the browser and go to the selenium documentation website"
    )
    public void testBrowser() {
        // Instatiate WebDriver object
        WebDriver driver = new ChromeDriver();

        // Visit Selenium documentation
        driver.get("https://selenium.dev");

        // Extract headline text from website
        String headlineText = driver.findElement(headlineSelector).getText();
        Assert.assertEquals(headlineText, "Selenium automates browsers. That's it!");

        // Close the driver
        driver.quit();
    }
}
```

If we now use QTAF, our test case looks like this:

```java
import de.qytera.qtaf.core.config.annotations.TestFeature;
import de.qytera.qtaf.testng.context.QtafTestNGContext;
import org.testng.Assert;
import org.testng.annotations.Test;

@TestFeature(
        name = "SeleniumTest",
        description = "Our first Selenium test"
)
public class HelloSeleniumTest extends QtafTestNGContext {
    By headlineSelector = By.cssSelector("h1.d-1");

    @Test(
      testName = "Open browser and visit selenium documentation",
      description = "Open the browser and go to the selenium documentation website"
    )
    public void testBrowser() {
        // Visit Selenium documentation
        driver.get("https://selenium.dev");

        // Extract headline text from website
        // assertEquals($(headlineSelector).text(), "Selenium automates browsers. That's it!");
        assertEquals(driver.findElement(headlineSelector).getText(), "Selenium automates browsers. That's it!");
    }
}
```

We only need to do two things to convert an ordinary TestNG test case into a QTAF test case:

1. The class must be annotated with the `TestFeature` annotation, which is provided by the QTAF library.
2. Our class must inherit from `QtafTestNGContext`.

If we look at the code inside the method we notice two more things: The statements for instantiating and closing the webdriver have been removed. QTAF takes over these tasks for us and already provides us with the initialised driver object via the class attribute `driver`.

A QTAF test case is thus an ordinary TestNG test case that we have merely extended with an annotation and an inherited class. Thus, every TestNG test case can also be converted into a QTAF test case.

### Divide test cases into test steps and page objects

Now that we have created our first test case we can move on to restructuring our test case. In our test case we have carried out two main steps: First, we called the desired page in the browser and then we extracted the text of a web element from the page using a selector. Then we checked whether this text corresponds to the text we wanted. Some of these test steps might also be of interest in other test cases, especially calling the website using `driver.get()` might occur more often in our test cases. Therefore, it makes sense to outsource these test steps to their own methods. First, we could create three methods within the test class into which we outsource the code of the respective test steps. In the test case, only these methods are called. Especially if the test steps become more complex in the course of a test project, it makes sense to split the code into methods. In our example, these test methods could look like this:

```java
package org.acme.tests;

import de.qytera.qtaf.core.config.annotations.TestFeature;
import de.qytera.qtaf.testng.context.QtafTestNGContext;
import org.testng.Assert;
import org.testng.annotations.Test;

@TestFeature(
        name = "SeleniumTest",
        description = "Our first Selenium test"
)
public class HelloSeleniumTest extends QtafTestNGContext {
    By headlineSelector = By.cssSelector("h1.display-1");

    @Test(
        testName = "Open browser and visit selenium documentation",
        description = "Open the browser and go to the selenium documentation website"
    )
    public void testBrowser() {
        openSite("https://selenium.dev");
        checkHeadline("Selenium automates browsers. That's it!");
    }

    public void openSite(String url) {
        // Visit Selenium documentation
        driver.get(url);
    }

    public void checkHeadline(String expectedText) {
        // Extract headline text from website
        assertEquals($(headlineSelector).text(), expectedText);
    }
}
```

The advantages of this code example are obvious: the code becomes more readable and by outsourcing test steps to separate methods, 
they can also be reused in other test cases. However, QTAF goes one step further and expects methods that represent test steps to 
be defined in separate classes. 
Thus, there are classes in which the methods contain test cases and other classes in which the methods only contain test steps. 
Instead of defining all test steps within a single class, it makes sense to bundle only those test steps within a class 
that all address a specific area of the website. Areas of the website can be, for example, 
a login form, a navigation bar or a specific menu. This also contributes to the maintainability of the code in larger projects.

#### Page Objects
Let's now look at how to define such a page object class in QTAF. We first create the package `org.acme.page_objects`, 
in which we will define our page object classes. The name of the package can also be chosen differently. 
In this package we now create the class `MainSitePO` that extends `QtafTestNGContext`. Within this class we define the methods `openSite` and `checkHeadline` 
as we had defined them before in the class `HelloSeleniumTest`. 

#### Step Annotations
Then we have to add annotations to our new class. 
We add the annotation `@Step` to each method that represents a test step. 
Within this annotation we can define the attributes name and description. 
The name and description of the test step will be used later in the reporting.

Our new page object class should look like this:

```java
package org.acme.page_objects;

import de.qytera.qtaf.core.guice.annotations.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import javax.inject.Singleton;


public class MainSitePO extends QtafTestNGContext {
    By headlineSelector = By.cssSelector("h1.display-1");

    @Step(
        name = "Open Site",
        description = "Open the selenium documentation website in the browser"
    )
    public void openSite(String url) {
        // Visit Selenium documentation
        driver.get(url);
    }

    @Step(
        name = "Check Headline",
        description = "Check if the headline of the site cintains a specific text"
    )
    public void checkHeadline(String expectedText) {
        // Extract headline text from website
        assertEquals($(headlineSelector).text(), expectedText);
    }
}
```
###load()
Now we need to instantiate this page object class in out test case. This can be done by the function `load` that is provided by the QTAF test context. This function accepts a class reference and creates a new instance of this class. It is important to instantiate the page object by calling the `load`and not using the `new`keyword, otherwise logging will not work for this page object. Internally QTAF injects code before and after each step method so that we can trace these functions. Our test case class, which now uses our page object class, then looks like this:

```java
package org.acme.tests;

import de.qytera.qtaf.core.config.annotations.TestFeature;
import de.qytera.qtaf.testng.context.QtafTestNGContext;
import org.testng.annotations.Test;

@TestFeature(
        name = "SeleniumTest",
        description = "Our first Selenium test"
)
public class HelloSeleniumTest extends QtafTestNGContext {
    @Test(
        testName = "Open browser and visit selenium documentation",
        description = "Open the browser and go to the selenium documentation website"
    )
    public void testBrowser() {
        // Instantiate page objects
        MainSitePO mainSitePO = load(MainSitePO.class)

        // Test case
        mainSitePO.openSite("https://selenium.dev");
        mainSitePO.checkHeadline("Selenium automates browsers. That's it!");
    }
}
```

Now we have divided our project into page objects and the test steps defined in them. We can now call the main method of `TestRunner` or execute the command `mvn clean test`. This will run our test cases.

## Create reports

QTAF offers you the possibility to automatically create reports from your test runs. In this example we show you two reporting formats integrated into the QTAF framework, one documenting the test execution by means of a JSON document and the other one creating an HTML report. The JSON document is interesting for the machine processing of the test results, the HTML report for the testers as a graphical presentation of the test results.

### Add QTAF HTML Report plugin
First, we need to add the QTAF HTML Report plugin as a dependency to our project. To do this, add the following dependency to the pom.xml file.

```xml
<dependency>
    <groupId>de.qytera</groupId>
    <artifactId>qtaf-html-report-plugin</artifactId>
    <version>${qtafVersion}</version>
</dependency>
```

Since the pom.xml has been changed, you should not forget to reload the dependencies.

### Activate HTML report
Furthermore, we have to activate the creation of the HTML report in the `qtaf.json` file.
The `qtaf.json` file can be found under `src/test/resources` in the project folder.
Make sure that the value `htmlReport.enabled` in the configuration file is set to `true`:

```json
  "htmlReport":{
    "enabled":true
  }
```

Then run the test cases again by executing the main method of the `TestRunner` class. You will then find the file `Report.html` in the logs directory, which contains the HTML report. You can open and display this in any browser.

In the same directory you will find the file `Report.json`, which contains the data of the test run as a JSON document.

You can find an example of an HTML report here: [QTAF HTML Report](../../assets/html_report/suite_crm/Report.html)

You can also find an example JSON report here: [QTAF JSON Report](../../assets/json_report/suite_crm/Report.json)

## Run test cases on different browsers

QTAF offers you the possibility to run test cases on different browsers. You can tell QTAF in three different ways which browser it should use to run the test cases. The only requirement is that the browsers themselves have already been installed by you on your computer. QTAF will automatically download the appropriate Selenium drivers for the desired browsers. You therefore do not need to worry about setting up the appropriate drivers.

**Option 1: Use the configuration file**

Change the value of the `driver.name` attribute in the `qtaf.json` file. Possible values include `chrome`, `firefox`, `edge`, `opera` and `ie`.

```json
  "driver":{
    "name": "chrome"
  }
```

Then run your test cases as usual. For example, if you have selected `firefox` as the value, the test cases will now be executed in the Firefox browser.

**Option 2: Use the command line**

QTAF test cases can also be executed via the command line. This is advantageous if you want to run test cases in a pipeline on different browsers, as in this case you do not have to make any changes to the code base. To run test cases from the command line you have to execute the command `mvn clean test`. Please note that the package name `org.acme` may differ from project to project. You can also pass the desired browser using the argument `-Ddriver.name`. For the Firefox browser, the command would look like this: `mvn clean test -Ddriver.name="firefox"`. Command line arguments always overwrite the values in the configuration file, i.e. if you have set the value `chrome` for `driver.name` in the configuration file, but pass the value `firefox` via the command line, your test cases will ultimately be executed in the Firefox browser.

**Option 3: Use environment variables**

As a third option, QTAF offers to set configuration parameters via environment variables. For example, if you want to test on the Edge browser, set the environment variable `DRIVER_NAME` to the value `edge`. In a Bash shell, you can also set environment variables directly before the actual command. This would look like this: `DRIVER_NAME=edge mvn clean test`. Environment variables also always overwrite the values in the `qtaf.json` file.

<hr>
<div style="display: flex; flex-direction: row; justify-content: space-between">
  <a href="https://www.qytera.de" target="_blank">Developed with love by Qytera, Germany</a>
  <span>|</span>
  <a href="https://www.qytera.de/testautomatisierung-workshop" target="_blank">Support & Service</a>
  <span>|</span>
  <a href="https://github.com/Qytera-Gmbh/QTAF" target="_blank">QTAF Repository</a>
  <span>|</span>
  <a href="https://www.qytera.de/kontakt" target="_blank">Contact</a><br>
</div>
