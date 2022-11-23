# Local Setup of QTAF

In this article we describe how QTAF can downloaded and installed locally. This should be done if you want to use beta verisons of QTAF, develop own plugins or add modifications of the code.

We assume that you have already cloned the QTAF source code from the GitHub repository to your machine. Otherwise navigate to a directory of your choice and execute the following command: 

```bash
$ git clone https://github.com/Qytera-Gmbh/QTAF
```

You can then start editing the QTAF source code.

If you would like to try out your changes locally first, you can proceed as follows.

1. Set a new version number for QTAF. This version number should contain the addition "LOCAL" to make it clear that it is only a locally developed version that is not to be deployed to the central repository. For example, you could assign the version number "LOCAL-2022-11-14-001". Since the QTAF project is divided into several modules and each of these modules has its own POM file, it can be tedious and error-prone to update the version number of each POM file. Instead, you can run the command `mvn versions:set "-DnewVersion=<version>"` to update the version numbers of all modules.

2. Then run the command `mvn clean install` to install the current version of QTAF locally. This may take some time as all test cases will also be executed. If you want to skip the test cases you can append the option `-DskipTests=true` to the command.

3. After the installation has been completed, you can integrate the new, local QTAF version in other projects via the POM file.

```xml
<dependency>
    <groupId>de.qytera</groupId>
    <artifactId>qtaf-core</artifactId>
    <version>LOCAL-2022-11-14-001</version>
</dependency>
```

For example, use demo projects such as the SuiteCRM demo project to test the changes to the QTAF framework and their effects.