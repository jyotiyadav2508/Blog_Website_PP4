# Incredible India - Introduction

This is my Portfolio Project 4, which is a Full Stack website built using the Django framework for Code Institute Full-stack development diploma.
> Incredible India is a blog website which targets **tourist destinations** of India, where user can view the blog post of tourist destinations. The user can view the detailed blog post and read comments. Also when the user is logged in, they can like/unlike a post and comment on a post. They can also share their blog post by adding a post on the user page.

You can view the live site here -

![Incredible India]()

----

## [Content](#content)
- [Incredible India - Introduction](#incredible-india---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [Site Aims](#site-aims)
    - [Agile Methodology](#agile-methodology)
      - [Epics and User Stories](#epics-and-user-stories)
      - [Tasks](#tasks)
  - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Database Diagram](#database-diagram)
  - [Features](#features)
    - [Home Page](#home-page)
      - [Navbar](#navbar)
      - [Hero Image](#hero-image)
      - [Destination Section](#destination-section)
      - [Footer](#footer)
    - [About Page](#about-page)
    - [Blog Page](#blog-page)
      - [Blog Details](#blog-details)
      - [Blog Comments](#blog-comments)
    - [Register](#register)
    - [Login](#login)
    - [Logout](#logout)
    - [Destinations](#destinations)
    - [Search Button](#search-button)
    - [Alert Messages](#alert-messages)      
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  - [Testing](#testing)
      - [Validation](#validation)
      - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Unfix Bugs](#fixed-bugs)
  - [Deployment](#deployment)
      - [Creating the Django project](#creating-the-django-project)
      - [Creating Heroku app](#creating-heroku-app)
      - [Set up Environment Variables](#set-up-environment-variables)
      - [Heroku deployment](#heroku-deployment)
      - [Final Deployment](#final-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Acknowledgement](#acknowledgement)

-----

# User Experience - UX

## Site Aims

* Incredible India is a website mainly meant to explore the Indian tourist destinattions with a good user experience.
* The site aims is to provide users with a visually pleasing and informative website that is intuitive to use and easy to navigate.
* This website provides the user with the ability to read and view posts, as well as tools that allow users to search for a particular destination posts.
* All users who sign up and sign in, can access the features of like/unlike and comment on a blog post of this website.
* Author can access all the features of the website and can read, create, edit, and delete their posts.

## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board. Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections: 

* To Do- (All the User stories were initially entered in the 'To Do' column)
* In Progress- (then during development story they were moved into the 'In Progress' column)
* Done- (and then finally they get moved into 'Done' once the development completes)

Please find my Kanban Board with my user stories [here](https://github.com/users/jyotiyadav2508/projects/3/views/1).

## Epics and User Stories

Following Epics were created which were further developed into ..... User Stories.

### Epic 1- Website UI
Epic Goals for User- 
* An intuitive User Interface with easy to navigate throughout the website 
* Easily see the purpose of the site from the landing page
* View a list of destinations and blog posts
* Search bar for quick and easy access to required information

#### Related User Stories:
* As a site user I can easily see the purpose of the site from the landing page so that I can see if the site is relevant to my needs.
* As a site user I can view a list of destinations so that I can see a list of posts relating to my specific interest.
* As a site user I can view a paginated list of posts so that easily select a post to view.
* As a site user I can click on a post so that I can read the full article.
* As a site user I can use a search bar to search for a specific place so that I have quick and easy access to the information I need.

### Epic 2- Registration and Account Management
Epic Goals-
* Easy registration of an account
* Easy Sign Up, Sign in and Sign Out
* Upon signing in, the user should be able to like, comment on a blog post
* Easy access to Create, Read, Update and Delete (CRUD) features upon signing in
* Visibility of personalized blog posts and comments

#### Related User Stories:
* As a site user, I can register an account so that I can comment and like.
* As a registered user, I can login and logout of the site so that I can access my content.
* As a site user, I can view the number of likes on each post so that I can see which is the most popular or viral.
* As a site user, I can view comments on an individual post so that I can read the conversation.
* As a author I can create a post of tourist place so that I can share it with other.

### Epic 3- Blog Post Management
Epic Goals-
* Create/ Update / Read / Delete blog posts.
* View their created blog posts
* Approve and publish a comment and post

#### Related User Stories:
* As a site admin/ author, I can create draft posts so that I can finish writing the content later.
* As a site admin/ author, I can create, read, update and delete posts to manage the blog content.
* As a site admin, I can approve or disapprove comments so that I can filter out objectionable comments.
* As a author, I can access all my blog posts easily in one place so that I can easily track my activity on the site.

### Epic 4- Comments and Like Management
Epic Goals-
* Add /Delete and View Comments on a post
* Like / Unlike a post

#### Related User Stories:
* As a logged-in user I can leave comments on a post so that I can be involved in the conversation.
* As a logged-in user I can edit/delete my comments so that I can update/delete my post opinion.
* As a logged-in user I can like or unlike a post so that I can interact with the content.

## Tasks

The tasks for the website development process was closely followed as mentioned in CI's Django module "I Think Therefore I Blog" walkthrough project. The task is generally the developers step towards preparing the app.
The tasks that I have followed during the development phase were carried out in this order.

**Before Project Inception**

- Design ERD and Data 
- Create Repository in GitHub
- Create Project, Epics, User Stories and prepare Kanban Board

**Creation of Project in GitPod**

- Create the django project. Check details in [deployment-section](#deployment)
- Deploying app to Heroku - Details in [deployment](#deployment) section
- Create Database Models
	- Set up models.py file in "blog" directory
- Build Admin site
- Set up Templates
	- Create base.html - Navbar and Footer content, which gets extended to all the other template files
	- Add responsiveness to navigation and footer
    - Create index.html, view and style
	- Set up template file features with views.py and urls.py
  - about.html (Description about incredible india)
  - blog.html (to view all blog posts)
  - author_page.html (for author's personal collections)
  - post_details.html (for detailed post view)
  - destinations_post.html (to view blog post for a selected destination)
  - add_post.html (to allow author's input for blog posts)
  - delete_post.html (to allow author to delete his post)
  - search.html (to search a blog post)
  - update_post.html (to allow author to edit his post)
  - author_post_list.html (to allow author to view all post, which he posted so far)
- Install Allauth for sign in, sign up and sign out tenplates with-  pip3 install django-allauth 
	- Install crispy-forms to add styles to Django account templates with-  pip3 install crispy-bootstrap5
- Intensive Manual Testing and Validation checks of each page and codes written
- Final Deployment steps

**Future Tasks**
- Automated Testing 

-----

## Design

### Colours

The colour scheme has considered based on easy accessibility for all and have been consistently maintained throughout the website.

### Typography

Fonts were imported using Google Fonts. Roboto was used throughout with a backup of sans-serif. It was chosen for easy readability for users.

### Imagery

All the imagery is related to the Indian tourist destination and website design. Some images including carousel are static. The remaining imagery was uploaded by the author to the database.

### Wireframes

The wireframes were generated at the start of the project using Balsamiq. 

----

## Database Diagram

...Smart Draw/ Lucid Chart ...was used to create a database schema to visualise the types of custom models the project requires. This schema was used as a guide to what needed to be added to each model. Below is the Database structure that this project is based on. The relationship between Entities User, Post and Comment....... are shown here.

[Back to top ⇧](#content)

----

# Features

## Home Page

At first glimpse, user can see a Navigation menu with a search button and carousel-images on the homepage. Homepage provides the user with some quick information about the site and make use of all its features. User do not need to be registered to view a blog post. The responsive navigation bar is featured on all pages. 

![Homepage](assets/features/home-page.jpg)

Upon scrolling down, there is destination section which describe different types of tourist destination. Each destination card navigate to that particular blog posts. 

![Destination](assets/features/destinations-section1.jpg)
![Destination](assets/features/destinations-section2.jpg)
![Destination](assets/features/destinations-section3.jpg)

User can also select a specific destination blog posts from the navbar dropdown which navigates to that specific destination blog posts.

![Destination](assets/features/dropdown-destination.jpg)

----

## About Us Page

The About Page gives, users information about the Incredible India with a brief discription of india and the travel options to reach there.

![About Us](assets/features/about-us1.jpg)
![About Us](assets/features/about-us2.jpg)

## Blog Page

This page enlists all the blog posts added so far to the website. The blog posts is paginated in a way that 9 posts are displayed. Further post can be accessed by clicking next button. Each blog post shows the image overlay with the destination type. and the card body displays blog post title with specific fields and sliced post content along with the name of author, submitted date and shows the number of likes and comment icon in the card footer.

![Blog Page](assets/features/blog-page1.jpg)
![Blog Page](assets/features/blog-page2.jpg)

## Post-Detail Page

- When a user clicks on the image or title of the blog post, they are brought to the post details page for the selected blog post. Here the user is shown a full description of the blog post with image, author name, created time, title, best-time, ideal-duration, full content along with number of likes and comments.
- Underneath the post description the page displays all the approved comments of that blog post posted by signed-in users. 
- At the bottom of this page, Comment box is visible to users.

![Blog Page](assets/features/post-details1.jpg)
![Blog Page](assets/features/post-details2.jpg)

- If user is signed-in, following comment box will appear. 

![Blog Page](assets/features/comment-box-login-user.jpg)

- When User submit a comment or like a post, following messages/ alert displays respectively.

![Blog Page](assets/features/comment-approval.jpg)
![Blog Page](assets/features/like-alert.jpg)



----

## Admin Panel/Superuser

On the Admin Panel, as an admin I have full access to CRUD functionality so I can view, create, edit and delete the following ones:
Posts
Comments
Author
Destination

* As admin I can also approve comments, approve posts and change the status and give other permissions to the users.

----

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)- Used to structure all the templates on the site
* [CSS 3](https://en.wikipedia.org/wiki/CSS)- to provide extra styling to the site
* [JavaScript](https://www.javascript.com/)- Minimum javascript was used to fade out alerts after a few seconds.
* [Python](https://www.python.org/)- To provide the functionality to the site. Packages used in the project can be found in requirements.txt

### Django Packages

* [Gunicorn](https://gunicorn.org/)- As the server for Heroku.
* [Cloudinary](https://cloudinary.com/)- Was used to host the static files and media for the site.
* [Dj_database_url](https://pypi.org/project/dj-database-url/)- To parse the database URL from the environment variables in Heroku.
* [Psycopg2](https://pypi.org/project/psycopg2/)- As an adaptor for Python and PostgreSQL databases.
* [Summernote](https://summernote.org/)- As a text editor.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- For authentication, registration, account management.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- To style the forms.

### Frameworks - Libraries - Programs Used

* [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
* [Bootstrap](https://getbootstrap.com/)- Used to style the website, add responsiveness and interactivity.
* [Git](https://git-scm.com/)- Used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
* [GitHub](https://github.com/)- Used to store the project's code after being pushed from Git.
* [Heroku](https://id.heroku.com)- Used to deploy the live project.
* [PostgreSQL](https://www.postgresql.org/)- Database used through heroku.
* [Balsamiq](https://balsamiq.com/)- To build the wireframes for the project.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) was used to inspect page elements, debug, troubleshoot and test features and adjust property values. Using the Lighthouse extension installed in Chrome Browser, the performance report was generated.
* [Google Fonts:](https://fonts.google.com/) used for the Roboto font
* [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.

-----

## Testing


----

## Bugs

destination dropdown was not displaing the list items. add in setting.py


----

## Deployment

### 1. Creating the Django Project
* Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click on `Use This Template` button, then create new repository.
* Name our repository and click on `Create repository from template` button.
* Once the template is available in your repository click on `Gitpod` button.
* When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App.
* Install Django and gunicorn: `pip3 install 'django<4' gunicorn`.
* Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url==0.5.0 psycopg2`.
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`.
* Create file for requirements: `pip freeze --local > requirements.txt`.
* Create project:`django-admin startproject project_name .`.
* Create app: `python manage.py startapp app_name`.
* Add app to list of `installed apps` in settings.py file: `'app_name'`.
* Migrate changes: `python manage.py migrate`.
* Test server works locally: `python manage.py runserver`.
* If the app has been installed correctly the window will display- The install worked successfully! Congratulations!

### 2. Create your Heroku app
* Navigate to [Heroku](https://id.heroku.com).
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account.
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app.
* Click Reveal Config Vars and add a new record with `DATABASE_URL`.
* Click Reveal Config Vars and add a new record with `PORT`.
* Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`(note: this must be removed for final deployment).
* Next, scroll down to the Buildpack section, click `Add Buildpack` select python and click Save Changes.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory.
* Add env.py to the .gitignore file.
* In env.py import the os library.
* In env.py add `os.environ["DATABASE_URL"]` = "Paste the link copied from Heroku DATABASE_URL".
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`.
* In Heroku Settings tab Config Vars enter the same `SECRET_KEY` created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 4. Setting up settings.py
* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku, click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: 
```ALLOWED_HOSTS = ['<Heroku_app_name>.herokuapp.com', 'localhost']```
* Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Commit and push the code to the GitHub Repository.

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku.
* Select Github as the deployment method.
* Confirm you want to connect to GitHub.
* Search for the repository name and click the connect button to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.
* Scroll to the bottom of the deploy page and select the preferred deployment type.
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github or To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

### 6. Final Deployment
In the IDE:




----

[Back to top](<#content>)

# Credits



----


# Acknowledgement




[Back to top](<#content>)
   
