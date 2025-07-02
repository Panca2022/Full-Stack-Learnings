## HTML Attributes:
-> Attributes that are used within the opening tags of an HTML element.
-> They provide the dditional informations about the HTML Element.
-> Format: ```name = "value"```.
-> This will tell the element how it should be appeared.

## Syntax:
```<tagame name = "value">...</tagname>```

## Code:
```
<!DOCTYPE html>
<head>
    <title>Document</title>
</head>
<body>
    <img src="./assets/image.png" alt="Sample Image" width="500px" height="500px" title="Image">

    <a href="https://github.com/Panca2022/Panca-2022">Visit my Portfolio</a>
</body>
</html>
```

## Output:
[Output](../assets/Screenshot3.png)
[Hands-on_Output](../assets/Screenshot4.png)

## Explanation:
```title```: Defines the name that will be visible in the tab 
```strong```: This will bold the text
```em```: It makes the text in itlic format 
```u```: This underlines the text
```b```: This also bolds the text
```mark```: The mark gives teh bullet point figure to the list 
```&lt```: It is an entity which represents the Lesser than symbol
```&gt```: It is an entity which represents the Greater than symbol
```&copy```: n entity that is used to display copyright symbol
```img```: This is the tag
    -> ```src```: The attribute is src where it tells to show the image from the source link.
    -> ```alt```: alt tells the alternative description for the image, which will be visible when the image is not visible.
    -> ```width```: Defines the Width of the image.
    -> ```height```: Defines the height of the image.
    -> ```title```: The title will show some text, when the mouse hover over the image. Provides some additional detail about the image.
```a```: It defines the hyperlink, were it redirects to another webpage.
    -> Unvisited Link: Underlined and will be in Blue 
    -> Visited Link: Underlined and will be in Purple 
    -> Active Link: Underlined and Red

### Some of Linking attributes as interlinking:
-> ```href```: Links to a website or any other format of document 
-> ```mailto```: Link to an email address 
-> ```tel```: Links to the Phone number 
-> ```button```: The provided link will be embedded in the format of button for the accessing
-> ```download```: Provided with the link of the file to download

### Links - Target Attributes
-> _blank = Opens the link in new tab or window 
-> _self = Opens in the same frame or window as the link, it's a default behaviour 
-> _parent = Opens document in the parent frame 
-> _top = Opens the document in the full body window 

## Text Formatting
-> Logical Formatting: Convey the meaning and importance of the text without necessarily altering the style of the visual apperance
    - ```em```
    - ```strong```
-> Physical Formatting: Directly affects the visul appearance of the text on the webpage by changinf the font size and other styles 
    - ```b```
    - ```i```
## Some important points in Attributes usage:
- Use Lower case for attributes 
- Always quote attributes values 
- Usage of single or double quote is fine
- Boolean attributes should be written without values
- Proper attribute order for readability 
- Avoid using styles in the format of attributes. Use styles in the separate CSS files