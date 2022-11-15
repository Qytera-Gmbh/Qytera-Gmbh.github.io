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

In the logs directory you can now also observe that a JSON file is created for each test run, which contains information about the test run.

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