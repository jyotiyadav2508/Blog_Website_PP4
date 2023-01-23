# Incredible India - Project Portfolio 4

This project is a Full Stack website built using the Django framework for Code Institute Full-stack development program.
> Incredible India is a blog website which targets India's tourist places, where user can look or search for a tourist place in India. When the user is logged in they can also like/unlike a post and comment on a post. They can also share their favourite place by adding a post on the ---- Page and upload or update their user image and details.

You can view the live site here -

![Incredible India]()

## Deployment

### 1. Creating the Django Project
* Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
* Click on `Use This Template` button, then create new repository
* Name our repository and click on `Create repository from template` button
* Once the template is available in your repository click on `Gitpod` button
* When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App
* Install Django and gunicorn: `pip3 install 'django<4' gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url==0.5.0 psycopg2`
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
* Create file for requirements: `pip freeze --local > requirements.txt`
* Create project:`django-admin startproject project_name .`
* Create app: `python manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: `python manage.py migrate`
* Test server works locally: `python manage.py runserver`
* If the app has been installed correctly the window will display- The install worked successfully! Congratulations!

### 2. Create your Heroku app
* Navigate to the Heroku website
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app
* On the Heroku dashboard, click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.