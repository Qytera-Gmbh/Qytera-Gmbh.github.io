# Setup new QTAF Project with IntelliJ and Maven

To create a new project, we use the IntelliJ IDE from Jetbrains. Here we navigate in the menu to `File > New > Project` and then select `Maven` in the left selection menu and click on Next.

<img src="https://qytera-gmbh.github.io/img/intellij/intellij_new_maven_project.png" />

We are then asked for a name for the project. This can be chosen freely, but in this example we use the name "QtafProject". It is recommended to also specify the GroupId of the project. This is an identifier for the creator of the project. It is common to choose the company's domain for this, but starting with the country- or organisation-specific ending of the domain. For a company domain "acme.org", one would choose the GroupId "org.acme" according to this standard. The GroupId can be found in the sub-item `Artifact Coordinates`. Then we click on `Finish`. The new project should now have been created in the folder `~\IdeaProjects\QtafProject`, where `~` is a placeholder for the root directory of the currently logged in user.

<img src="https://qytera-gmbh.github.io/img/intellij/intellij_project_name.png" />

In the root directory of the project we see the file pom.xml. This file is used to configure Maven projects, i.e. to load external libraries, to control the build process, etc.

The following additions should be entered in the file:

```xml
<project>    
    <!-- ... -->
    
    <!-- Here we define the Java version of the project -->
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>

    <!-- Here you can add external Java libraries to your project -->
    <dependencies>

    </dependencies>

    <!-- Everything is configured here for the build process -->
    <build>
        
        <!-- Path under which Java should search for files (resources) -->
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>true</filtering>
            </resource>
        </resources>

        <!-- Maven plugins that extend the basic functionality of Maven -->
        <plugins>
            <!-- Plugin for creating JAR files -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <classpathPrefix>/</classpathPrefix>
                            <!-- Test runner class that runs all tests -->
                            <mainClass>de.qytera.suite_crm.TestRunner</mainClass>
                        </manifest>
                    </archive>
                    <finalName>app</finalName>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

<hr>
<a href="https://github.com/Qytera-Gmbh/QTAF" target="_blank">QTAF Repository</a><br>
<a href="https://www.qytera.de" target="_blank">Developed with love by Qytera, Germany</a>