# Incredible India - Testing

:arrow_left: [Return to the README](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [PEP8 Validation](#pep8-validation)
- [Testing](#testing)
  - [Manual Testing (BDD)](#manual-testing-bdd)

## Performance

### Google's Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website. 
#### Desktop Results:
![Lighthouse Mobile Result](./assets/testing/desktop-lighthouse.jpg).

#### Mobile Results:
![Lighthouse Desktop Result](./assets/testing/mobile-lighthouse.jpg).

*Go back to the [top](#table-of-contents)*

## Code Validation

### HTML Validation
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.
All the Django templates html files hava been manually copying the source of the rendered pages and then validating using the W3C Validator.
 - Result for [home page](./assets/testing/W3C-home-page.jpg)
 - Result for [about page](./assets/testing/W3C-about-page.jpg)
 - Result for [blog page](./assets/testing/W3C-blog-page.jpg)
 - Result for [post-detail page](./assets/testing/W3C-post-detail.jpg)
 - Result for [user page](./assets/testing/W3C-user-page.jpg)
 - Result for [add-post page](./assets/testing/W3C-add-post.jpg)
 - Result for [update post](./assets/testing/W3C-update-post.jpg)
 - Result for [delete post](./assets/testing/W3C-delete-post.jpg)
 - Result for [edit comment](./assets/testing/W3C-edit-comment.jpg)
 - Result for [search page](./assets/testing/W3C-search-page.jpg)


### CSS Validation 
[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used for validating the CSS stylesheet. CSS file was tested by manually copying the CSS codes into the manual input option.

- The result can be seen [here](assets/testing/css-validator.jpg).

### PEP8 Python Linter Test
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) was used to check that the Python code meets PEP8 standards.

### Blog
* [admin.py](./assets/testing/pep8-admin-py.jpg)
* [models.py](./assets/testing/pep8-models-py.jpg)
* [forms.py](./assets/testing/pep8-forms-py.jpg)
* [urls.py](./assets/testing/pep8-urls-py.jpg)
* [views.py](./assets/testing/pep8-views-py.jpg)

## Manual Testing (BDD)

BDD, or Behaviour Driven Development, is the process used to test user stories in a non-technical way, allowing anyone to test the features of an app.

User Story | BDD Test | Pass
--- | --- | :---:
As a first time site user <br>I can easily see the purpose of the site from the landing page<br> so that I can see if the site is relevant to my needs. | Given that I'm a first time user<br>When I view/scroll down the homepage<br>Then I should see what the purpose of the site is and easy navigation throughout the website. | :white_check_mark:
As a first time site user <br>I can view a paginated list of posts<br>so that easily select a post to view.|Given that I'm a first time user<br>When I view the blog page<br>Then I view a list of blog posts. | :white_check_mark:
As a site user <br>I can view a list of post specific to a certain destination place <br>so that I can view most relevent post I am searching for. | Given that I'm a site user <br>When I click on destination dropdown<br>Then I should select any destination and view all posts within that destination. |:white_check_mark:
As a site user <br> I can view the number of likes and comments on each post <br>so that I can see which one is the most popular or viral and read the conversation on an individual post. | Given that I'm a site user<br>When I view the post detail page<br>Then I view the number of likes and list of comments on that post. | :white_check_mark:
As a site user <br>I can register an account <br>so that I can comment and like on a post. | Given that I'm a site user<br>When I register an account on homepage<br>Then I can access the main functionality of the site. | :white_check_mark:
As a registered user<br>I want to be able to easily login/log out<br>So that I can access my information without registering every time and ensure the security of my account. | Given that I'm a site user<br>When I login/log out<br>Then I can access my information without registering every time and ensure the security of my account. |:white_check_mark:
As a logged in user <br>I can like/unlike and leave a comment on a post<br> so that I can be involved in the conversation. | Given that I'm a logged in user<br>When I am on post detail page<br>Then I can like/unlike and leave a comment on the post. |:white_check_mark:
As a site user<br>I can use a search bar to search for a specific place <br>so that I have quick and easy access to the information I need. | Given that I'm a site user<br>When I use the search bar<br>Then I should see specific post/s that match my search query. |:white_check_mark:
As a site user<br>I want to be able to receive a feedback for my action<br> so that I know my inputs are working. | Given that I'm a site user<br>When I register,login/logout, access CURD functionality for a post<br>Then I should receive a confirmation message.| :white_check_mark:
As an author <br>I can access all my posts easily in one place <br>so that I can easily track my activity on the site. |Given that I'm a author of post<br>When I am logged in and navigate to user-page<br>Then I can view all of mine posted blog post.| :white_check_mark:
As an author/user<br>I can fully access the CURD functionality <br> so that I can manage my blog content. | Given that I'm an author/user<br>When I am logged in and navigate to user-page <br>Then I need to be able to CURD mine post content on the website.| :white_check_mark:
As a site admin<br>I want to be able to review all posts, destinations, users, comments, etc <br>So that I can maintain the site and remove any offensive content. | Given that I'm a site admin<br>When I navigate to the admin panel<br>Then I should see all posts, destination, comments, likes, etc. | :white_check_mark:
As a site admin <br>I can approve or disapprove comments<br>so that I can filter out objectionable comments.| Given that I'm a site admin<br>When I navigate to the comment model in admin panel<br>Then I need to be able to approve or disapprove any comments.| :white_check_mark:
As a site admin<br>I want to be able to create/edit/update/delete a post <br>	so that I can maintain the site and remove any offensive content. | Given that I'm a site admin<br>When I navigate to the admin panel<br>Then I need to be able to control all the content on the website.| :white_check_mark:
As a site admin<br>I want to be able to direct users to my social profiles<br> So that I can increase social interaction and attract new users. | Given that I'm a site admin<br>When I view/scroll down to the footer<br>Then I should see working links to my social media. | :white_check_mark:
As a site admin<br>I want to be able to ensure that all areas of the site to function correctly and have no bugs<br> so that I can ensure an enjoyable browsing experience for all users. | Given that I'm a site admin<br>When I check all site functionality<br>Then I should see that everything works as expected, there are no bugs and all links and forms work as expected | :white_check_mark: