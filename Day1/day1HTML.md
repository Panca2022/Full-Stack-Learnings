## Introduction 
-> HTML is the structure of the website.<br>
-> Its a markup language but not programming language.<br>
-> By default it is not have an interactive interface. But by combining with the CSS and JS it will be interactcive.<br>
-> HTML is not case sensitive 

## Code:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>

    <hr>

    <p>This is a paragraph</p>

    <hr>

    <a href="https:www.github.com/Panca-2022">Visit my Portfolio</a><br><br>

    <hr>

    <img src="./assets/image.png" alt="This is an sample image" width="200px" height="200px">

    <hr>

    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JS</li>
    </ul>
    
    <hr>

    <ol>
        <li>Angular</li>
        <li>Vue</li>
        <li>React</li>
    </ol>
    
    <hr>
</body>
</html>
```

## Page Structure
![Output](https://github.com/Panca2022/Full-Stack-Learnings/blob/main/assets/Screenshot1.png)
![Output](https://github.com/Panca2022/Full-Stack-Learnings/blob/main/assets/Screenshot2.png)

## Explanation of the tags:
```!DOCTYPE```: Document type declaration. It's not a tag. It tells that the document is HTML 5 version.<br>
```html```: Root element and other elements within it.<br>
```head```: Elements within this will not be visible in the frontend.<br>
```title```: The name in title will be visible in the browser tab.<br>
```body```: The body tag contains the main content of the webpage.<br>
```h1 - h6```: The heading will be in the level-by-level size from ascending to descending. Useful in the SEO.<br>
```p```: This will tell that, the content inside this will be paragraph. Automttically adds space before and after the paragraph when rendering <br>
```a```: It defines the hyperlink, were it redirects to another webpage.<br>
    -> ```href```: This attribute belongs to tag ```a```, which contains the link.<br>
```img```: The image tag helps to embed an image in a website.<br>
    -> ```src```: This contains the link for the image.<br>
    -> ```alt```: This is an alternative description for the image can be visible, if the image is not be available in the webpade for some circumstance.<br>
    -> ```width```: This will set the width of the image.<br>
    -> ```height```: This will set the height of the image.<br>
```ul```: It defines the unordered list. It structure the list with bullet points, arrow points etc.<br>
```ol```: It defines the ordered list. It structure the list with numericals, alphabets, roman numbers.<br>
```li```: Defines the list items, which comes under the ul or ol.<br>
```br```: This is a line breaker, were it does not print anything. It's an empty element <br>
```hr```: This is an Horizontal Line tag.

## Elements and Tags:
-> Elements: The complete structure that will be included with opening tags, closing tags, content.<br>
        -> Block Element: <br>
            - It takes full width available of the actual content width. <br>
            - It typically starts in a new line.<br>
            - Example: div, p, h1 - h6, ol, ul, table, form, section, article, nav, aside, header, footer.<br>
        -> Inline Elements:<br>
            - It takes only necessary amount needed for the inline element.<br>
            - It doesn't start in the new line.<br>
            - Example: span, a, img, strong, b, i, br, input.<br>

-> Tags: Actual Keyword, that is enclosed in angle brackets<br>
