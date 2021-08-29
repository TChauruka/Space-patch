# [Space Patch](https://space-patch.herokuapp.com/)

<div align="center">
    <img src="static/img/website.png" href="https://space-patch.herokuapp.com/" target="_blank" alt="Space Patch Picture"/>
</div>

## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Current Features](#current-features)

3. [Database](#database)
    - [Database choice](#db-choice)

4. [Technologies Used](#tech)
    - [Languages](#languages)
    - [Frameworks & libraries](#libraries)
    - [Databases](#db)
    - [Tools](#tools)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#depl-heroku)
    - [Local Deployment (GitPod)](#depl-gitpod)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#ack)

<a name="ux"/>

# UX

**Project definition**
- Space Patch is the first website that brings you the latest space patches as they come out and the latest news about space.
- The purpose of this web app is to provide customers who would like to own one of their own space patch and catch up with what is going on in the space world 
- Users can browse for all the patches from many defferent rocket companies. 

<a name="user-stories"/>

## User Stories

As a user, I expect:
1. To have convenient access to all the patcheson  offers.
2. The website to have a neat and elegant design with an optimal architecture and layout.
3. The website to be intuitive and easy to navigate so that I can find what I need in the most effective manner.
4. To easily find information i.e. identify key information for a patch , be able to access more details.
5. To read the comments on the blog   
6. To be able to but a patch and then register/log in to an account with minimal steps to confirm my order.
7. The website to display my order details for each steps of the checkout and receive an email once my booking has been completed.
8. The website to be fully responsive on any devices: mobile, tablet, desktop. 
9. The website to be fully interactive so that I get clear feedback on any action I undertake (complete a form, process a payment, log in, log out etc…). 
10. As a client, I want to be able to access (and update) my personal information, upcoming and post bookings.  

<a name="design"/>

## Design

### Theme

I wanted to create a website that would "bring" the user to space. I wanted to keep it classy and professional as well. I have tried to put some efforts on selecting visually impacting pictures. 

### Colors

The three main colors were used throughout this project.

1. White - `#fff` 
2. Black - `#161616`

<a name="wireframes"/>

## Wireframes

- [Home](https://ibb.co/4VbS8GV)
- [Products](https://ibb.co/rmFRNRT)
- [Profile](https://ibb.co/xjhnwhy)
- [Blog](https://ibb.co/7G09K9h)
- [Blog Deatils](https://ibb.co/HKFnGfs)
- [Product Detail](https://ibb.co/BzYKRcH)
- [Bag](https://ibb.co/hYzZtkC)
- [Toast](https://ibb.co/sQdNMhJ)


## Current Features

###### Feature 1 - Home page
Home page with:
- search bar to search the products
- list of products, launch companies,special offers and blog
- acconts button
- shopping bag
- button to products page

###### Feature 2 - products Page
- shows all products 
- sorting for the products

###### Feature 3 - product detail page
- image of the prodoct
- information of the product
- quantity of the product
- keep shopping and add to bag button

###### Feature 3 - blog page
- shows all blogs and thier images
- continue rreading button

###### Feature 4 - blog detail page
- image of the blog 
- title of the blog
- comments on the blog 
- add comments button

###### Feature 5 - Checkout
Checkout process step by step with the following pages:
- (log in / sign up if the user is not logged in yet)
- contact details form
- forms to register passengers
- payment form
- confirmation of order booked
- for each step of the checkout process, a recap of the cart is available as well as a return button to get back to the previous step. 

###### Feature 6 - Sign up page
Sign up form to register to an account.

###### Feature 12 - Login page
Form to log in to your account.

<a name="database"/>

# Database

<a name="db-choice"/>

## Database choice

- Development: I used sqlite3 database which is the default database provided by Django. 
- Production: I used PostgreSQL for my deployed application hosted on Heroku. 

<a name="tech"/>

# Technologies Used

<a name="languages"/>

## Languages

##### [HTML5](https://www.w3.org/TR/html/)
- I used HTML to create the static content of my website.
- The following [code validator](https://validator.w3.org/) was used to test my HTML code.

##### [CSS3](https://www.w3.org/Style/CSS/)
- I used CSS to style my website and personalize it.  
- The following [code validator](https://jigsaw.w3.org/css-validator/) was used to test my CSS code.

##### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- I used core JS in coordination with Sweet Alert library.
- [JSHint](https://jshint.com/) was used to check my JS code quality.

##### [Python 3](https://www.python.org/downloads/release/python-374/)
- I used Python 3 as the back-end programming language for my application.

<a name="libraries"/>

## Frameworks & Libraries

##### [Django 3](https://www.djangoproject.com)
- I used Django 3 as Python framework to build this website. 

##### [Bootstrap](https://getbootstrap.com/)
- I used Bootstrap as the main framework for HTML.

##### [jQuery](https://jquery.com/) 
- I used jQuery to simplify the DOM manipulation.

##### [Font Awesome](https://origin.fontawesome.com/)
- I used Font Awesome to display icons.

##### [Google Fonts](https://fonts.google.com/)
- I used google fonts for my main font families.

<a name="db"/>

## Databases

##### [SQLite3](https://www.sqlite.org/releaselog/3_32_3.html)
- I used sqlite as database during the development stage.

##### [PostgreSQL](https://www.postgresql.org/)
- I used PostgreSQL as database in production. 

<a name="tools"/>

## Tools

##### [Balsamiq](https://balsamiq.com/) 
- I used Balsamiq to design my wireframes.

##### [Gitpod](https://gitpod.io/)
- I used Gitpod as my IDE for this project.

##### [Amazon S3](https://aws.amazon.com/s3/)
- I used Amazon Simple Storage Service to store my static and media files.

##### [Stripe](https://stripe.com/)
- I used Stripe for secure credit card payment validation.

##### [Git & GitHub](https://github.com/)
- I used Git for version control. 
- I used GitHub to store my code in a remote repository.

##### [Heroku](https://dashboard.heroku.com)
- I used Heroku to deploy and host my application.

<a name="testing"/>

# Testing 
## Manual testing

### Responsiveness

- **Plan:** this game was planned to be responsive, working on all devices - mobile phones, tablets and desktops. Following this it was planned for Bootstrap library to be used for a page design.
- **Implementation:** page was **tested in Chrome Developer Tools** throughout the process of putting it together to make sure it was responsive to all devices. "Responsive" slider was used to make sure content is shown correctly on desktop, tablet and mobile, that they look as desired by the developer. Bootstrap classes as well as media rules were used to adjust responsiveness.
**Tested** the pages **on** all sizes/devices **available in Chrome**, these were:
  - 360 x 640 Blackberry Z30 & Galaxy Note
  - 375 x 812 iPhone X
  - 375 x 687 iPhone 6/7/8
  - 411 x 731 Pixel 2
  - 411 x 823 Pixel 2 XL
  - 414 x 736 iPhone 6/7/8 Plus
  - 600 x 1024 Blackberry Playbook
  - 768 x 1024 iPad
  - 1024 x 1366 iPad Pro

- **Results:** page is responsive and can be used on all planned devices. There are no elements on this page that are not responding as planned.
- **Conclusion:** all tests that were run on responsiveness were passed therefore page is fully responsive.

### Interaction

- **Plan:** there are elements that are planned to be interactive on this page, these are buttons, cards and modals
- **Implementation:** was carried out on many devices and on several browsers, including Chrome, Firefox and Opera. Following elements were tested:
  - Win modal:
    - confirmed that clicking close in this modal reloads the game
    - confirmed that there is no possibility to click on the backdrop of this modal
    - confirmed that there is no possibility of closing this modal using keyboard
  -Reset button:
    - confirmed that after the button has been pressed it will show an new order of cards

- **Results:** all tested elements are interactive as planned . There are no elements on this page that are not responding as planned
- **Conclusion:** all tests that were run on interactivity were passed therefore page is interactive


## User stories testing

1. As a user I want to play easy but not too involving game to kill spare time (eg. during travel etc.):
    - this game is perfect to play in spare time, it is easy to operate, engaging and not too complicated
    - playing this game does not require too much concentration therefore can be played on the move
    - easy and quick game for a user to keep themselves occupied during spare time

2. As a user and a parent I want the game that is easy enough for my children to operate:
    - game that requires matching 2 cards only is not too complicated even for very young children
    - game is easy to operate - just couple of clicks gets children engaged and challenged
    - game allows user to pick easy level that requires matching only 4 pairs

3. As a user I want to play the game that is visually appealing:
    - game is very colourful and nice looking
    - game presents user with characters that attract attention
    - fonts and colours used evoke emotion


## Automated testing

Following online validators were used to test the code:

- [W3C Mark-up Validation Service](https://validator.w3.org/) for HTML validation
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for CSS validation
- [Esprima](https://esprima.org/) for JavaScript validation
### HTML validation

| Error message | Action taken|
|-----|-----|
| Bad value https://fonts.googleapis.com/css?family=Gloria+HallelujahPermanent+Marker | No action taken as link was taken from Google. |
| Section lacks heading. Consider using h2-h6 elements | no action taken as no h2-h6 required for the part of the code. |
| The type attribute on the li element is obsolete. | no action taken as the card class is used in the CSS file. |

### CSS validation

No errors found.

### JavaScript validation
No errors found.

<a name="deployment"/>

# Deployment

<a name="depl-heroku"/>

## Heroku

My application was deployed through [heroku](https://dashboard.heroku.com) using the master branch of my github repository for this project. The following steps were implemented to deploy this project:

1. Install **gunicorn** package to run the application on Heroku.
    - `sudo pip3 install gunicorn`
2. Install **pycopg2** to connect to PostgreSQL
    - `sudo pip3 install psycopg2`
3. Create a **requirements.txt** file
    - `sudo pip3 freeze --local > requirements.txt`
4. Create a new Heroku application
    - Sign up to a new account if you do not already have one.
    - Create a new application by clicking on `new` then `create new app`.
    - Set the name of your application and select your region and click on `create app` to finalize the creation of your app. 
5. Install PostgreSQL add-on
    - `heroku addons:create heroku-postgresql:hobby-dev`
6. Create a **Procfile** in the root directory
    - content: `web: gunicorn spacex.wsgi:application`
7. Set the following config variables as environment variables:

Config Vars | Value
----------- | -------------
AWS_ACCESS_KEY_ID | `<AWS_ACCESS_KEY_ID>`
AWS_SECRET_ACCESS_KEY | `<AWS_SECRET_ACCESS_KEY>`
DATABASE_URL | `<DATABASE_URL>`
EMAIL_HOST_PASSWORD | `<EMAIL_HOST_PASSWORD>`
EMAIL_HOST_USER | `<EMAIL_HOST_USER>`
EMAILJS_USER | `<EMAILJS_USER>`
GOOGLE_API_KEY | `<GOOGLE_API_KEY>`
HOSTNAME | `<HOSTNAME>`
SECRET_KEY | `<SECRET_KEY>`
STRIPE_PUBLISHABLE | `<STRIPE_PUBLISHABLE>`
STRIPE_SECRET | `<STRIPE_SECRET>`
USE_AWS | `<TRUE>`

5. In the `Deploy` tab, choose `Connect Github` as **Deployment Method** and *Enable Automatic Deployment* from the Github master branch so that any new commit will be automatically deployed through your heroku app. 


<a name="depl-gitpod"/>

## Local Deployment (GitPod)

To deploy this project locally using gitpod you will have to create a gitpod account and use a web browser with a stable internet connection as gitpod is an online IDE. I suggest you use Chrome as web browser so that you can use gitpod chrome extension to speed up the deployment process. 

1. Create a Gitpod account (if not already)
    - Go to [GitPod](https://www.gitpod.io)
    - Click on `Go to App` and click on the green `Authorize gitpod.io`
    - Agree to the terms and then create your free account
2. Add gitpod browser extension for Chrome:
    - Go to [GitPod Chrome Browser Extension](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki)
    - Search for "gitpod" in chrome web store search bar
    - Click on `Add to Chrome` then click on `Add to extension`
3. Clone this project repository from github
    - Go to my [repository](https://github.com/AlexiaDelorme/project-spacex) for this project.
    - If you successfully installed the gitpod browser extension you should view a green `Gitpod` button in the top right corner of the repository (next to `Clone or download` button). Click the `Gitpod` button. 
    - This will allow you to open this repository directly in gitpod for editing.
4. Set the following environment variables for the project:

Env Vars | Value
----------- | -------------
AWS_ACCESS_KEY_ID | `<AWS_ACCESS_KEY_ID>`
AWS_SECRET_ACCESS_KEY | `<AWS_SECRET_ACCESS_KEY>`
EMAIL_HOST_PASSWORD | `<EMAIL_HOST_PASSWORD>`
EMAIL_HOST_USER | `<EMAIL_HOST_USER>`
EMAILJS_USER | `<EMAILJS_USER>`
GOOGLE_API_KEY | `<GOOGLE_API_KEY>`
HOSTNAME | `<HOSTNAME>`
SECRET_KEY | `<SECRET_KEY>`
STRIPE_PUBLISHABLE | `<STRIPE_PUBLISHABLE>`
STRIPE_SECRET | `<STRIPE_SECRET>`

5. The default local database for django projects is SQLite 3.
6. Download all the dependencies necessary to run this project and listed in the **requirements.txt** file. 
    - Run the following command `pip3 install -r requirements.txt`
7. Create a local development server:
    - In the workspace run the following command `Python3 manage.py runserver`.
    - You should now have a gitpod link to the deployed app. 


<a name="credits"/>

# Credits

<a name="content"/>

### Content
- most of the content and images on the blog app was from [EverydayAstronaut](https://everydayastronaut.com/)

<a name="media"/>

### Media

- All the images used for this project were found on [spacepatches](http://www.spacepatches.nl/).
- I used [Font Awesome](https://fontawesome.com/v4.7.0/icons/) for my icons.
- Demo picture of my app used in this README file: [Am I Responsive](http://ami.responsivedesign.is/#)

<a name="code"/>

### Code)
- [Collapsable](http://jsfiddle.net/hungerpain/eK8X5/7/)
- [Progress Bar](https://codepen.io/cavellblood/pen/NNNbbg)
- [Django Email](https://stackoverflow.com/questions/2809547/creating-email-templates-with-django)
- [Corey Schafer's Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

<a name="ack"/>

### Acknowledgements
- To my  Code Institute mentor, Reuben Ferrante, for his patience and great support throughout this project.
- The entire team of tutors at Code Institute for their guidance and patience. 