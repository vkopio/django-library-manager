[![Build Status](https://travis-ci.org/V-Kopio/django-library-manager.svg?branch=master)](https://travis-ci.org/V-Kopio/django-library-manager)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2b80eb20505b4c97bc7601794a2e127b)](https://www.codacy.com/app/V-Kopio/django-library-manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=V-Kopio/django-library-manager&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/2b80eb20505b4c97bc7601794a2e127b)](https://www.codacy.com/app/V-Kopio/django-library-manager?utm_source=github.com&utm_medium=referral&utm_content=V-Kopio/django-library-manager&utm_campaign=Badge_Coverage)

# django-library-manager
A management system for a library using Django.

## Setup development environment
Python version 3.6 is used. Add a virtual environment for it in the project root and activate it:

    python3 -m venv venv
    source venv/bin/activate

Install `pipenv` for package management:

    pip install pipenv

Install development packages with `pipenv`:

    pipenv install -d

## Run development server

    python manage.py runserver
