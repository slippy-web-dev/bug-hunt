# Bug Hunt

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#projectstructure)

## Requirements

* Python     >= 3.7
* Pip        >= 20.0.2 (latest)
* Virtualenv >= 20.0.7 (latest)
* Django     >= 3.0

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

https://docs.djangoproject.com/en/3.0/topics/install/

MySQL
https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/


## Usage

## Project Structure
```
.
├── Project Artifacts
│   ├── BugHound.vpp
│   ├── BugHound_ER_Diagram.JPG
│   ├── Bughound-use-case_ver1.1.docx
│   ├── Bughound-use-case_ver1.2.docx
│   ├── ProjectDocument_v1.0-(02-18-2020).docx
│   └── SampleUSECASE4Bughound.docx
├── README.md
├── bug_hunt
│   ├── bug_hunt
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── requirements.txt
└── src
```