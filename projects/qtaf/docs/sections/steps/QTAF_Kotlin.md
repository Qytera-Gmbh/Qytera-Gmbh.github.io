# Use QTAF with Kotlin

QTAF is written in Java, but can also be used with Kotlin, as Java and Kotlin compile to Bytecode for the same runtime. For creating a new QTAF project with Kotlin you can choose between Maven and Gradle as a build system. In this article we will show you for both systems how you can setup a new QTAF project.

## New QTAF Kotlin project using Maven

Create a new project with IntelliJ or VSCode as you would create it when using Java. The `pom.xml` file should look like the following code sample.

There are two dependencies you have to add to `pom.xml`:
- <a href="https://mvnrepository.com/artifact/org.jetbrains.kotlin/kotlin-stdlib" href="blank_">kotlin-stdlib</a>
- <a href="https://mvnrepository.com/artifact/de.qytera/qtaf-core" target="_blank">qtaf-core</a>

Also you need to add the following Maven plugins:
- <a href="https://mvnrepository.com/artifact/org.jetbrains.kotlin/kotlin-maven-plugin" target="_blank">Kotlin Maven Plugin</a>
- <a href="https://mvnrepository.com/artifact/org.codehaus.mojo/exec-maven-plugin" target="_blank">Exec Maven Plugin</a>
- <a href="https://mvnrepository.com/artifact/org.apache.maven.plugins/maven-compiler-plugin" target="_blank">Apache maven Compiler Plugin</a>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns="http://maven.apache.org/POM/4.0.0"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <artifactId>KotlinQtafMavenDemo</artifactId>
    <groupId>org.example</groupId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>consoleApp</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <kotlin.code.style>official</kotlin.code.style>
        <kotlin.compiler.jvmTarget>17</kotlin.compiler.jvmTarget>
    </properties>

    <repositories>
        <repository>
            <id>mavenCentral</id>
            <url>https://repo1.maven.org/maven2/</url>
        </repository>
    </repositories>

    <build>
        <sourceDirectory>src/main/kotlin</sourceDirectory>
        <testSourceDirectory>src/test/kotlin</testSourceDirectory>
        <plugins>
            <plugin>
                <groupId>org.jetbrains.kotlin</groupId>
                <artifactId>kotlin-maven-plugin</artifactId>
                <version>1.9.0</version>
                <executions>
                    <execution>
                        <id>compile</id>
                        <phase>compile</phase>
                        <goals>
                            <goal>compile</goal>
                        </goals>
                    </execution>
                    <execution>
                        <id>test-compile</id>
                        <phase>test-compile</phase>
                        <goals>
                            <goal>test-compile</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>1.6.0</version>
                <configuration>
                    <mainClass>MainKt</mainClass>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <dependencies>
        <dependency>
            <groupId>org.jetbrains.kotlin</groupId>
            <artifactId>kotlin-stdlib</artifactId>
            <version>1.9.0</version>
        </dependency>
        <dependency>
            <groupId>de.qytera</groupId>
            <artifactId>qtaf-core</artifactId>
            <version>0.2.0</version>
        </dependency>

    </dependencies>
</project>
```

## New QTAF Kotlin project using Gradle

If you use Gradle the file `build.gradle.kts` should have the following content:

```kotlin
plugins {
    kotlin("jvm") version "1.8.0"
    application
}

group = "de.qytera"
version = "0.0.1"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))
    implementation("de.qytera:qtaf-core:0.2.0")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(17)
}

application {
    mainClass.set("MainKt")
}
```

## Creating page object classes

A page object class in Kotlin looks like the following code snippet. Methods and classes <b>MUST</b> be marked with the keyword `open`, otherwise logging will not work correctly, because internally these classes and methods are compile to final classes and final method. These methods cannot be intercepted by the framework we use for tracking calls to these methods.

```kotlin
// src/test/<your-package-name>/SeleniumPage.kt
import com.codeborne.selenide.Selenide.element
import de.qytera.qtaf.core.guice.annotations.Step
import de.qytera.qtaf.testng.context.QtafTestNGContext
import org.openqa.selenium.By


open class SeleniumPage : QtafTestNGContext() {
    private val headlineSelector: By = By.cssSelector("h1")

    @Step(name = "Open Website", description = "Navigate to the given URL")
    open fun openWebsite(url: String) {
        driver.get(url)
    }

    @Step(name = "Read headline", description = "Read the headline of the website")
    open fun checkHeadline(expectedText: String) {
        val givenText = element(headlineSelector).text()
        assertEquals(givenText, expectedText, "Expected headline to be $expectedText, but was $givenText")
    }
}
```

A test case in Kotlin looks like the following sample. Also make sure that your classes and methods are marked as `open`.

## Create test case classes
```kotlin
// src/test/<your-package-name>/DemoTest.kt
import de.qytera.kotlindemo.page_objects.SeleniumPage
import de.qytera.qtaf.core.config.annotations.TestFeature
import de.qytera.qtaf.testng.context.QtafTestNGContext
import org.testng.annotations.Test

@TestFeature(name = "Test One", description = "Test One")
open class DemoTest() : QtafTestNGContext() {
    @Test()
    open fun testOne() {
        val page: SeleniumPage = load(SeleniumPage::class.java)
        page.openWebsite("https://www.selenium.dev")
        page.checkHeadline("Selenium automates browsers. That's it!")
    }
}
```

## Running the test cases

You can run the test cases with the same command as in Java: `mvn clean test`.

The second option is to create a class that extends `TestRunner` and call its `main` method. Here is the code for this class:

```kotlin
// src/test/<your-package-name>/Main.kt
import de.qytera.qtaf.testng.QtafTestNGRunner

fun main(args: Array<String>) {
    QtafTestNGRunner.main(args)
}
```