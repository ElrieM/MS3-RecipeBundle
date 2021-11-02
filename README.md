<h1 align="center">Recipe Bundle</h1>

[View the live project here.](http://ci-ms3-recipebook.herokuapp.com/)

This website provides users with the opportunity to add, edit and delete your own recipes, as well as search for other recipes recipes.

![mockup](#)

## Contents <!-- omit in toc -->

- [1. User Experience (UX)](#1-user-experience-ux)
  - [1.1 Strategy Plane](#11-strategy-plane)
    - [Target audience](#target-audience)
  - [1.2 Scope Plane](#12-scope-plane)
    - [1.2.1 Requirements and functional specifications](#121-requirements-and-functional-specifications)
    - [1.2.2 User Stories](#122-user-stories)
      - [Site Visitor Goals](#site-visitor-goals)
      - [Site Owner Goals](#site-owner-goals)
  - [1.3 Structure Plane](#13-structure-plane)
    - [Structure](#structure)
  - [1.4 Skeleton Plane](#14-skeleton-plane)
    - [1.4.1 Navigation](#141-navigation)
    - [1.4.2 Wireframes](#142-wireframes)
  - [1.5 Surface Plane](#15-surface-plane)
    - [Colour scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [2. Technologies Used](#2-technologies-used)
  - [2.1 Language Used](#21-language-used)
  - [2.2 Frameworks, Libraries & Programs Used](#22-frameworks-libraries--programs-used)
- [3. Features](#3-features)
      - [3.1 Existing Features](#31-existing-features)
      - [3.2 Features Left to Implement](#32-features-left-to-implement)
- [4. Testing](#4-testing)
      - [Click here to go to testing](#click-here-to-go-to-testing)
- [5. Deployment](#5-deployment)
  - [5.1. GitHub Pages](#51-github-pages)
  - [5.2. Forking the GitHub Repository](#52-forking-the-github-repository)
  - [5.3. Making a Local Clone](#53-making-a-local-clone)
- [6. Credits](#6-credits)
  - [6.1. Code](#61-code)
  - [6.2. Content](#62-content)
  - [6.3. Media](#63-media)
  - [6.4. Acknowledgements](#64-acknowledgements)

# 1. User Experience (UX)

## 1.1 Strategy Plane

This website will allow users to keep a digital recipe book, easily uploading and storing their favourite recipes to refer back to later instead of thumbing through piles of paper recipes. It will also enable them to search recipes based on ingredients they have on-hand.

### Target audience

- Cooking enthusiasts
- People looking to store family recipes safely

## 1.2 Scope Plane

### 1.2.1 Requirements and functional specifications

- Header and Footer
  - Simple header with Logo that returns to landing page and dropdown menu
  - Hamburger menu on all device sizes
  - Navbar navigates to Home (landing page), Search page, Collection page and Sign Out page (only available when signed in), Sign In page and Register page (only available when signed out).
  - Footer with icons, navigates to Home (landing page), Search page, Collection page and Sign Out page (only available when signed in), Sign In page and Register page (only available when signed out), Contact page (report bugs / suggestions or contact)
- Landing page
- Collection page
  - List of recipes
  - Add new recipes
  - Remove recipes
- Search
  - Search by ingredients
  - Search by cuisine
  - Search by meal type

### 1.2.2 User Stories

#### Site Visitor Goals

  1. As a Site Visitor, I want to easily navigate the website's pages from the header and footer.
  2. As a Site Visitor, I want to be able to privately store my recipes.
  3. As a Site Visitor, I want to be able to view my stored recipes.
  4. As a Site Visitor, I want to be able to add my recipes.
  5. As a Site Visitor, I want to be able to edit my recipes.
  6. As a Site Visitor, I want to be able to remove recipes I no longer want to store.
  7. As a Site Visitor, I want to be able to search for other recipes that may interest me.

#### Site Owner Goals

  8. As the Site Owner, I want to make it easy and convenient for users to send suggestions for improvement or bug reports to a dedicated mailbox, thereby improving the chances of them returning.
  9. As the Site Owner, I want to restrict recipe storage-related features to registered users.

## 1.3 Structure Plane

### Structure

The website consists of the following pages:

- Landing page
- Search page
- Recipe collection page
- Recipe page
- Contact page
- 404 error page
- Header:
  - Navigation button to all pages
- Footer:
  - Return to landing page, settings and contact form

Schematic website flow can be seen [here](static\readme\wireframes\site_map.png)

## 1.4 Skeleton Plane

### 1.4.1 Navigation

- Landing page navigates to...
- ... pages navigate to landing page, with settings and contact page accessible from header and footer.

### 1.4.2 Wireframes

- Home / Landing page - [view](static\readme\wireframes\index.png)
- Search page - [view](static\readme\wireframes\search.png)
- Collection page - [view](static\readme\wireframes\collection.png)
- Recipe add / edit pages - [view](static\readme\wireframes\recipe_edit.png)
- Recipe view page - [view](static\readme\wireframes\recipe_view.png)
- Contact page - [view](#)

## 1.5 Surface Plane

### Colour scheme

- For the colour scheme, I wanted to keep the colour schemes simple due to the nature of the game.

- The main colours for the three themes were:
  - Bright, generated by uploading [a picture from Pexels](/docs/other/bright.jpg) to [coolors](https://coolors.co/291420-adbd89-eac7ae-63183c-dddca6)
    - #DDDCA6 Pale Spring Bud - Background colour
    - #ADBD89 Olivine - Header and footer background colour
    - #EAC7AE Desert Sand - Navigation buttons on landing page 
    - #291420 Dark Purple - Header text
    - #63183C Tyrian Purple - Content text
    - #FFF White - puzzle and timer background
    - Snapshot of palette images ![mockup](docs/other/color-palette_bright.png)
    - Attribution: [Photo by Pixabay from Pexels](https://www.pexels.com/photo/butterfly-perched-on-flower-462118/)
    
  - Light, generated by uploading [a picture from Pexels](docs/other/light.jpg) to [coolors](https://coolors.co/ffffff-f7f1ff-decdf5-656176-534d56)
    - #F7F1FF Magnolia - Background colour and Content text
    - #DECDF5 Thistle - Header and footer background colour
    - #656176 Old Lavendar - Navigation buttons on landing page 
    - #534D56 Dark Liver - Header text
    - #FFF White - puzzle and timer background
    - Snapshot of palette images ![mockup](docs/other/color-palette_light.png)
    - Attribution: [Photo by Pixabay from Pexels](https://www.pexels.com/photo/pink-and-purple-flower-field-262713/)

  - Dark, generated by uploading [a picture from Pexels](docs/other/dark.jpg) to [coolors](https://coolors.co/4f6073-eeeeee-a8c4c3-3d4b59-60848b)
    - #3D4B59 Charcoal - Background colour
    - #4F6073 Black Coral - Header and footer background colour
    - #EEE Cultured - Navigation buttons on landing page, puzzle and timer background
    - #534D56 Dark Liver - Header and Content text
    - #60848B Steel Teal - Puzzle input cells
    - Snapshot of palette images ![mockup](docs/other/color-palette_dark.png)
    - Attribution: [Photo by Pixabay from Pexels](https://www.pexels.com/photo/close-up-of-leaf-326055/)

### Typography

- When selecting a font for the puzzle, I searched Google Fonts (filtering for Numerals) for a font with . I selected EB Garamond, which is a classical font with numbers that are equal in size and align with all other numbers in a single line. This was important to me to make sure the numbers in the puzzle appeared in a straight line across the grid, with no numbers dipping below or sticking out above others.

- For the website text, I used EB Garamond's suggested pairing "Raleway" for its elegant and classic format, which I feel alings with the nature of the game.

### Imagery

- I opted for a simple background on the because the puzzle grid is already quite busy and a busy background would add unnecessary distraction.

# 2. Technologies Used

## 2.1 Language Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)

## 2.2 Frameworks, Libraries & Programs Used

### - [Bootstrap 5:](https://getbootstrap.com/docs/5.1/getting-started/introduction/) <!-- omit in toc -->

- Bootstrap was used to assist with the responsiveness and styling of the website:
  - Horizontal alignment navs & tabs used for navbar
  
### - [Google Fonts:](https://fonts.google.com/) <!-- omit in toc -->

- Imported (fonts)] fonts from Google Fonts into the style.css file used on all pages throughout the website.
  
### - [Font Awesome:](https://fontawesome.com/) <!-- omit in toc -->

- Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

### - [jQuery:](https://jquery.com/) <!-- omit in toc -->

- jQuery in conjunction with Bootstrap make the navbar and modal responsive.

### - [jQuery UI:](https://jqueryui.com/) <!-- omit in toc -->

- Used to make solve modal draggable.

### - [Git:](https://git-scm.com/) <!-- omit in toc -->

- Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

### - [GitHub:](https://github.com/) <!-- omit in toc -->

- GitHub is used to store the projects code after being pushed from Git.

### - [Visual Studio Code:](https://code.visualstudio.com/) <!-- omit in toc -->

- IDE used to write code for this project.

### - [Balsamiq:](https://balsamiq.com/) <!-- omit in toc -->

- Balsamiq was used to create the wireframes during the design process.

### - [Am I Responsive:](http://ami.responsivedesign.is/) <!-- omit in toc -->

- Used to create mockups for README file.

### - [Resizing.app:](https://resizing.app/features/resize-png/) <!-- omit in toc -->

- Resize PNG to reduce README file sizes.

# 3. Features

## 3.1 Existing Features

- Responsive on all device sizes
- Interactive elements
- Contact form to report bugs / make suggestions

## 3.2 Features Left to Implement

- Puzzle for the day challenge, where site visitors can compete for better completion time
- Scoreboard to store best scored times and levels of all visitors on challenge game
- Check inputs against solution in both puzzle games
- Save last 5 completion times and levels in practice game to track improvement

# 4. Testing

## [Click here to go to testing](TESTING.md)

# 5. APIs

# 6. Deployment

# 7. Credits

## 7.1. Code

- Bootstrap 5: Bootstrap Library used to make the site responsive using the Bootstrap Grid System
- [emailJS](https://www.emailjs.com/) for contact form

## 7.2. Content

- Created favicon from logo using [favicon.cc](https://www.favicon.cc/)

## 7.3. Media

- [Font Awesome](http://fontawesome.com)
- [Google Fonts](https://fonts.google.com/)
- [Pexels](https://www.pexels.com/)
- [Testing example](https://github.com/pmeeny/CI-MS2-BicepMusicFanSite)
- [Favicon guidance](https://www.101computing.net/html-how-to-add-a-favicon/)
- [Cypress testing](https://www.chaijs.com/api/assert/)
- [Cypress guide for writing tests](https://docs.cypress.io/guides/overview/why-cypress)

## 7.4. Acknowledgements

- My mentor for guidance and support.
- My partner for advice and patience.
- My brothers for their pep-talks and positivity.
- My mother for all her words of love and encouragement.
