# QTAF Xray Plugin

One possibility to export and document test results is the tool "Xray" of Jira. In this article we show you how to create test cases in Xray, how to link your test cases written in Java with the test cases defined in Xray and how QTAf can automatically save the test results of your test runs in Xray.

## Create test cases in Xray

The first step is to create the definitions of our test cases in Xray. In our example, we will create three test case definitions called "QTAF-1", "QTAF-2" and "QTAF-3".

First you have to click on "Testing Board" in the left menu of Jira to get to the user interface of Xray. The following screenshot shows the testing board of our example project. Create the three test case definitions for our test cases here.

<img src="https://qytera-gmbh.github.io/img/qtaf/xray_plugin/xray_testing_board.png" />

Test steps must still be defined for each of the three tests. In the Xray user interface, these can be found in the "Test Details" section. In our example, we assume that the tests "QTAF-1", "QTAF-2" and "QTAF-3" have two, three and two steps respectively. The following picture shows the test case "QTAF-1" in Xray:

<img src="https://qytera-gmbh.github.io/img/qtaf/xray_plugin/xray_test_steps.png" />

## Qtaf and Xray

This section shows how the recorded information about the executed test cases and test steps can be sent automatically to Xray.

First we have to store the credentials for Xray in the configuration.json file. To do this, add the following section to this file:

```json
{
  ...
  "xray":{
    "enabled": true,
    "authentication":{
      "clientId": "<YOUR_CLIENT_ID>",
      "clientSecret": "<YOUR_CLIENT_SECRET>"
    }
  },
  ...
}
```

Tehn create three test cases and annotate each with all required annotations. To assign a test class to a test case in Xray, the attribute `name` of the annotation `@Test` must correspond to the name of the test case in Xray. The following example shows a test whose results are to be stored in Xray under the key "QTAF-1".

```java
@TestFeature(
        name = "DoGoogleSearch",
        description = "Perform a search for text 'Hello World'"
)
public class DoGoogleSearch extends GoogleTestContext {

    @Test(
            testName = "QTAF-1",
            description = "Type 'Hello World' and click search button",
            groups = {"Group 1", "Group 2"}
    )
    public void TestCaseGoogleSearch()
    {
        // test logic here
    }
}
```

In order to also document the test steps, methods must be called in the test that are provided with the annotation `@Step` of the Qtaf framework. In this example, we assume that there are two methods that are defined in a separate class called `GoogleFunctionsPage`.

```java
public class GoogleFunctions extends TestContext
{
    @Step(
            name = "Search value",
            description = "Search for a value"
    )
    public void doSearch(String searchValue) {
        driver.findElement(By.xpath(UsedObject.SearchInputXPath())).sendKeys(searchValue);
        driver.findElement(By.name(UsedObject.GoogleSearchButtonName())).click();
    }

    @Step(
            name = "Go to Google home page",
            description = "Navigate to the Google home page"
    )
    public void goToGoogleHome() {
        driver.get(UsedObject.GoogleHome());
    }
}
```

We then call these methods in the test case.

```java
@TestFeature(
        name = "DoGoogleSearch",
        description = "Perform a search for text 'Hello World'"
)
public class DoGoogleSearch extends GoogleTestContext {

    @Test(
            testName = "QTAF-1",
            description = "Type 'Hello World' and click search button"
    )
    public void TestCaseGoogleSearch()
    {
         // 1. Open Google
        googleFunctionPage.goToGoogleHome();

        // 2. Execute Search
        googleFunctionPage.doSearch("Hello World");
    }
}
```

Qtaf registers the call of these methods and logs the call in the background. Here, no IDs need to be defined for the test steps. Qtaf assigns the called methods in the order of the steps defined in Xray.

Now execute your test cases as usual. After the execution of your test cases is finished, QTAF will show you the following statement in the console:

```
15:22:25.717 [main] INFO  de.qytera.qtaf.core - Uploading Xray results ...
15:22:49.260 [main] INFO  de.qytera.qtaf.core - Uploaded test execution. Key is QTAF-846
```

This means that the upload to Xray was successful and can now be viewed in Jira under the key "QTAF-846".

<hr>
<a href="https://github.com/Qytera-Gmbh/QTAF" target="_blank">QTAF Repository</a><br>
<a href="https://www.qytera.de" target="_blank">Developed with love by Qytera, Germany</a>