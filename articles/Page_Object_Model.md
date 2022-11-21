# Page Object Model

The Page Object Model is a software design pattern that describes interfaces for software-controlled manipulation of an element of a graphical user interface. The basic idea of the Page Object Model is to describe and control elements of a GUI through a parameterisable code base. The page object model is often used in the software-based automation of software applications with a graphical user interface.

There are two basic ways to select elements of a graphical user interface: First, each element can be assigned a unique ID. On the other hand, there is the possibility to select elements by means of a query language. A page object consists of a set of selectors that identify one or more elements of a GUI by means of an ID or a query language. In the context of web applications, GUI elements are mainly identified by unique IDs, CSS or HTML attributes. Furthermore, methods are defined in a page object that can perform a manipulation on one or more elements of the web application or read their attributes. The attributes of a GUI element are, for example, information about the graphic representation of the element (height, width, colours, etc.), its position on the display device and its relationship to other elements of the GUI.

## Example of page objects

The following HTML code is an example of a page object for a website. The page object shown consists of four basic elements: An image, a headline, a text and a button.

<img src="https://qytera-gmbh.github.io/img/qtaf/page_objects/ui_page_object.jpg" />

This is the corresponding HTML source code of the shown UI element:

```java
<div>
	<img
	src="https://www.qytera.de/sites/default/files/startseite-2020/qytera-testmanagement-300-169.jpg" alt="" class="startseite-saeulen-logo" />
	<h3>Continuous Testing</h3>
	<p>Wir verhelfen Ihnen zu kontinuierlichen und schnellen Softwarelieferungen in hoher Qualität.</p>
	<form action="https://www.qytera.de/testing-solutions/continuous-testing" method="get">
		<button class="button-red consulting-blog-verlinkung-button">Mehr erfahren</button>
	</form>
</div>
```

In test automation, a class is now created in which methods for interacting with the elements of the page object are defined. Useful methods for interacting with the page object shown could be reading the headline and the text as well as clicking the button.

The following is an example of the definition of a page object using the Java programming language. The root node of the page object is passed to the class in the constructor. Subsequently, references to the UI elements (image, heading, text and button) are stored in the class attributes. Furthermore, methods for interacting with the page object are defined in the class, such as reading out the texts of the elements or other attributes such as the URL of the image.

```java
public class CardPageObject {
    HTMLImageElement image;
    HTMLElement headline;
    HTMLParagraphElement paragraph;
    HTMLButtonElement button;

    CardPageObject(WebElement rootElement) {
        image = (HTMLImageElement) rootElement.findElement(By.cssSelector("img.startseite-saeulen-logo"));
        headline = (HTMLElement) rootElement.findElement(By.cssSelector("h3"));
        paragraph = (HTMLParagraphElement) rootElement.findElement(By.cssSelector("p"));
        button = (HTMLButtonElement) rootElement.findElement(By.cssSelector("button.button-red"));
    }

    String getImageSource() {
        return image.getAttribute("src");
    }

    String getHeadlineText() {
        return headline.getAttribute("innerText");
    }

    String getParagraphText() {
        return paragraph.getAttribute("innerText");
    }

    void clickButton() {
        ((WebElement) button).click();
    }
}
```

On the website examined, UI elements with a similar structure to the one shown can be found.
From the point of view of test automation, it makes no sense to abstract each of these objects
with its own page object class. Instead, it makes more sense to create a common class for these
page objects and to pass parameters to this class that can be used to react to deviations between
the individual page objects.

<img src="https://qytera-gmbh.github.io/img/qtaf/page_objects/ui_page_objects.jpg" />