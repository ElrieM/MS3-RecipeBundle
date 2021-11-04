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
  - Footer with icons, navigates to Home (landing page), Search page, Contact page (report bugs / suggestions or contact)
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

- Page header navigates to Landing page, Search page, Collection page and Sign Out page (if signed in), Sign In page and Register page (if not signed in).
- Sign In page navigates to Register page and vice versa.
- Page footer navigates to Landing page, Search page and Contact page.

### 1.4.2 Wireframes

- Home / Landing page ![view](static\readme\wireframes\index.png)
- Search page ![view](static\readme\wireframes\search.png)
- Collection page ![view](static\readme\wireframes\collection.png)
- Recipe add / edit pages ![view](static\readme\wireframes\recipe_edit.png)
- Recipe view page ![view](static\readme\wireframes\recipe_view.png)
- Contact page ![view](#)
- 404 error (Page Not Found) page ![view](#)

## 1.5 Surface Plane

### Colour scheme

- The colour scheme was generated from the header image.

- The main colours for the themes were generated by uploading ![a picture from Pexels]() to [colormind.io](http://colormind.io/bootstrap/)
  - #DCDFD1 Moon Mist - Background colour
  - #C4B7B5 Cold Turkey - NavBar text colour
  - #1F1012 Gondola - Header text
  - #5F3E52 Eggplant - Content text
  - #8F9A6D Avocado
  - #786779 Salt Box - Dropdown Menu background
  - Snapshot of palette images ![mockup](static\readme\other\color-palette.png)
  - Attribution: [Photo by Rachel Claire from Pexels](https://www.pexels.com/photo/delicious-cheese-and-sausage-garnished-with-nuts-and-herbs-in-restaurant-4993251/)

### Typography

- I selected the calm and easy-to-read font [Zen Old Mincho](https://fonts.google.com/specimen/Zen+Old+Mincho?query=Zen+Old+Mincho) as the main font, and
- [Calligraffitti](https://fonts.google.com/specimen/Calligraffitti?query=calligraf) as a complementary font, which bears a resemblance to herbs and fits with the food theme of the site.

### Imagery

- I opted for a single image across all pages, with some white space to complement it. I searched for images of food on Pexels, and selected an image with moody colours and a comforting effect.

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
