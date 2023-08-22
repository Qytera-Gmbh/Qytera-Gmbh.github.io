# Data Providers

In this article you will learn how to implement data-driven test scenarios with QTAF.

In this tutorial, we will assume a test case that is supposed to fill out a form on a website. This test case could look like the example shown:

```java
@TestFeature(
        name = "Calls form",
        description = "Create call form"
)
public class CallsTest extends TestContext {
    @Test(testName = "CallsTest", description = "Calls Test")
    public void testCalls() {
        //Navigate to calls page
        navigator.goToRootPage();
        topNavbar.openMobileMenu();
        topNavbar.clickMobileCallsMenu();
        callsPage.clickCallsModuleButton();
        topBarCallsMenu.clickLogCallLink();
        // Fill call form
        createCallForm.fillSubjectField("Call subject");
        createCallForm.fillDurationField();
        createCallForm.fillDescriptionField("Call description");
        createCallPage.clickSaveButton();
        //Navigate to Home page
        topNavbar.openMobileMenu();
        topNavbar.clickHomeMenuFromNotHomePage();
    }
}
```

In this example, you see a test scenario called `CallsTest`, which calls various page objects to eventually fill out a form on a website and submit it afterwards. In this example, the page object `createCallForm` is responsible for filling out the form, which provides the methods `fillSubjectField` and `fillDescriptionField`, among others. Both methods accept a string as parameter.

In the example shown, the data we want to enter into the form is statically defined, i.e. no parameters can be passed to the test case from outside. However, if we want this test scenario to run multiple times and with different data, we need to make the following changes to our test scenario.

## Creating a Data Provider

First, within our Java class, which in our example is called `CallsTest`, we create a new method called `getCallsData`. You are free to choose the name of this method. This method returns a two-dimensional array of type `Object[][]`. Furthermore, this method must be annotated with the annotation `@DataProvider` of the TestNG framework. Also, assign an ID of this Data Provider using the `name` attribute in the DataProvider annotation. The DataProvider could look like this:

```java
import org.testng.annotations.*;

@TestFeature(
        name = "Calls form",
        description = "Create call form"
)
public class CallsTest extends TestContext {
    @DataProvider(name = "callsData")
    public Object[][] getCallsData() {
        return new Object[][]{
                {"Daily", "Daily conference"},
                {"Weekly", "Weekly conference"},
                {"Meeting John Doe", "Meeting with John Doe"},
                {"Meeting Jane Doe", "Meeting with Jane Doe"},
        };
    }

    // ...
}
```

Each test scenario that uses a Data Provider is executed once for each row of the data matrix. In our example, our data provider leifert a data matrix with four rows, accordingly the corresponding test scenarios are executed four times. The columns of the data matrix correspond to the number of parameters passed to the test scenarios. In our example, each execution of a test scenario would be passed two parameters of type String.

Now we still need to link our test scenario to our data provider. First, add the attribute `dataProvider` to the `@Test` annotation and give this attribute the same value as the attribute `name` of the `@DataProvider` annotation. Furthermore, add two parameters of type String to your Java method. Within the test scenario, replace all static parameters with the new dynamic parameters that the method takes. This may look like this:

Now you have successfully implemented a data-driven test case. Now run the test case as usual using the mvn clean test command.

```java
@Test(testName = "CallsTest", description = "Calls Test", dataProvider = "callsData")
public void testCalls(String subject, String description) {
    //Navigate to calls page
    navigator.goToRootPage();
    topNavbar.openMobileMenu();
    topNavbar.clickMobileCallsMenu();
    callsPage.clickCallsModuleButton();
    topBarCallsMenu.clickLogCallLink();
    // Fill call form
    createCallForm.fillSubjectField(subject);
    createCallForm.fillDurationField();
    createCallForm.fillDescriptionField(description);
    createCallPage.clickSaveButton();
    //Navigate to Home page
    topNavbar.openMobileMenu();
    topNavbar.clickHomeMenuFromNotHomePage();
}
```

You have now successfully implemented a data-driven test case. Now run the test case as usual using the `mvn clean test` command.