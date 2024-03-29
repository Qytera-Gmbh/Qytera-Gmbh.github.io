# Setup QTAF in VSCode

Before you read this article you should be familiar with the QTAF framework. You can read [this article](../steps/New_QTAF_Project.md) if you want to understand the Java code which is shown here.

Front-end developers mostly use VSCode IDE for developing front-end applications, so it is of great importance that they can also start back-end projects with VSCode.

To test the QTAF implementation under VSCode, Java 17 should first be installed on the system, there are several tutorials on this. The following instructions show how to install Java 17 on different operating systems:

<a href="https://www3.cs.stonybrook.edu/~amione/CSE114_Course/materials/resources/InstallingJava17.pdf" target="_blank">Install Java 17</a>

Now check if the installation was sucecssful with the following command:

```bash
$ java --version
```

Now open VSCode and install the extension "Extension Pack for Java".

<video controls>
  <source src="../../../assets/video/vscode/extension_pack_for_java_installation.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

Furthermore you need to install the extension "Maven for Java".

<video controls>
  <source src="../../../assets/video/vscode/maven_for_java_installation.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

After installing the necessary extensions, a view "JAVA PROJECTS" with the project structure is activated under Explorer.

<img src="../../../assets/images/vscode/vscode_test_cases.png" />

To run tests, the Java Pack Extension adds the button "Run/Debug" next to the test classes, as in classic Java IDEs (Eclips or Intellij).

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
