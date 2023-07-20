# QTAF Annotations

In this article we show you which annotations QTAF provides.

## Test cases


### @TestFeature

The annotation `@TestFeature` is used to annotate classes that contain test cases. `@TestFeature` expects the attributes `name` and `description`. This annotation is used to describe the test cases defined in the class.

```java
import de.qytera.qtaf.core.config.annotations.TestFeature;
import org.testng.annotations.Test;

@TestFeature(
        name = "Test Feature One",
        description = "This is the first test feature"
)
public class TestFeatureOne extends TestContext {

    @Test(testName = "T1", description = "First Test Case")
    public void testOne() {
        // ...
    }
}
```

### @Test

The annotation `@Test` comes from the TestNG framework and can be used as usual to annotate methods that contain test cases. Several test cases can be defined in a class. The test cases that are defined within a class should have a similar context, otherwise the test cases should be divided among several classes.

## Page Objects

### @Singleton

The annotation `@Singleton` comes from the Java library and is used for page object classes. Since QTAF instantiates these classes by means of dependency injection, we have to tell QTAF that we want to create only one instance of this class at runtime. Otherwise, endless loops can occur if page objects have mutual relationships to each other and keep trying to instantiate each other.

```java
import de.qytera.qtaf.core.guice.annotations.Step;
import jakarta.inject.Singleton;

@Singleton
public class CalendarPage extends TestContext {
    String moduleButtonSelector = "#moduleTab_Calendar";

    @Step(name = "Click contact module button", description = "Click contact module button")
    public void clickMeetingsModuleButton() {
        WebElement menu = driver.findElement(By.cssSelector(moduleButtonSelector));
        menu.click();
    }

}
```

### @Step

The annotation `@Step` comes from the QTAF framework and is used for methods that represent a test step. This annotation has the attributes `name` and `description`, with which the test step can be given a name and a description. These attributes are used when generating log files and reports.



## Test context

### @Inject

In QTAF, the page object classes are instantiated in the `TestContext` class. To prevent them from being instantiated more than once and to avoid infinite loops during instantiation, page object classes are provided with the annotation `@Singleton`. In the TestContext classes, we add attributes that are of the type of the respective page object class and provide these attributes with the annotation `@Inject`. This causes QTAF to automatically take care of instantiating these classes. We do not have to call a constructor.

```java
import jakarta.inject.Inject;

public class TestContext extends QtafTestNGContext {

    @Inject
    protected Navigator navigator;

    @Inject
    protected LoginFormPO loginForm;

    @Inject
    protected TopNavbar topNavbar;
}
```

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
