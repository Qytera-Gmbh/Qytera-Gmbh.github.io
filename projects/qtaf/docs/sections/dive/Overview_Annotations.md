# QTAF Annotations

This article shows which annotations QTAF provides.
Furthermore, all annotations provided by TestNG are supported.

---

## QTAF Annotations

QTAF makes it possible to quickly and easily name or describe test cases and more directly in the code by using the annotations provided.
This information allows for more detailed log files and reports.
In addition, some QTAF plug-ins also offer further annotations.

## General

### @Step

The annotation `@Step` is used for methods that represent a test step.

This annotation has the following attributes :

* `name`: Name of the step

* `description` : Description of the step

These attributes are used when generating log files and reports.

### @TestFeature

The annotation `@TestFeature` is used to annotate classes that contain test cases.

This annotation expects the following attributes:

* `name`: Name of the test feature

* `description`: Description  of the test feature

These attributes are used when generating log files and reports.

The following annotation can be used to describe a test feature and associated test cases in a class:
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
For a description of the `@Test` annotation, see also the section [TestNG Annotations](#testng-annotations).

## Plug-ins
QTAF can be extended with plug-ins.
Some of these plug-ins offer annotation.
More detailed information on the corresponding plug-ins can be found in their documentation.

### @TestRail
The annotation `@TestRail` can be used to describe a TestRail test case.

This annotation has the following the attributes:

* `caseId`: ID of the test case

* `runId`: ID of a test run. (Like a test plan ID)

These attributes are used when generating log files and reports.

### @XrayTest
The annotation `@XrayTest` can be used to configure documentation to test results in Xray.

This annotation has the following the attributes:

* `key`: Internal Xray test ID that can be used for uploading test execution results.

* `scenarioReport`: Indicates whether an HTML report should be added as evidence to this test. (default is false)

* `screenshots` : Indicates whether screenshots should be added as evidence to this test. (default is false)

These attributes are used when generating log files and reports.

---

## TestNG Annotations
All annotations provided by TestNG are supported by QTAF.
This includes `@Test`, `@Parameters`, `@BeforeSuite` etc.
A complete list of TestNG annotations can be found in the official [TestNG documentation](https://testng.org).


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
