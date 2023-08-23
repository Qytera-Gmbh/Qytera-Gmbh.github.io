# Use QTAF with Groovy

QTAF is written in Java, but can also be used with Groovy, as Java and Groovy compile to Bytecode for the same runtime. For creating a new QTAF project with Groovy you can choose between Maven and Gradle as a build system. In this article we will show you for both systems how you can setup a new QTAF project.

## New QTAF Groovy project using Maven

Create a new project with IntelliJ or VSCode as you would create it when using Java. The `pom.xml` file should look like the following code sample.

There are two dependencies you have to add to `pom.xml`:
- <a href="https://mvnrepository.com/artifact/org.apache.groovy/groovy-all" href="blank_">groovy-all</a>
- <a href="https://mvnrepository.com/artifact/de.qytera/qtaf-core" target="_blank">qtaf-core</a>

Also you need to add the following Maven plugins:
- <a href="https://mvnrepository.com/artifact/org.codehaus.gmavenplus/gmavenplus-plugin" target="_blank">GMavenPlus Plugin</a>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>de.qytera.qtafgroovy</groupId>
    <artifactId>QtafGroovyMavenDemo</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <dependency>
            <groupId>org.apache.groovy</groupId>
            <artifactId>groovy-all</artifactId>
            <version>4.0.2</version>
            <type>pom</type>
        </dependency>
        <dependency>
            <groupId>de.qytera</groupId>
            <artifactId>qtaf-core</artifactId>
            <version>0.2.0</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.gmavenplus</groupId>
                <artifactId>gmavenplus-plugin</artifactId>
                <version>1.13.1</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>execute</goal>
                        </goals>
                    </execution>
                </executions>
                <dependencies>
                    <dependency>
                        <groupId>org.apache.groovy</groupId>
                        <artifactId>groovy</artifactId>
                        <version>4.0.2</version>
                        <scope>runtime</scope>
                    </dependency>
                </dependencies>
                <configuration>
                    <scripts>
                        <script>src/main/groovy/Main.groovy</script>
                    </scripts>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

</project>

```

## New QTAF Groovy project using Gradle

If you use Gradle the file `build.gradle` should have the following content:

```groovy
plugins {
    id 'groovy'
}

group = 'de.qytera.qtaf'
version = '1.0-SNAPSHOT'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.groovy:groovy:4.0.2'
    implementation 'de.qytera:qtaf-core:0.2.0'
}

test {
    useTestNG() { //Tells Gradle to use TestNG
        useDefaultListeners = true // Tells TestNG to execute its default reporting structure
        suites 'src/test/suite.xml' //location of our suite.xml
    }
}
```

## Creating page object classes

A page object class in Groovy looks like the following code snippet. Methods and classes <b>MUST</b> not be defined using the keyword `def`, otherwise logging will not work correctly.

```groovy
// src/test/<your-package-name>/SeleniumPage.groovy
import de.qytera.qtaf.core.guice.annotations.Step
import de.qytera.qtaf.testng.context.QtafTestNGContext

import static com.codeborne.selenide.Selenide.$

class SeleniumPage extends QtafTestNGContext {
    @Step(name = "Open site", description = "Open the website https://www.selenium.dev")
    void openSite() {
        driver.get("https://www.selenium.dev")
    }

    @Step(name = "Check headline", description = "Check that the headline matches the given text")
    void checkHeadline(String expectedText) {
        assertEquals($("h1").text(), expectedText)
    }
}
```

A test case in Groovy looks like the following sample. Also make surenot to use the keyword `def` for methods.

## Create test case classes
```groovy
// src/test/<your-package-name>/DemoTest.kt
import de.qytera.qtaf.core.config.annotations.TestFeature
import de.qytera.qtafgroovy.page_objects.SeleniumPage
import de.qytera.qtaf.testng.context.QtafTestNGContext
import org.testng.annotations.Test

@TestFeature(name = "Test Feature One", description = "Test Feature One")
class TestOne extends QtafTestNGContext {
    @Test(testName = "Test One", description = "Test One")
    void testOne() {
        def page = load(SeleniumPage)
        page.openSite()
        page.checkHeadline("Selenium automates browsers. That's it!")
    }
}
```

## Running the test cases

You can run the test cases with the same command as in Java: `mvn clean test` or `gradle test`.

The second option is to create a class that extends `TestRunner` and call its `main` method. Here is the code for this class:

```groovy
// src/test/<your-package-name>/Main.kt
class TestRunner extends QtafTestNGRunner {
}
```