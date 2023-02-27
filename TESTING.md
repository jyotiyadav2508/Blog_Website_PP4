# Incredible India - Testing

:arrow_left: [Return to the README](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [PEP8 Validation](#pep8-validation)
- [Testing](#testing)
  - [Manual Testing (BDD)](#manual-testing-bdd)

## Performance

### Google's Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website. 
#### Desktop Results:
![Lighthouse Mobile Result](./assets/readme/test/).

#### Mobile Results:
![Lighthouse Desktop Result](./assets/readme/test/...).

*Go back to the [top](#table-of-contents)*

## Code Validation

### HTML Validation
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.
All the Django templates html files hava been manually copying the source of the rendered pages and then validating using the W3C Validator.

- The results can be seen [here](assets/validation/.....pdf).

### CSS Validation 
[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used for validating the CSS stylesheet. CSS file was tested by manually copying the CSS codes into the manual input option.

- The result can be seen [here](assets/validation/.....).

### PEP8 Python Linter Test
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) was used to check that the Python code meets PEP8 standards.

### Blog
* [admin.py](./assets/readme/test/pep8/....)
* [apps.py](./assets/readme/test/pep8/.....)
* [models.py](./assets/readme/test/pep8/......)
* [apps.py](./assets/readme/test/pep8......)
* [forms.py](./assets/readme/test/pep8/......)
* [signals.py](./assets/readme/test/pep8......)
* [urls.py](./assets/readme/test/pep8......)
* [views.py](./assets/readme/test/pep8/......)

## Manual Testing (BDD)

BDD, or Behaviour Driven Development, is the process used to test user stories in a non-technical way, allowing anyone to test the features of an app.

User Story | BDD Test | Pass
--- | --- | :---:
As a first time user<br>I want to know what is expected of me on the home page<br>So that I can read some blog posts navigate the site and decide on whether or not I want to sign up | Given that I'm a first time user<br>When I view/scroll down the homepage<br>Then I should see what the purpose of the site is, easy navigation, a link to sign up and some news stories | :white_check_mark:
As a first time user<br>I want to be able to<br>read posts and comments, So that I can<br>decide on whether or not I think it is worth signing up to. | Given that I'm a first time user<br>When I view/scroll down the homepage<br>Then I read posts and comments, a link to sign up and some news stories | :white_check_mark: