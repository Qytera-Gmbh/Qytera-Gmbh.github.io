# Feature file synchronization

The plugin allows you to keep your local feature files in sync with the step definitions in Xray.

!!! development
    Please note that Cucumber support is still in an experimental development stage.
    You should probably expect Cucumber features to not work consistently for the time being.

## Feature file upload

<figure markdown>
  ![cucumber plugin workflow](../../assets/images/cypressXrayCucumberUploadLight.svg#only-light)
  ![cucumber plugin workflow](../../assets/images/cypressXrayCucumberUploadDark.svg#only-dark)
  <figcaption>Synchronize step definitions in Xray based on your local feature files.</figcaption>
</figure>

Uploading feature files is useful if the source of truth for test cases are local feature files in Cypress and Xray is only used for tracking execution results.
You can enable the upload using the [uploadFeatures](../configuration/cucumber.md#uploadfeatures) setting and by making sure that [feature file synchronization](../setup/installation.md#cucumber-support) is enabled.
!!! tip
    Don't forget to add tags to your scenarios to make [issue reuse](targetingExistingIssues.md#reuse-cucumber-test-issues) more comfortable.

    These tags are different for the cloud and server version.
    You can verify this by letting Xray export a [Cucumber test case to a feature file](https://docs.getxray.app/display/XRAY/Export+Cucumber+Features) followed by an inspection into the tags of the generated files.

    For Xray cloud, the tags must be provided in the following form:
    ```gherkin
    @TestName:CYP-129
    Scenario: Redirect by clicking
    ```
    For Xray server, they must be provided like this:
    ```gherkin
    @CYP-129
    Scenario: Redirect by clicking
    ```

    !!! warning
        Please be aware that there is no way of keeping Xray's issue summaries when synchronizing issues this way.
        All Xray issue summaries will be replaced with the scenarios' names on successful import.

???+ example

    In the following scenario, the [existing example](targetingExistingIssues.md#reuse-cucumber-test-issues) will be extended by an additional step.

    === "demo.spec.feature"

        ```gherkin hl_lines="8"
        Feature: Example page redirection

            @TestName:CYP-129
            Scenario: Redirect by clicking
                Given the example page
                When the link is clicked
                Then a redirect should occur
                And the test should fail
        ```

    === "demo.spec.js"

        ```js hl_lines="22-24"
        import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

        Given("the example page", function () {
            cy.visit("https://example.org");
        });

        When("the link is clicked", function () {
            // Intercept the click, since it unfortunately redirects to a http:// location
            // and causes Cypress to abort the execution.
            cy.intercept("GET", "https://www.iana.org/domains/example", (request) => {
                request.reply("link was clicked");
            }).as("redirect");
            cy.get("a").click();
        });

        Then("a redirect should occur", function () {
            cy.wait("@redirect").then((request) => {
                expect(request.response.body).to.eq("link was clicked");
            });
        });

        Then("the test should fail", function () {
            expect(true).to.be.false;
        });
        ```

    === "cypress.config.js"

        ```js hl_lines="12-15"
        import { addCucumberPreprocessorPlugin } from "@badeball/cypress-cucumber-preprocessor";
        import createEsbuildPlugin from "@badeball/cypress-cucumber-preprocessor/esbuild";
        import * as createBundler from "@bahmutov/cypress-esbuild-preprocessor";
        import { addXrayResultUpload, configureXrayPlugin, syncFeatureFile } from "cypress-xray-plugin";

        // ...
            async setupNodeEvents(on, config) {
                await configureXrayPlugin({
                    jira: {
                        projectKey: "CYP"
                    },
                    cucumber: {
                        featureFileExtension: ".feature",
                        uploadFeatures: true
                    }
                });
                await addCucumberPreprocessorPlugin(on, config, {
                    omitBeforeRunHandler: true,
                    omitAfterRunHandler: true,
                    omitBeforeSpecHandler: true,
                    omitAfterSpecHandler: true,
                    omitAfterScreenshotHandler: true,
                });
                await addXrayResultUpload(on);
                on("file:preprocessor", async (file) => {
                    await syncFeatureFile(file);
                    const cucumberPlugin = createBundler({
                        plugins: [createEsbuildPlugin(config)],
                    });
                    return cucumberPlugin(file);
                });
                return config;
            }
        // ...
        ```

    === "Video"

        Please note the the steps and the issue's summary changing due to the feature import.

        <video preload="none" poster="../../../assets/videos/guides_feature_synchronization_00.jpg" controls muted>
            <source src="../../../assets/videos/guides_feature_synchronization_00.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

### Language support

By default, Xray expects feature files to use English keywords.
If you want to use [different languages](https://cucumber.io/docs/gherkin/languages/), make sure to add the corresponding `#!gherkin # language:` header to your feature files, as described [here](https://cucumber.io/docs/gherkin/reference/#spoken-languages).

!!! example

    ```gherkin
    # language: de
    Funktionalität: Weiterleitung Beispielseite

        @TestName:CYP-129
        Szenario: Weiterleitung durch Klick
            Angenommen Beispielseite
            Wenn Klick auf Link
            Dann Weiterleitung findet statt
    ```

## Feature file download

!!! development
    Synchronization of local feature files based on the step definitions as managed in Xray is currently still being worked on (i.e. download of Xray step definitions to local feature files and then running them).