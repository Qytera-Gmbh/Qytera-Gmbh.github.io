# How to create a new QTAF project

This article shows how a new project can be set up using the QTAF framework. First, we will show you how to install QTAF using Maven. Then we will create our first test case using QTAF.

# Set up a new project with IntelliJ

To create a new project, we use the IntelliJ IDE from Jetbrains. Here we navigate in the menu to `File > New > Project` and then select `Maven` in the left selection menu and click on `Next`. 

We are then asked for a name for the project. This can be chosen freely, but in this example we use the name "QtafProject". It is recommended to also specify the GroupId of the project. This is an identifier for the creator of the project. It is common to choose the company's domain for this, but starting with the country- or organisation-specific ending of the domain. For a company domain "acme.org", one would choose the GroupId "org.acme" according to this standard. The GroupId can be found in the sub-item Artifact Coordinates. Then we click on Finish. The new project should now have been created in the folder `~\IdeaProjects\QtafProject`, where `~` is a placeholder for the root directory of the currently logged in user.

In the root directory of the project we see the file `pom.xml`. This file is used to configure Maven projects, i.e. to load external libraries, to control the build process, etc. The file should look like this:

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

This file can be used to manage plug-ins and extensions of the project. Now we only have to include QTAF as a dependency in the project. To do this, add the following code to pom.xml:

```xml
<dependency>
    <groupId>de.qytera</groupId>
    <artifactId>qtaf-core</artifactId>
    <version>0.0.1</version>
    <scope>test</scope>
</dependency>
```

Replace the version number with the latest version of QTAF. You can find this in the Central Maven Repository under the following link: <a href="https://mvnrepository.com/artifact/de.qytera/qtaf" target="_blank">QTAF Central Repository</a>

# Overview of the project structure

After creating the project, a file called `pom.xml` should have been created in the root directory of the project with the following content.

## Create TestRunner class
A TestRunner is a Java class that controls the execution of tests. At the same time, it takes over the initialisation of the QTAF project the first time a test execution is carried out.

Go to the Java package you specified in the `pom.xml` file for the attribute groupId. In the example from this article, this would be the package `org.acme`. Create a new class called `TestRunner` in this package and let this class inherit from the class `QtafTestNGRunner`.

```java
package org.acme;

import de.qytera.qtaf.testng.QtafTestNGRunner;

public class TestRunner extends QtafTestNGRunner {

}
```

The class `QtafTestNGRunner` has a main method so that it is executable. The class `TestRunner` just created inherits this method from its parent class and is therefore also executable. In IntelliJ, you can click on the small green tick to the left of the class name to execute the main method of the class (see image).

When executing the class, QTAF checks for the existence of various files and folders that are needed by QTAF. If these have not yet been created, they will be created automatically. Among other things, a configuration file is created in the folder `./src/main/resources/en/qytera/qtaf/core/config` when the TestRunner class is executed. You can use this configuration file to control and parameterise the test execution of QTAF. Furthermore, the folder `./logs` is created in which you can find the reports of the individual test executions. After the first run of TestRunner, QTAF is already set up and you can start creating test cases.

## Create test cases

### Create first test case

Now the project should be initialised. We can now turn our attention to creating the first test case. 

Create a class `TestOne` in this directory with the following content:

```java
import de.qytera.qtaf.core.config.annotations.TestFeature;
import de.qytera.qtaf.testng.context.QtafTestNGContext;
import org.testng.Assert;
import org.testng.annotations.Test;

@TestFeature(
        name = "TestCase One",
        description = "First test"
)
public class TestOne extends QtafTestNGContext {

    @Test(testName = "Test Success", description = "This test should pass")
    public void testSuccess() {
        Assert.assertEquals(2 * 2, 4);
    }

    @Test(testName = "Test Failure", description = "This test should fail")
    public void testFailure() {
        Assert.assertEquals(2 * 2, 3);
    }
}
```

### Run tests

You can run the tests in two ways. In the first case, you can run the tests via the command line with the command mvn exec:java -Dexec.mainClass="org.acme.TestRunner". In our example, one test should succeed and the second test should fail. The output on the command line should end with the following text:

```
Results :

Failed tests:   testFailure(TestOne): expected [3] but found [4]

Tests run: 2, Failures: 1, Errors: 0, Skipped: 0

[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  15.570 s
[INFO] Finished at: 2020-11-05T11:04:36+01:00
[INFO] ------------------------------------------------------------------------
```

The second option is to run tests using the IntelliJ IDE. To do this, click on the green triangles next to the test methods in the TestOne class to run individual tests or on the green triangle next to the TestRunner class to run all tests and then click on Run test in the menu that opens. 

In the logs directory you can now also observe that a JSON file is created for each test run, which contains information about the test run. Furthermore, you will see a new file called `configuration.json` in the subdirectory `de/qytera/qtaf/core/config` of the resource folder of your Maven project. Within this file you can define parameters for the test execution. Within this file we now need to edit the following block:


```json
  "tests":{
    "suite":{
      "name":""
    },
    "package":""
  }
```

Now enter for the value "package" the name of the package in which we will define our test cases. In our example, this will be the package `org.acme.tests`. The block shown should then look like this:

```json
  "tests":{
    "suite":{
      "name":""
    },
    "package":"org.acme.tests"
  }
```

The `configuration.json` file contains many more values, but these are covered in a separate article.

# Create a Selenium test case

QTAF has been developed with a particular focus on web application testing and therefore offers special support for Selenium test cases. The Selenium library has already been installed by including QTAF as a dependency in your Maven project. To create a new Selenium test case, we proceed as in the example shown earlier. First we create a test class called `SeleniumTest` and let this class inherit from `QtafTestNGContext`. Now we again create a method within this class and provide it again with the annotation `@Test`from TestNG.

The class `QtafTestNGContext` provides us with the `driver` object, with which we can control our browser. The `driver`object is an ordinary Selenium web driver object, which we can work with as usual from other Selenium projects. The documentation of the Selenium driver for Java including a small example can be found on the following website: <a href="https://www.selenium.dev/documentation/" target="_blank">Selenium Documentation</a>

We would now like to look at how we would write the test case described in the Selenium documentation using QTAF. The Selenium test case without QTAF looks like this:


```java
import org.testng.Assert;
import org.testng.annotations.Test;

public class HelloSeleniumTest {
    String headlineSelector = "div.td-content h1";

    @Test(
      testName = "Open browser and visit selenium documentation",
      description = "Open the browser and go to the selenium documentation website"
    )   
    public testBrowser() {
        // Instatiate WebDriver object
        WebDriver driver = new ChromeDriver();

        // Visit Selenium documentation
        driver.get("https://selenium.dev");
        
        // Extract headline text from website
        String headlineText = driver.findElement(By.cssSelector(headlineSelector)),getText();
        Assert.assertEquals(headlineText, "The Selenium Browser Automation Project");

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
    String headlineSelector = "div.td-content h1";

    @Test(
      testName = "Open browser and visit selenium documentation",
      description = "Open the browser and go to the selenium documentation website"
    )   
    public testBrowser() {
        // Visit Selenium documentation
        driver.get("https://selenium.dev");
        
        // Extract headline text from website
        String headlineText = driver.findElement(By.cssSelector(headlineSelector)),getText();
        Assert.assertEquals(headlineText, "The Selenium Browser Automation Project");
    }
}
```

We only need to do two things to convert an ordinary TestNG test case into a QTAF test case:

1. The class must be annotated with the `TestFeature` annotation, which is provided by the QTAF library.
2. Our class must inherit from `QtafTestNGContext`.

If we look at the code inside the method we notice two more things: The statements for instantiating and closing the webdriver have been removed. QTAF takes over these tasks for us and already provides us with the initialised driver object via the class attribute `driver`.

A QTAF test case is thus an ordinary TestNG test case that we have merely extended with an annotation and an inherited class. Thus, every TestNG test case can also be converted into a QTAF test case.

# Divide test cases into test steps and page objects

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
    String headlineSelector = "div.td-content h1";

    @Test(
      testName = "Open browser and visit selenium documentation",
      description = "Open the browser and go to the selenium documentation website"
    )   
    public testBrowser() {
        openSite("https://selenium.dev");
        checkHeadline("The Selenium Browser Automation Project");
    }
    
    public void openSite(String url) {
        // Visit Selenium documentation
        driver.get(url);
    }
    
    public void checkHeadline(String expectedText) {
        // Extract headline text from website
        String headlineText = driver.findElement(By.cssSelector(headlineSelector)),getText();
        Assert.assertEquals(headlineText, "The Selenium Browser Automation Project");
    }
}
```

The advantages of this code example are obvious: the code becomes more readable and by outsourcing test steps to separate methods, they can also be reused in other test cases. However, QTAF goes one step further and expects methods that represent test steps to be defined in separate classes. Thus, there are classes in which the methods contain test cases and other classes in which the methods only contain test steps. Instead of defining all test steps within a single class, it makes sense to bundle only those test steps within a class that all address a specific area of the website. Areas of the website can be, for example, a login form, a navigation bar or a specific menu. This also contributes to the maintainability of the code in larger projects.

Let's now look at how to define such a page object class in QTAF. We first create the package `org.acme.page_objects`, in which we will define our page object classes. The name of the package can also be chosen differently. In this package we now create the class `MainSitePO`. Within this class we define the methods `openSite` and `checkHeadline` as we had defined them before in the class `HelloSeleniumTest`. Then we have to add annotations to our new class. First, we add the annotation `@Singleton` to the class. This ensures that only one object is created from this class at runtime. Next, we add the annotation `@Step` to each method that represents a test step. Within this annotation we can define the attributes name and description. The name and description of the test step will be used later in the reporting.

Our new page object class should look like this:

```java
package org.acme.page_objects;

import de.qytera.qtaf.core.guice.annotations.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import javax.inject.Singleton;


@Singleton
public class MainSitePO extends QtafTestNGContext {
    String headlineSelector = "div.td-content h1";
    
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
        String headlineText = driver.findElement(By.cssSelector(headlineSelector)),getText();
        Assert.assertEquals(headlineText, "The Selenium Browser Automation Project");
    }
}
```

Now we only have to import our new page object class into our test case class. Until now, our test case class inherited from the `QtafTestNGContext` class from the QTAF framework, which, for example, provides a pre-configured Selenium driver via the `driver` attribute. Since we have now created page object classes, it makes sense to create a new class called `TestContext`, let it inherit from `QtafTestNGContext` and then instantiate our page objects here. The test classes then inherit from our own test context class and thus inherit the Selenium driver and our own page objects.

The test context class could look like this:

```java
package org.acme;

import de.qytera.qtaf.testng.context.QtafTestNGContext;
import org.acme.page_objects.*;

import javax.inject.Inject;


public class TestContext extends QtafTestNGContext {

    @Inject
    protected MainSitePO mainSitePO;
}
```

Our test case class, which now inherits from TestContext, then looks like this:

```java
package org.acme.tests;

import de.qytera.qtaf.core.config.annotations.TestFeature;
import de.qytera.qtaf.testng.context.QtafTestNGContext;
import org.testng.Assert;
import org.testng.annotations.Test;
import org.acme.TestContext;

@TestFeature(
        name = "SeleniumTest",
        description = "Our first Selenium test"
)
public class HelloSeleniumTest extends TestContext {
    String headlineSelector = "div.td-content h1";

    @Test(
      testName = "Open browser and visit selenium documentation",
      description = "Open the browser and go to the selenium documentation website"
    )   
    public testBrowser() {
        mainSitePO.openSite("https://selenium.dev");
        mainSitePO.checkHeadline("The Selenium Browser Automation Project");
    }
}
```

Now we have divided our project into page objects and the test steps defined in them. We can now call the main method of `TestRunner` and execute our test cases.

# Create reports

QTAF offers you the possibility to automatically create reports from your test runs. In this example we show you two reporting formats integrated into the QTAF framework, one documenting the test execution by means of a JSON document and the other one creating an HTML report. The JSON document is interesting for the machine processing of the test results, the HTML report for the testers as a graphical presentation of the test results.

First we have to activate the creation of the HTML report in the configuration file. Make sure that the value `htmlReport.enabled` in the configuration file is set to `true`:

```json
  "htmlReport":{
    "enabled":true
  }
```

Then run the test cases again by executing the main method of the `TestRunner` class. You will then find the file `Report.html` in the logs directory, which contains the HTML report. You can open and display this in any browser.

Furthermore, in the same directory you will find the file `Report.json`, which contains the data of the test run as a JSON document.

You can find an example of an HTML report here: <a href="https://qytera-gmbh.github.io/html_report/suite_crm/Report.html" target="_blank">QTAF HTML Report</a>

You can also find an example JSON report here: <a href="https://qytera-gmbh.github.io/json_report/suite_crm/Report.json" target="_blank">QTAF JSON Report</a>

# Run test cases on different browsers

QTAF offers you the possibility to run test cases on different browsers. You can tell QTAF in three different ways which browser it should use to run the test cases. The only requirement is that the browsers themselves have already been installed by you on your computer. QTAF will automatically download the appropriate Selenium drivers for the desired browsers. You therefore do not need to worry about setting up the appropriate drivers.

**Option 1: Use the configuration file**

Change the value of the `driver.name` attribute in the `configuration.json` file. Possible values include `chrome`, `firefox`, `edge`, `opera` and `ie`.

```json
  "driver":{
    "name": "chrome"
  }
```

Then run your test cases as usual. For example, if you have selected `firefox` as the value, the test cases will now be executed in the Firefox browser.

**Option 2: Use the command line**

QTAF test cases can also be executed via the command line. This is advantageous if you want to run test cases in a pipeline on different browsers, as in this case you do not have to make any changes to the code base. To run test cases from the command line you have to execute the command `mvn exec:java -Dexec.mainClass="org.acme.TestRunner"`. Please note that the package name `org.acme` may differ from project to project. You can also pass the desired browser using the argument `-Ddriver.name`. For the Firefox browser, the command would look like this: `mvn exec:java -Dexec.mainClass="org.acme.TestRunner" -Ddriver.name="firefox"`. Command line arguments always overwrite the values in the configuration file, i.e. if you have set the value `chrome` for `driver.name` in the configuration file, but pass the value `firefox` via the command line, your test cases will ultimately be executed in the Firefox browser.

**Option 3: Use environment variables**

As a third option, QTAF offers to set configuration parameters via environment variables. For example, if you want to test on the Edge browser, set the environment variable `DRIVER_NAME` to the value `edge`. In a Bash shell, you can also set environment variables directly before the actual command. This would look like this: `DRIVER_NAME=edge mvn exec:java -Dexec.mainClass="org.acme.TestRunner"`. Environment variables also always overwrite the values in the `configuration.json` file.