# Day 1: Introduction to HTML

## What is HTML?

- **HTML** (HyperText Markup Language) is the standard markup language used to create the structure of web pages.
- It tells the browser how to display content using elements called **tags**.

### Breakdown:
- **HyperText**: Refers to "text within text"—it allows linking from one document to another. Example: when you click on a link in a webpage, it opens a new page.
- **Markup**: Means using tags to define how elements like headings, paragraphs, links, etc., are displayed.
- **Language**: A system of rules that browsers understand and follow to display content correctly.

---

## Basic Structure of an HTML Document

Here is the basic skeleton of any HTML page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>
    <p>Hello World !!!</p>
</body>
</html>

| Tag                                                                      | Description                                                                                        |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `<!DOCTYPE html>`                                                        | Declares the document type as HTML5. Helps the browser render the page correctly.                  |
| `<html>`                                                                 | The root element of the HTML page. All other elements go inside it.                                |
| `<head>`                                                                 | Contains metadata about the page—information not visible to the user (e.g., title, character set). |
| `<meta charset="UTF-8">`                                                 | Defines the character encoding (UTF-8 supports most characters from all known languages).          |
| `<meta name="viewport" content="width=device-width, initial-scale=1.0">` | Makes the page responsive on mobile devices.                                                       |
| `<title>`                                                                | Sets the title of the page (shown in the browser tab).                                             |
| `<body>`                                                                 | Contains the content that is visible on the webpage.                                               |
| `<h1>` to `<h6>`                                                         | Header tags. `<h1>` is the largest and most important; `<h6>` is the smallest.                     |
| `<p>`                                                                    | Defines the Paragraph content                                                                      |