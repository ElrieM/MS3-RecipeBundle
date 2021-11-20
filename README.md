<h1 align="center">Recipe Bundle</h1>

[View the live project here.](http://ci-ms3-recipebook.herokuapp.com/)

Two user types' credentials have been included below:
| User type | Username | Password |
| --- | --- | --- |
| Admin | Admin | Admin |
| General | User1 | User1 |
(Case sensitive)

This website provides users with the opportunity to add, edit and delete your own recipes, while sharing and having access to other users' recipes.

![mockup](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/amiresponsive.png)

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

This website will allow users to keep a digital recipe book, easily uploading and storing their favourite recipes to refer back to later instead of thumbing through piles of paper recipes. Users also have access to recipes uploaded by other users. Users are able to search recipes names or ingredients.

### Target audience

- Novice cooks
- Seasoned cooks

## 1.2 Scope Plane

### 1.2.1 Requirements and functional specifications

- Header and Footer
  - Simple header with Logo that returns to landing page, navbar with links and dropdown for user account management.
  - Hamburger menu on small and medium device sizes.
  - Navbar navigates to Home (landing page), Collection page and Sign Out page (only available when signed in), Sign In page and Register page (only available when signed out), and Administration page (only available to Admin user) and contact page.
  - Footer with icons, navigates to Twitter, FaceBook and Pinterest.
- Landing page
  - Visible when signed out or signed out
- Administrator
  - Add, Edit or Remove cuisine type options
  - Add, Edit or Remove diet type options
  - Add, Edit or Remove meal type options
- Collection page
  - Only available to signed in users
  - Collection page displays list of recipes
  - Button to Add new recipes
  - Buttons to Remove recipes
  - Buttons to Edit recipes
  - Search by ingredients or name
- Add new recipes to database
- Remove recipes, Admin can remove all, User can only remove what they've created
- Edit recipes, Admin can edit all, User can only edit what they've created
- User authentication
  - Sign in to get access to collection of recipes
  - Sign out
  - Register new credentials
  - Reset password from Sign in page
- Contact form with options to report bugs, make suggestions or other.

### 1.2.2 User Stories

#### Site Visitor Goals

  1. As a Site Visitor, I want to easily navigate the website's pages from the header and footer.
  2. As a Site Visitor, I want to be able to view a collection of recipes.
  3. As a Site Visitor, I want to be able to search by names or ingredients.
  4. As a Site Visitor, I want to be able to add new recipes.
  5. As a Site Visitor, I want to be able to edit my recipes.
  6. As a Site Visitor, I want to be able to remove recipes I no longer want to share on the site.
  7. As a Site Visitor, I want to be able to contact site owners.

#### Site Owner Goals

  8. As the Site Owner, I want to make it easy and convenient for users to send suggestions for improvement or bug reports to a dedicated mailbox, thereby improving the chances of them returning.
  9. As the Site Owner, I want to restrict recipe-related features to registered users.
  10. As the Site Owner, I want to be able to easily add, edit or remove recipe dropdown options (cuisine, meal type, diet).

## 1.3 Structure Plane

### Website pages

The website consists of the following pages:

- Landing page: First web page and home page
- Register page: Register form for new users
- Sign in page: Allows returning (registered) visitors to sign in.
- Administrator page: Restricted to Admin user. View cuisine, diet and mealtypes with options to edit or remove
- Add cuisine page: Add new cuisine option for Add recipe page.
- Add diet page: Add new diet option for Add recipe page.
- Add mealtype page: Add new mealtype option for Add recipe page.
- Edit cuisine page: Edit existing cuisine option for Add recipe page.
- Edit mealtype page: Edit mealtype cuisine option for Add recipe page.
- Edit diet page: Edit existing diet option for Add recipe page.
- Recipe collection page: Shows collection of all recipes in database.
- Recipe viewing page: Views details for recipe selected from collection page.
- Add recipe page: Add new recipe, written to database and returns to collection page, where it is shown.
- Edit recipe page: Edit existing recipe and update database details.
- Contact page: Contact form with subject options.
- 404 error page: Displays when incorrect URL entered.
- 400 and 500 error pages: Display when errors occur on the website.

### Code Structure:

- Flask Blueprints used to construct / build the website.
- Project structure
  - Admin - Contains flask route for landing page.
  - Authentication (Auth) - Flask routes for sign in, register, resetting password and signing out.
  - Contact - Flask route for contact form.
  - Manage - Flask routes for adding, editing and deleting cuisines, meal types and diet options.
  - Recipes - Flask routes for viewing collection of recipes, adding, editing and viewing recipe details.
  - Errors - Flask routes for page error handlers (404, 400 and 500).
  - Static
    - CSS
    - Images
    - JS
  - Templates - HTML templates, corresponds with abovementioned Flask routes
  - Util - Contains AWS function and variables
  - app.py - setup, create and run application
  - env.py - not saved to source control, contains sensitive passwords and access keys.

Schematic website flow can be seen ![here](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/database_diagram.png)

### MongoDB database

- Production database - MS3RecipeBundle - created to store site information:
  - Users - stores username, email and passwords
  - Cuisines - stores cuisines for recipe dropdown options, managed by Admin
  - Diets - stores diets for recipe dropdown options, managed by Admin
  - Mealtypes - stores mealtypes for recipe dropdown options, managed by Admin
  - Recipes - stores recipe information, including selected options from previous 3 tables

### Users

- Stores username, email address and password
- Password is encrypted with generate_password_hash for Werkzeug.security Python library.
![snapshot](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/mongodb-users.png)

### Cuisines

- Stores cuisine options for Add Recipe dropdown options
![snapshot](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/mongodb-cuisines.png)

### Diets

- Stores diet options for Add Recipe dropdown options
![snapshot](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/mongodb-diets.png)

### Meal types

- Stores meal type options for Add Recipe dropdown options
![snapshot](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/mongodb-mealtypes.png)

### Recipes

- Stores recipe details, for recipes created by admin and other users
- Recipe name and ingredients used as search index.
![snapshot](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/mongodb-recipes.png)

## Amazon Web Services S3 bucket

Images uploaded by users and readme images are stored in AWS S3. Header image and favicon have been locally saved for faster loading.

Steps taken integration:

1. Created user account with AWS
2. Created an IAM user -  [detailed steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-up-s3.html)
![S3_IAM](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/AWS_S3_2.png)
3. Created S3 bucket named ms3recipebundle - [detailed steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
![S3_landing](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/AWS_S3_1.png)
4. Imported Python library, [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), as console to create, configure and manage AWS services.
5. Assigned s3 variables (bucket name, url, access and security keys) in util.py file.
6. Create function to upload image files, used by add recipe and edit recipe pages.

## 1.4 Skeleton Plane

### 1.4.1 Navigation

- Page header navigates to Landing page, Admin page (Admin user only), Collection page and Sign Out page (if signed in), Sign In page and Register page (if not signed in).
- Sign In page navigates to Register page and Reset page.
- Sign Out page navigates to Register page.
- Page footer navigates to social media links (Pinterest, FaceBook and Twitter).

### 1.4.2 Wireframes

- Home / Landing page ![view](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/home.png)
- Admin page ![view](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/admin.png)
- Collection page ![view](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/collection.png)
- Recipe add / edit pages ![view](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/change_recipe.png)
- Recipe view page ![view](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/view_recipe.png)

## 1.5 Surface Plane

### Colour scheme

- The colour scheme was generated from the header image.

- The main colours for the themes were generated by uploading ![a picture from Pexels](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/pexels-rachel-claire-4993251.jpg) to [colormind.io](http://colormind.io/bootstrap/)
  - #DCDFD1 Moon Mist - Background colour
  - #C4B7B5 Cold Turkey - NavBar text colour
  - #1F1012 Gondola - Header text
  - #5F3E52 Eggplant - Content text
  - #8F9A6D Avocado
  - #786779 Salt Box - Dropdown Menu background
  - Snapshot of palette images ![mockup](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/color-palette.png)
  - Attribution: [Photo by Rachel Claire from Pexels](https://www.pexels.com/photo/delicious-cheese-and-sausage-garnished-with-nuts-and-herbs-in-restaurant-4993251/)

### Typography

- I selected the calm and easy-to-read font [Zen Old Mincho](https://fonts.google.com/specimen/Zen+Old+Mincho?query=Zen+Old+Mincho) as the main font, and
- [Calligraffitti](https://fonts.google.com/specimen/Calligraffitti?query=calligraf) as a complementary font, which bears a resemblance to herbs and fits with the food theme of the site.

### Imagery

- I opted for a single image across all pages, with some white space to complement it. I searched for images of food on Pexels, and selected an image with moody colours and a comforting effect.

# 2. Technologies Used

## 2.1 Languages Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)

## 2.2 Frameworks, Libraries & Programs Used

### - [Bootstrap 5.1:](https://getbootstrap.com/docs/5.1/getting-started/introduction/) <!-- omit in toc -->

- Bootstrap was used to assist with the responsiveness and styling of the website

### - [Google Fonts:](https://fonts.google.com/) <!-- omit in toc -->

- Imported (fonts)] fonts from Google Fonts into the style.css file used on all pages throughout the website.
  
### - [Font Awesome:](https://fontawesome.com/) <!-- omit in toc -->

- Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

### - [jQuery:](https://jquery.com/) <!-- omit in toc -->

- jQuery in conjunction with Bootstrap make the navbar and accordion responsive.

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

### - [StartBootstrap:](https://startbootstrap.com/theme/clean-blog) <!-- omit in toc -->

- Base template used for layout, css and javascript.

### - [MDBootstrap:](https://mdbootstrap.com/) <!--- omit in toc -->

- Used [registration form #7](https://mdbootstrap.com/docs/standard/extended/registration/) as starting for signup form
- Used [login form #6](https://mdbootstrap.com/docs/standard/extended/login/) as starting point for sign in form
- After formatting, the final version was used to create the Reset password form.

### - [PolicyMaker](https://policymaker.io/) <!-- omit in toc -->

- Terms for register form obtained from free template [from](https://policymaker.io/terms-conditions-ready)

### - [Paint 11.2110.0.0](https://support.microsoft.com/en-us/windows/get-microsoft-paint-a6b9578c-ed1c-5b09-0699-4ed8115f9aa9)

- Used to create placeholder image and user testing files.

### - [Snipping Tool 11.2109.37.0](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b)

- Used for screenshots during testing.

### - [colormind.io](http://colormind.io/image/)

- Used to generate colour palette for website.

# 3. Features

## 3.1 Existing Features

- Responsive on all device sizes
- User authentication (Sign in, Sign out, Reset Password and Register)
- Interactive elements
- Add recipes, edit recipes, remove recipes
- Contact form to report bugs / make suggestions

## 3.2 Features Left to Implement

- Add filter features, to separate recipes by cuisine type, meal type or diet type.
- Pin functionality, to store favourite recipes for later reference.
- Add user account manager rights.
- Add confirm delete feature.
- Connect to Spoonacular API to enhance search abilities.
- Add shopping list function.
- Connect to recipe database (potentially Spoonacular) for greater variety.
- Connect to Spoonacular for improved input and matching ability.

# 4. Testing

## [Click here to go to testing](TESTING.md)

# 5. APIs

## [EmailJS](https://www.emailjs.com/)

- Create (free) user account
- Add an email services - [detailed steps](https://www.emailjs.com/docs/user-guide/connecting-email-services/)
- Create an email template - [detailed steps](https://www.emailjs.com/docs/user-guide/creating-email-templates/)
- Create email form - [detailed steps](https://www.emailjs.com/docs/tutorial/creating-contact-form/)
- Install and update script to send email - [installation guide](https://www.emailjs.com/docs/sdk/installation/)
- Add variables to make (service_id, template_name)

# 6. Deployment

## 6.1 - GitHub

### Forking the GitHub Repository

A fork is a copy of the repository, allowing you to experiment with changes without affecting the original project.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ElrieM/MS3_RecipeBundle).
2. In the banner above the Repository, click on the "Fork" button.
3. If you have succeeded, you now have a copy of the original repository in your GitHub account.

Alternatively, click [here](https://docs.github.com/en/github/getting-started-with-github/quickstart/fork-a-repo) for a guide to fork a repository.

### Making a Local Clone

A clone allows you to create a local copy of a repository on your computer and sync between your computer and the GitHub repository.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ElrieM/MS3_RecipeBundle)
2. Click on Code, click on the copy button next to HTTPS to copy the URL.
3. Open Git Bash.
4. Change the current working directory to the location where the cloned directory should be stored.
5. Type "git clone', then paste the URL copied in step 2.
6. Press Enter to create a local clone.

Alternatively, click [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) for a guide to clone a repository.

### Create env.py

- Create env.py file in root folder, with the following parameters
    os.environ.setdefault("IP", [user input])
    os.environ.setdefault("PORT",  [user input])
    os.environ.setdefault("SECRET_KEY",  [user input])
    os.environ.setdefault("MONGO_URI",  [user input])
    os.environ.setdefault("MONGO_DBNAME",  [user input])
    os.environ.setdefault("AWS_ACCESS_KEY_ID",  [user input])
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY",  [user input])

- Install packages per requirements.txt file

- Run application with CLI (PIP / PIPENV, depending on environment, run)  python3 app.py

## 6.2 - Heroku

Heroku is a free hosting service for hosting small projects.

### Deploy to Heroku

- Create a Heroku account
- Install Python (3.10 at time of creation) locally.
- Install Heroku CLI (first install Git CLI if you don't already have it installed).
- Log in to Heroku from CLI.
- Prepare and clone app - clone Github Repository.
- Deploy with heroku create and git push heroku main.
- Define a Procfile.
- Declare app dependencies in requirements.txt (pip install -r requirements.txt)
- Create new application with unique name.
- Navigate to Deploy, and connect to GitHub. Select repo, and then branch.
- Configure Config Vars - same parameters as in env.py file mentioned above.
- Deploy from dashboard.
- Open App.
- For more [details, visit here](https://devcenter.heroku.com/articles/getting-started-with-python)

### Deploy to AWS (Amazon Web Services)

1. Create AWS user account [here](https://aws.amazon.com/).
2. Create new user on IAM console [here](https://console.aws.amazon.com/).
3. Set AmazonS3FullAccess for user and note AWS Access and Secret keys.
4. On AWS S3 console, create a new bucket. Bucket name can be updated in the util.py file.
5. Set bucket policy, [see here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) for details and to generate policies. There is also an option to have policies generated from the bucket policies page.
6. Update util.py variables with bucket details from AWS:

    s3_bucket_name = "ms3recipebundle"
    s3_bucket_url = "http://ms3recipebundle.s3.amazonaws.com/"

### Set up MongoDB

1. Create new user account [here](https://www.mongodb.com/).
2. Create data cluster, see [here](https://docs.mongodb.com/manual/tutorial/getting-started/) for details.
3. Click on "Browse Collections", then create 5 collections:
   - users
   - cuisines
   - types
   - diet
   - recipes
4. Under Security > Database Access, create user with read and write access.
5. Under Security > Network Access, allow network access from the application's IP address.
6. Under Deployment > Database, click on Connect. Database is now connected to app.
7. In env.py, update MONGO_URI, MONGO_DBName and SECRET key and deploy to Heroku.

# 7. Credits

## 7.1. Code

- Bootstrap 5: Bootstrap Library used to make the site responsive using the Bootstrap Grid System
- [emailJS](https://www.emailjs.com/) for contact form API
- [Sign in form](https://mdbootstrap.com/docs/standard/extended/login/) for Sign In form
- [Register form](https://mdbootstrap.com/docs/standard/extended/register/) for Register form
- [Flash messages](https://flask.palletsprojects.com/en/2.0.x/patterns/flashing/)
- [Clicking for detailed recipe](https://stackoverflow.com/questions/67165461/get-data-on-selection-from-mongodb-list-in-python-and-html)
- [Form autocomplete](https://www.chromium.org/developers/design-documents/form-styles-that-chromium-understands)
- [AWS file uploading](https://gist.github.com/leongjinqwen/9d9a2d58bf2fb923658820559a88a5ec)
- [AWS file uploading with Flask](https://medium.com/aws-pocket/uploading-files-to-aws-s3-with-flask-3d3d213404fb)
- [Forcing Footer to bottom of page](https://stackoverflow.com/questions/16679146/force-footer-on-bottom-on-pages-with-little-content)
- [Displaying array](https://www.w3resource.com/javascript-exercises/javascript-array-exercise-13.php)

## 7.2. Content

- Recipes for testing :
  - [Banana Bread](https://www.simplyrecipes.com/recipes/banana_bread/)
  - [Beetroot Hummus Crispy Chickpea Sub Sandwich](https://www.bbcgoodfood.com/recipes/beetroot-hummus-crispy-chickpea-sub-sandwich)
- Recipe images:
  - [Banana Bread](Photo by Airin Party from Pexels https://www.pexels.com/photo/close-up-photography-of-banana-bread-on-saucer-830894/)
- [HTML error details](https://en.wikipedia.org/wiki/List_of_HTTP_status_code0073)
- Placeholder image for recipes adapted from [flaticon](https://www.flaticon.com/free-icon/hot-pot_465)
- Created favicon from logo using [favicon.cc](https://www.favicon.cc/)

## 7.3. Media

- [Font Awesome](http://fontawesome.com)
- [Google Fonts](https://fonts.google.com/)
- [Pexels](https://www.pexels.com/)
- [Testing and ReadMe example](https://github.com/pmeeny/CI-MS3-https://github.com/pmeeny/CI-MS3-FootballMemories)overview/why-cypress)
- [Header image](https://github.com/ElrieM/MS3-RecipeBundle/blob/3eb943e1db8a44dc72540c3f1a523e6976ab4384/README.md#L465)

## 7.4. Acknowledgements

- My mentor for guidance and support.
- My partner for advice and patience.
- My brothers for their pep-talks and positivity.
- My mother for all her words of love and encouragement.
- My manager, for support and holding me accountable for my wellbeing.
