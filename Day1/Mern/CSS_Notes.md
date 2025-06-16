# 🎨 Day 1: Introduction to CSS

## What is CSS?

- **CSS (Cascading Style Sheets)** is a language used to style and layout HTML elements on a web page.
- It controls colors, fonts, spacing, positioning, responsiveness, and overall design.
- CSS separates **content (HTML)** from **presentation (CSS)**, making webpages easier to manage and maintain.

---

## Types of CSS

1. **Inline CSS**
   - Applied directly inside the HTML element using the `style` attribute.
   - This can be used without using selectors.
   - Challenge to hndle this in website but sometimes it is useful 
   - Example:
     ```html
     <p style="color: blue;">This is blue text.</p>
     ```

2. **Internal CSS**
   - Defined within the `<style>` tag in the `<head>` section of the HTML.
   - Used when we are syling in a single page within the HTML
   - Time consuming process. But can be used when we are styling a single unique page 
   - Example:
     ```html
     <head>
       <style>
         p {
           color: green;
         }
       </style>
     </head>
     ```

3. **External CSS**
   - Stored in a separate `.css` file and linked to the HTML.
   - Example:
     ```html
     <link rel="stylesheet" href="style.css">
     ```

---

## Comments of CSS
``` /* This is comment in CSS */

---

## CSS Syntax
```css
selector {
  property: value;
}

**selector**: Target the HTML Element
**Property**: The style attribute we want to style
**Value: The setting we are applying to the element 

---

## CSS Selectors
- In CSS, selectors select the specific word you want to style. There are different types of selectors:
    - Element selector
    - Universal selector
    - Id selector
    - Class selectors

### Elementor Selector: 
    - Provides the styling to a selected Element of HTML
    ``` CSS
    Element  {  
        property: value  
    }   
    ```Example 
    p{
        font: 20px
    }

### Universal Selector: 
    - Provides the styling to the overall document of HTML
    - Uses * (asterisk) which denotes it is universal selector 
    ``` CSS
    *  {  
        property: value  
    }   
    ```Example 
    *{
        font: 20px
    }

### Id Selector: 
    - Provides the unique styling to the created id with the name 
    - Uses # as id. 
    ``` CSS
    #id  {  
        property: value  
    }   
    ```Example 
    #id1{
        font: 20px
    }

### Class Selector: 
    - Provides the styling to a element of HTML which created with the attribute class and that can be linked with the same name which used to create the class
    - Multiple class can come up with same name 
    - Class selector denoted with the (.)
    ``` CSS
    .class-name  {  
        property: value  
    }   
    ```Example 
    .class1{
        font: 20px
    }

## Linking CSS to HTML
### External CSS
- Can be linked with the element link in HTML and use the attributes rel and href.
    - rel: Defines the type of the file.
    - href: Contains the link of CSS file.
```<link rel="stylesheet" href="style.css">

### Internal CSS
- Internal CSS allows to style the HTML by using the CSS within the HTML file itself.
```<head>
  <style>
    body {
      background-color: lightgray;
    }
  </style>
</head>
