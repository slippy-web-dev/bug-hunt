# Bug Hunt

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Webserver](#running-the-webserver)
- [Project Structure](#project-structure)

---

## Requirements

- Python     >= 3.7
- Pip        >= 20.0.2 (latest)
- Virtualenv >= 20.0.7 (latest)
- Django     >= 3.0

---

## Installation

Create a virtual environment called 'env' using Python3.7
Then activate your enviornment

```bash
virtualenv -p Python3.7 env
source env/bin/activate
```

Install all requirements using pip
NOTE: please ensure you are in the repo's root directory

```bash
pip install -r requirements.txt
```

~~https://docs.djangoproject.com/en/3.0/topics/install/~~

~~MySQL~~
~~https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/~~

---

## Usage

### Running the Webserver

To run the webserver during development; ensure you are in your virtual environment

```bash
python ./bug_hunt/manage.py runserver
```

This will run a small webserver at 127.0.0.1:8000

### Application routes

Append to 127.0.0.1:8000

- /app
  - Webapp's index and main entry point

---

## Project Structure

```
.
├── Project_Artifacts
│   ├── BugHound.vpp
│   ├── BugHound_ER_Diagram.JPG
│   ├── Bughound-use-case_ver1.1.docx
│   ├── Bughound-use-case_ver1.2.docx
│   ├── ProjectDocument_v1.0-(02-18-2020).docx
│   └── SampleUSECASE4Bughound.docx
├── README.md
├── bug_hunt
│   ├── app         <---- This is where the application resides
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── bug_hunt    <---- This is the 'project' folder
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   └── manage.py
└── requirements.txt
```

---

## Useful commands

Print project directory

```bash
tree -I 'env|__pycache' .
```

Django migration stuffs

```bash
# Updating Django models (and subsequent DB schema)
python manage.py makemigrations app

# Updating DB to match Django models
python manage.py migrate

# Checking (for errors) migrations before making migrations
python manage.py check
```
