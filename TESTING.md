# 4. Testing

- The website was tested on Google Chrome, Firefox and Microsoft Edge.

- The website was viewed on a variety of devices, including:

| Name | Type | Browser | Version | Nature |
| --- | --- | --- | --- | --- |
| Xioami Mi 10T Lite | Mobile | Chrome | Chrome 96.0.4664.45 | Physical |
| iPhone 11s | Mobile | Chrome simulation | | Emulator |
| iPhone 5/SE | Mobile | Chrome simulation |  | Emulator |
| Galaxy Note 3 | Mobile | Chrome simulation | | Emulator |
| iPad | Tablet | Chrome simulation | | Emulator |
| Surface Duo | Tablet | Chrome simulation | | Emulator |
| Toshiba Satellite L850-F33V | Desktop | Chrome | Version 95.0.4638.69 (Official Build) (64-bit) | Physical |
| Dell Inspiron 15 5515 with 24" Dell monitor | Desktop | Chrome | Version 95.0.4638.69 (Official Build) (64-bit) | Physical |
| Dell Inspiron 15 5515 with 24" Dell monitor | Desktop | Firefox | 91.0.1 (64-bits)| Physical |
| Dell Inspiron 15 5515 with 24" Dell monitor | Desktop | Microsoft Edge | Version 95.0.1020.53 (Official build) (64-bit) | Physical |

- Friends and family were asked to review the site and documentation to point out bugs and /or user experience issues.

- [4. Testing](#4-testing)
  - [4.1 Manual testing](#41-manual-testing)
    - [4.1.1 HTML - W3C Markup Validator](#411-html---w3c-markup-validator)
    - [4.1.2 CSS - W3C CSS Validator](#412-css---w3c-css-validator)
    - [4.1.3 Accessibility - WAVE Web Accessibility Evaluation Tool](#413-accessibility---wave-web-accessibility-evaluation-tool)
    - [4.1.4 Performance - Chrome Lighthouse](#414-performance---chrome-lighthouse)
    - [4.1.5 JSHint](#415-jshint)
    - [4.1.6 User Experience testing](#416-user-experience-testing)
  - [4.2 Automated testing](#42-automated-testing)
    - [Tested page](#tested-page)
  - [4.3 Testing Bugs - Resolved](#43-testing-bugs---resolved)
  - [4.4 Known Bugs](#44-known-bugs)

## 4.1 Manual testing

The following tools were used to validate every page of project to ensure there were no syntax errors in the project:

### 4.1.1 HTML - W3C Markup Validator

- Pages tested:
  
| Page | Outcome | Link |
| --- | --- | --- |
| Home | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-home.png) |
| Sign in | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-singin.png) |
| Sign up | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-singup.png) |
| Reset  | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-reset.png) |
| Admin | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-admin.png) |
| Add cuisine | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-add_cuisine.png) |
| Edit cuisine | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-edit_cuisine.png) |
| Add mealtype | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-add_mealtype.png) |
| Edit mealtype | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-edit_mealtype.png) |
| Add diet | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-add_diet.png) |
| Edit diet | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-edit_diet.png) |
| Collection | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-collection.png) |
| View recipe | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-view_recipe.png) |
| Add recipe | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-add_recipe.png) |
| Edit recipe | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-edit_recipe.png) |
| Contact | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-contact.png) |
| Error (404) | No errors | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/html-error_pages.png) |
  
### 4.1.2 CSS - W3C CSS Validator

- All errors / warnings relate to Bootstrap template CSS.
- Summary of result:
- No errors or warnings from CSS style file unrelated to Bootstrap;
- Errors from Bootstrap 5.1 (unused / unrecognised errors); and
- Report can be found [here](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fci-ms3-recipebook.herokuapp.com%2Fhome&profile=css3svg&usermedium=all&warning=1&vextwarning=).
  
### 4.1.3 Accessibility - WAVE Web Accessibility Evaluation Tool

- Pages tested:
  
| Page | Result - Errors | Result - Warnings | Link |
| --- | --- | --- | --- |
| Home | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/home.png) |
| Sign in | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/singin.png) |
| Sign up | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/singup.png) |
| Reset  | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/reset_password.png) |
| Admin | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/admin.png) |
| Add cuisine | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/add_cuisine.png) |
| Edit cuisine | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/edit_cuisine.png) |
| Add mealtype | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/add_mealtype.png) |
| Edit mealtype | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/edit_mealtype.png) |
| Add diet | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/add_diet.png) |
| Edit diet | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/edit_diet.png) |
| Collection | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/collection.png) |
| View recipe | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/view_recipe.png) |
| Add recipe | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/add_recipe.png) |
| Edit recipe | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/edit_recipe.png) |
| Contact | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/contact.png) |
| Error (404) | No errors | None | ![results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/error_pages.png) |

### 4.1.4 Performance - Chrome Lighthouse

- Pages tested (mobile and desktop tested on each):

| Page | Scores - Desktop | Scores - Mobile |
| --- | --- |  --- |
| Home | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-home.png) | [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-home.png) |
| Sign in | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-singin.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-singin.png) |
| Sign up | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-singup.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-signup.png) |
| Reset  | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-reset.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-reset.png) |
| Admin | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-admin.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-admin.png) |
| Add cuisine | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-add_cuisine.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-add)cuisine.png) |
| Edit cuisine | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-edit_cuisine.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-edit_cuisine.png) |
| Add mealtype | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-add_mealtype.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-add_mealtype.png) |
| Edit mealtype | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-edit_mealtype.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-edit_mealtype.png) |
| Add diet | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-add_diet.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-add_diet.png) |
| Edit diet | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-edit_diet.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-edit_diet.png) |
| Collection | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-contact.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-contact.png) |
| View recipe | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-view_recipe.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-view_recipe.png) |
| Add recipe | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-add_recipe.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-add_recipe.png) |
| Edit recipe | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-edit_recipe.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-edit_recipe.png) |
| Contact | ![Desktop results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhd-contact.png)| [Mobile results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/lhm-contact.png) |

### 4.1.5 JSHint

- Pages tested (mobile and desktop tested on each):

| Page | Results | Link |
| --- | --- | --- |
| scripts.js | No issues | [results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/jshint-contact-form_js.png) |
| contact-form.js | Undefined emailJS ignored. No issues | [results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/jshint-contact-form_js.png) |

### 4.1.6 User Experience testing  

#### User Story 1. As a Site Visitor, I want to easily navigate the website's pages from the header and footer <!-- omit in toc -->

1.1 Header with Navigation Bar

- Requirements considered
  - Simple header with Logo that returns to landing page, navbar with links and dropdown for user account management.
  - Hamburger menu on small and medium device sizes.
  - Navbar navigates to Home (landing page), Collection page and Sign Out page (only available when signed in), Sign In page and Register page (only available when signed out), and Administration page (only available to Admin user) and contact page.

- Tests

| Step | Expected Result | Devices | Test Result |
| --- | --- | --- | --- |
| Click on Home | Navigates to Home page | Desktop, Tablet, Mobile| All passed |
| Click on NavBar | Navigates to Home page | Desktop, Tablet, Mobile| All passed |
| Click on Account > Sign In | Navigates to Sign In page | Desktop, Tablet, Mobile| All passed |
| Click on Account > select Register | Navigates to Sign Up | Desktop, Tablet, Mobile| All passed |
| Click on Contact | Navigates to Contact page | Desktop, Tablet, Mobile| All passed |
| Sign in as Admin, Click on Administrator | Navigates to Administration page | Desktop, Tablet, Mobile| All passed |
| Sign in as User1 | No Administration page option to click | Desktop, Tablet, Mobile| All passed |
| Click on Collection | Navigates to recipe Collection page | Desktop, Tablet, Mobile| All passed |
| Click on Account > Sign Out | Signs out and redirects to home page | Desktop, Tablet, Mobile| All passed |

1.2 Footer with navigation links

- Requirements considered
  - Footer with icons, navigates to Twitter, FaceBook and Pinterest.

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Click on Twitter icon | Opens new browser with Twitter landing page | Desktop, Tablet, Mobile| All passed |
  | Click on Pinterest icon | Opens new browser with Pinterest landing page | Desktop, Tablet, Mobile| All passed |
  | Click on FaceBook icon | Opens new browser with FaceBook landing page | Desktop, Tablet, Mobile| All passed |

1.3 Landing page

- Requirements considered
  - Visible when signed out or signed out.

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Sign in as Admin, Click on Home | Navigates to landing page | Desktop, Tablet, Mobile| All passed |
  | Sign in as User1 | Navigates to landing page | Desktop, Tablet, Mobile| All passed |

    ![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-1.png)

#### User Story 2. As a Site Visitor, I want to be able to view a collection of recipes and User Story 9. As the Site Owner, I want to restrict recipe-related features to registered users.<!-- omit in toc -->

- Requirements considered
  - Button to Add new recipes
  - Buttons to Remove recipes
  - Buttons to Edit recipes
  - Only available to signed in users

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Sign in as Admin, click on Collection page | See list of recipes with buttons | Desktop, Tablet, Mobile| All passed |
  | Sign in as User1, click on Collection page | See list of recipes with buttons | Desktop, Tablet, Mobile| All passed |
  | Not singed in | No Collection page button and not able to view from direct URL input | Desktop, Tablet, Mobile| All passed |
  | Sign in as User1, click on Collection page | See list of recipes with buttons | Desktop, Tablet, Mobile| All passed |

    ![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-2,8.png)

#### User Story 3. As a Site Visitor, I want to be able to search by names or ingredients. <!-- omit in toc -->

- Requirements considered
  - Search by ingredients or name

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Sign in as Admin, from Collection page, input Chickpeas (ingredient and in name of one recipe) | See list of recipes with chickpeas in name or ingredients | Desktop, Tablet, Mobile| All passed |
  | Sign in as User1, from Collection page, input Chickpeas (ingredient and in name of one recipe) | See list of recipes with chickpeas in name or ingredients | Desktop, Tablet, Mobile| All passed |
  | From Collection page, input apples (ingredient not currently in name of one recipe) | No results found returned | Desktop, Tablet, Mobile| All passed |

 ![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-3.png)

#### User Story 4. As a Site Visitor, I want to be able to add new recipes <!-- omit in toc -->

- Requirements considered
  - Add new recipes to database

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | From Collections page, click on Add button | Redirects to Add Recipe | Desktop, Tablet, Mobile| All passed |
  | Complete all fieds | Returns successfully submitted message on submission | Desktop, Tablet, Mobile| All passed |  
  | Automatic redirect to Collection page | New recipe appears in Collection page list | Desktop, Tablet, Mobile| All passed |

  ![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-4.png)

#### User Story 5. As a Site Visitor, I want to be able to edit my recipes. <!-- omit in toc -->

- Requirements considered
  - Edit recipes, Admin can edit all, User can only edit what they've created

  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | From Collections page, click on Edit button | Redirects to Edit Recipe page| Desktop, Tablet, Mobile| All passed |
  | Edit fieds | Database content pre-populated. Returns successfully submitted message on submission | Desktop, Tablet, Mobile| All passed |  
  | Automatic redirect to Collection page | Edited recipe appears in Collection page list | Desktop, Tablet, Mobile| All passed |

![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-5.png)

#### User Story 6.  As a Site Visitor, I want to be able to remove recipes I no longer want to share on the site. <!-- omit in toc -->

6.1 Challenge game page

- Requirements considered
  - Remove recipes, Admin can remove all, User can only remove what they've created

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | From Collections page, click on Delete button | Recipe no longer appears on page| Desktop, Tablet, Mobile| All passed |
  | Signed in as Admin, from Collections page, see where Delete button appears | Delete button appears on all options | Desktop, Tablet, Mobile| All passed |
  | Signed in as User1, from Collections page, see where Delete button appears | Delete button appears on options created by User1 only | Desktop, Tablet, Mobile| All passed |

  ![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-6.png)

#### User Story 7. As a Site Visitor, I want to be able to contact site owners and User Story 8. As the Site Owner, I want to make it easy and convenient for users to send suggestions for improvement or bug reports to a dedicated mailbox, thereby improving the chances of them returning <!-- omit in toc -->

- Requirements considered
  - Contact form with options to report bugs, make suggestions or other.

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Send test query from contact page | Sends email with emailJS to test inbox and displays message of successful sending | Desktop, Tablet, Mobile | Error message on submission |

  ![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-7.png)


#### 8. As the Site Owner, I want to make it easy and convenient for users to send suggestions for improvement or bug reports to a dedicated mailbox, thereby improving the chances of them returning.  <!-- omit in toc -->

Tested with User Story 7.

#### 9. As the Site Owner, I want to restrict recipe-related features to registered users <!-- omit in toc -->

Tested with User Story 2.

## User Story 10. As the Site Owner, I want to be able to easily add, edit or remove recipe dropdown options (cuisine, meal type, diet)

- Requirements considered
  - Add, Edit or Remove cuisine type options
  - Add, Edit or Remove diet type options
  - Add, Edit or Remove meal type options

 | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
 | Signed in as Admin, from Administrator page, Open Cuisine option and select Edit Button | Changes Cuisine details and returns new detail on Administrator page | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Cuisine option and select Add Button | Add Cuisine details and returns new detail on Administrator page | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Cuisine option and select Edit Button | Changes Cuisine details and returns new detail on Administrator page | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Cuisine option and select Delete Button | Removes Cuisine option from list | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Mealtype option and select Add Button | Add Mealtype details and returns new detail on Administrator page | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Mealtype option and select Edit Button | Changes Mealtype details and returns new detail on Administrator page | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Mealtype option and select Delete Button | Removes Mealtype option from list | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Diets option and select Add Button | Add Diet details and returns new detail on Administrator page | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Diet option and select Edit Button | Changes Diet details and returns new detail on Administrator page | Desktop, Tablet, Mobile| All passed |
 | Signed in as Admin, from Administrator page, Open Diet option and select Delete Button | Removes Diet option from list | Desktop, Tablet, Mobile| All passed |

 ![Results](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/testing/user_story-1.png)

## 4.2 Automated testing

[UILicious:](https://uilicious.com/)
Tested user login, register and sign out.

[Results)[https://snippet.uilicious.com/embed/test/private/8oQXB8MNQFS5kHi5nmH6BA?stepNum=1&autoplay=0]

Issues related to user error, manually tested highlighted tests and all passed.

## 4.3 Testing Bugs - Resolved

| Bug Found | Solution |
| --- | ---- |
| Certificate expired error, unable to write to MongoDB | Manually installed security certificate to resolve, with guidance [from]("https://www.mongodb.com/community/forums/t/keep-getting-serverselectiontimeouterror/126190/10") |
| BadRequestKeyError '400: Bad Request' when adding recipe |  |

## 4.4 Known Bugs

- The website is not optimised for Internet Explorer. No additional work was performed to optimise the site for IE as (extended) support has ended for customers since January 2020 and no further development of IE is expected.
- Reset function not updating database correctly.
- Collections page scrolls across page, throws off responsiveness of page on Mobile.
- Ingredients and methods written to MongoDB appears as single array item instead of list of arrays.
- Edit ingredients and Edit method in Edit Recipe page results in items being removed from database due to issue with JavaScript code. Further debugging required to resolve this issue.
