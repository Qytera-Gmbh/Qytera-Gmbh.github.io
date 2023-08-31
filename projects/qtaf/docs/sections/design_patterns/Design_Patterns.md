# QTAF Test Automation Design Patterns

As projects grow it is neccessary that code is readable and maintainable. Design patterns help to master large projects and they help other developers understanding the code. In this article we want to introduce you to the most convenient design patterns in test automation with QTAF.

## Lazy Loading with the Supplier Pattern

<p>
<b>Why lazy loading?</b>
The supplier pattern helps you to deal with page objecs. For complex sites it can be neccessary to build nested page objects where you have a parent page objects that represents a whole page and child page objects that represent fractions of that site. When we have nested page objects it can be neccessary to pass web elements between two page objects, for example if the parent page objects wants to delegate the responsibility for some fraction of a page to a child page object and need to tell the child page object what its root element is. The parent page objects would instantiate these child objects and then pass the root web element of the page fraction to them. But this can lead to untraceability of web elements, because at construction time of the child page object the page fraction might not be available. Also in long lasting test cases elements can become stale, because the page might have been reloaded or changed during the test case. There needs to be a mechanism that loads the web elements that the parent page object provided only at the time when they are needeed.
</p>
<b>Different approaches</b>
<p>
We have different options how we can do this. The first option would be to fetch a web element by its selector and then pass it to the child page object. But this comes at a high risk of getting a StaleElementException. If the child page object is used multiple times in a test case it may be neccessary to reload a web element, but in this case this wouldn't be possible because the child page opbject has no information about how the web element was selected.
</p>
<p>
A possible solution for this problem would be that we can pass a selector instead of a web element to a child object. This enabled the page object to reload a web element every time we query it. With that technique it is possible to load web elements when they are needed and not when the child object is instantiated by its parent page object. This technique is also called "Lazy Loading". But there is a third option which is veen better than passing a selector to the child object. We also can pass a reference to a function which the child page object can call to get a web element. This is even more powerfull then passing the selector to the child page object, because we can add any logic to the creation process of the web element.
</p>
<b>Supplier functions</b>
<p>
Function that accepts no arguments and return an object of type `T` have a special functional interface in Java which is named `Supplier<T>`. When we construct a child page object that represents a fraction of a page we can pass a function to this child page object which can load the root web element of the page franction when it is needed. This pattern is similar to the observer pattern, where an observer can register functions in a subject that are executed when a certain event occurs. In the supplier design pattern the parent page objects provides methods for its child page objects that help them to load their own root web element. That is the whole idea of the supplier pattern: not the parent class decides when the web element is wanted but the child page object does.
</p>
<b>Implementation in QTAF</b>
<p>
Now lets look how we can implement the supplier pattern in QTAF. We assume that we want to model the following web page. The parent page object should model the complete page which starts at the div element with the id "root". The child page object should model the fraction of the page that is wrapped by the `<article>` tag. This would be the root web element of the child page object.
</p>

```html
<div id="root">
    <article>
        <h1>Article 1</h1>
        <div>Lorem Ipsum</div>
    </article>
</div>
```

First we define the parent page object. It has a method named `getArticle()` which accepts no arguments and returns a `SelenideElement` object. This matches the definition of a supplier function.

```java
public class ParentPageObject extends QtafTestNGContext {
    SelenideElement getArticle() {
        return $("article");
    }
}
```

Now lets look at the code of the child page object. This page object has a method named `setParent(Supplier<SelenideElement>)` which can be used by parent page objects to provide the root web element of the page fraction. The function reference is stored in a class attribute named `parent`. The supplier function itself is of type `Supplier<SelenideElement>`. Because the attribute is a function reference it is up to the child page object when this method is called. A function reference which is stored in a variable or a class attribute can be called by the expression `<attribute-name>`.get(). The child page object has methods for getting the headline and the text of the article, which first get the article web element by calling the function stored in the `parent` attribute and then calling a selector function on the returned web element.

```java
public class ChildPageObject extends QtafTestNGContext {
    private Supplier<SelenideElement> parent;

    public ChildPageObject setParent(Supplier<SelenideElement>) {
        this.parent = parent;
    }

    public SelenideElement getHeadline() {
        return parent.get().$("h1").shouldBe(visible);
    }

    public SelenideElement getText() {
        return parent.get().$("div").shouldBe(visible);
    }
}
```

Last we need a function in the parent page object that constructs the child page objects and passes the parent web element to it. First we get an instance of the child page object with the `load()` method of `QtafTestNGContext`. Then we call the `setParent()` method of the created instance, whcih receives a reference to the function `getArticle` as an argument. References to functions are notated by the expression `this::<function-name>` without parenthesis in Java. Finnaly we return the created page object. With this approach you can create multiple instances of a page object class that have different parent web elements.

```java

public class ParentPageObject extends QtafTestNGContext {
    SelenideElement getArticle() {
        return $("article");
    }

    ChildPageObject getChildPageObject() {
        return load(ChildPageObject.class).setParent(this::getArticle)
    }
}
```