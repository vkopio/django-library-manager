[![Build Status](https://travis-ci.org/V-Kopio/django-library-manager.svg?branch=master)](https://travis-ci.org/V-Kopio/django-library-manager)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2b80eb20505b4c97bc7601794a2e127b)](https://www.codacy.com/app/V-Kopio/django-library-manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=V-Kopio/django-library-manager&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/2b80eb20505b4c97bc7601794a2e127b)](https://www.codacy.com/app/V-Kopio/django-library-manager?utm_source=github.com&utm_medium=referral&utm_content=V-Kopio/django-library-manager&utm_campaign=Badge_Coverage)
[![Heroku Demo](https://img.shields.io/badge/heroku-demo-blue.svg)](https://django-library-manager.herokuapp.com)

# django-library-manager
A management system for a library using Django.


--------------------------------


## Setup development environment
Python version 3.6 is used. Add a virtual environment for it in the project root and activate it:

    python3 -m venv venv
    source venv/bin/activate

Install `pipenv` for package management:

    pip install pipenv

Install development packages with `pipenv`:

    pipenv install -d

Seed development database:

    python manage.py loaddata library_app/fixtures/*

--------------------------------


## Run development server

    python manage.py runserver


--------------------------------


## Architecture
In a Django project the project consists of a 'site' which wraps all the Django 'apps' together. Currently the 'site' 
is under the `library_site` directory and there is only one app under the `library_app` directory.

### Site library_site
The site combines app urls to a single `urls.py` file and contains the website layout which uses Bootstrap 4 as its
CSS framework.

### App library_app
This app contains the core functionality. 

#### Directory and file structure
In addition to the default Django app structure, models are divided to their own files to avoid a single bloated file. 
Also, there is the `sample` directory which contains "business" logic.

Test directory structure mimics the app structure rather than is divided by test types.

#### Database structure
The following diagram represents the designed database structure and not necessarily the current situation:

![Database diagram](doc/database_diagram.png)
