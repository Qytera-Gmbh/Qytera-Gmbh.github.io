# Create a Cucumber Project with QTAF

This article describes how to set up a QTAF Cucumber project. It is assumed that you have already set up a Maven project using IntelliJ and have included QTAF as a dependency. How this can be done is described in the following article: <a href="/articles/New_QTAF_Project.html" target="_blank">QTAF - Project Creation</a>.<br />
Also you can use our <a href="/articles/QTAFCucumberProject" target="_blank">QTAF with Cucumber</a> example project to try out.

## Create folder and package structure

The Java code of the Maven project is stored in the subfolder `src/main/java`, the resources (all other required files) in the subfolder `src/main/resources`.

Within the Java directory we create the package `org.acme`, because in this example we are creating a project for the fictitious company Acme GmbH. Furthermore, we create the folder `features` in the `resources` directory, which will later contain our feature files.

## Creating test cases

To create test cases using Qtaf with Cucumber, we first need to create a so-called test runner. This test runner is a class that provides information about the location of the Cucumber feature files and the step definitions by means of an annotation.

In the following example we assume that our source code is organised in the package `org.acme`. We create a new class in this package called `TestRunner`. This class must have the following properties:

1. The class will have the annotation `@CucumberOptions`. This annotation provides information on where to find the feature files `(features = {"..."})`, where to find the corresponding step definitions `(glue = {"..."})`, which tag (not) to run `(tags = "...")` and which Cucumber plugin to use to create the reports `(plugin = {"..."})`.
2. The `TestRunner` class must inherit from the CucumberQtafTestContext class.
3. The `TestRunner` class must contain a method that is annotated with the `@DataProvider` annotation of the TestNG framework and returns a list of scenarios, which is done by calling `super.scenarios()`.

The following code shows a sample implementation of this class:

```java
package org.acme;

import de.qytera.qtaf.cucumber.context.QtafTestNGCucumberContext;
import io.cucumber.testng.CucumberOptions;
import org.testng.annotations.DataProvider;

/**
 * Main class to execute Cucumber Tests
 */
@CucumberOptions(
        features = {"src/main/resources/features"},
        glue = {"org.acme.stepdefs"},
        tags = "",
        plugin = {"pretty"}
)
public class TestRunner extends QtafTestNGCucumberContext {
    @Override
    @DataProvider(parallel = true)
    public Object[][] scenarios() {
        return super.scenarios();
    }
}
```

## Creating a scenario listener

In order for QTAF to be able to create log files for the executed test cases, you have to create another class in the folder you specified in the `@CucumberOptions` annotation in the `glue` attribute. In this case, this would be the folder `org.acme.stepdefs`. 

In this folder, create a class called `TestListener` that inherits from the QTAF framework class `QtafCucumberHooks` and add the following methods to it:

```java
package org.acme.stefdefs;

import de.qytera.qtaf.cucumber.listener.QtafCucumberHooks;
import io.cucumber.java.*;

/**
 * This class listens to cucumber hooks and produces logs
 */
public class TestListener extends QtafCucumberHooks {
    @Before
    public void onBeforeScenario(Scenario scenario) {
        beforeScenario(scenario);
    }

    @After
    public void onAfterScenario(Scenario scenario) {
        afterScenario(scenario);
    }

    @BeforeStep
    public void onBeforeStep(Scenario scenario) {
        beforeStep(scenario);
    }

    @AfterStep
    public void onAfterStep(Scenario scenario) {
        afterStep(scenario);
    }
}
```

Cucumber will automatically recognise this class as a listener class through the annotations `@Before`, `@BeforeStep`, `@After` and `@AfterStep`. Within this methods, we let the QTAF framework perform the further steps for logging by calling these methods.

## Creating feature files

In the `TestRunner` class we have specified that the feature files are to be found in the `src/main/resources/features` directory relative to the root directory of our project. In this folder we now place our first feature file with the name `GoogleSearch`.feature. The name of the file can be freely chosen. As long as the file ends with `.feature` and is located in the directory that we specified with the annotation `@CucumberOptions`, Cucumber is able to find this file and interpret it as a test case.

Now we write the following content into our feature file:

```gherkin
# Test the Qytera search function
Feature: Qytera Search
  
  # This step will run before each scenario
  Background: The browser will be launched
    Given Launch the browser

  # Test case 1
  @TestName:QTAF-1
  Scenario: Search for Cucumber in Qytera
    Then Enter "Cucumber" in the search text box
    And Select the first result
```

## Creating Step Definitions

Step definitions are Java classes that contain the code to be executed when a step is called in a feature file. For example, if we have defined the step `Then Enter "Cucumber" in the search text box` in our feature file, Cucumber does not yet know what to do when it sees this statement. To tell Cucumber this, we create a new class called `StepDefs` in the package `org.acme.stepdefs`. We have previously defined the package name via the annotation `@CucumberOptions`. Furthermore, classes that contain step definitions must inherit from the class `QtafTestNGContext`.

In the following example, all steps are defined that are called in our feature file. Among other things, this class provides the attribute `driver`, which provides an instance of a web driver.

```java
package org.acme.stepdefs;

import de.qytera.qtaf.core.context.QtafTestContext;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;

public class StepDef extends QtafTestContext {

    @Given("Launch the browser")
    public void launchTheBrowser() {
        driver.get("https://www.qytera.de");
    }

    @When("Hit Qytera on your browser")
    public void hitQytera() {
        Assert.assertEquals(3, 3);
    }

    @Then("Enter {string} in the search text box.")
    public void enterStringInSearchBox(String string) {
        System.out.println("Search box: " + string);
    }

    @Then("Select the first result.")
    public void selectTheFirstResult() {
        Assert.assertEquals(1, 1);
    }
}
```

## Run program

Now the project is ready so that we can run it for the first time. To do this, we click on an icon with a green file to the left of the name of the main class in IntelliJ. A dialogue then opens where we click on Run `CucumberRunner`. This first run allows QTAF to create further required directories and files on its own.

<img src="https://qytera-gmbh.github.io/img/cucumber/cucumber_testrunner_exec.jpg" />

A browser will open for a short time. However, since we have not yet created any test cases, it will close again after a short time. Furthermore, a configuration file called `configuration.json` is created in the resource directory, as well as the folder `logs`, in which you can already see log files for the test run we have just carried out.

The project is now ready for the creation of test cases.

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
