#   SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
## Django REST framework is a powerful and flexible toolkit for building Web APIs.

## Requirements

- Python 3.6
- Django 3.1
- Django REST Framework
APIS:

## API Documentation : https://documenter.getpostman.com/view/27498901/2s9XxtyFQy

## Clone the Project
Clone the project and  do the following steps:

### 1.1 Setup Vertual Environment:

It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

Create virtual environment after cloning the repo

Open that clone folder location and type

#### Windows cmd : 
` py -m venv envname `

#### Unix/MacOS Terminal : 
` python -m venv envname `

### 1.2 Activate the environment, by typing this command:

#### Windows cmd :
` envname\Scripts\activate.bat `

#### Unix/MacOS Terminal : 
` source envname/bin/activate `

Once the environment is activated, you will see this result in the command prompt:

#### Windows cmd :

` (envname) C:\Users\Prashant> `

#### Unix/MacOS Terminal : 
` (envname) ... $ `

### 2.1  Django Installation:

#### Windows cmd : 
` py -m pip install Django `

#### Unix/MacOS Terminal : 
` python -m pip install Django `

Change directory to project where requirements.txt file lies:

You can install all the required dependencies by running below command:

` pip install -r requirements.txt `


#### Run the project:

` py manage.py runserver `












Activate Virtual Environment:
` ipo\scripts\activate`

Change Directory to Project:

`cd crud_api_project`

Install Requirements:

`pip install -r requirements.txt`

Runserver:

`python manage.py runserver`

now good to go with http://localhost:8000/api/v1/user


<br>
<br>
<br>

# Django Mostly Used Commands You must know:
## Installation
### Step 1: Install Python and Django
`python ---version `
 
`django-admin --version`

### 1.1 Python Installation:
<b>Windows : </b> https://www.python.org/downloads/windows/

<b>Linux : </b> Download Require Version from here : https://www.python.org/downloads/source/

and type in terminal `  sudo apt-get install python3.8 `

<b>MacOS  : </b> https://www.python.org/downloads/macos/



### 1.2  Django Installation:

#### Windows cmd : 
` py -m pip install Django `

#### Unix/MacOS Terminal : 
` python -m pip install Django `


### Step 2 : Setup Vertual Environment and Create django project:

### 2.1 Setup Vertual Environment:
It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

#### Windows cmd : 
` py -m venv envname `

#### Unix/MacOS Terminal : 
` python -m venv envname `

Then you have to activate the environment, by typing this command:

#### Windows cmd :
` myworld\Scripts\activate.bat `
#### Unix/MacOS Terminal : 
` source myworld/bin/activate `

Once the environment is activated, you will see this result in the command prompt:

#### Windows cmd :

` (envname) C:\Users\Prashant> `

#### Unix/MacOS Terminal : 
` (envname) ... $ `


#### Install the Django:
Django is installed using pip, with this command:

#### Windows cmd :
(envname) C:\Users\Prashant> ` py -m pip install Django `

#### Unix/MacOS Terminal : 

(envname) ... $ ` python -m pip install Django `

### 2.2 Create django project:

` django-admin startproject crud-api-project `

#### Run the project:
` py manage.py runserver `

#### Create the app:
` py manage.py startapp user `

#### When you update the model :
 If change in the Model's structure, and therefor we have to make a migration to tell Django that it has to update the database:

 ` py manage.py makemigrations `

 You will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder.

Run the migrate command:

 ` py manage.py migrate `

#### Create SuperUser
To be able to log into the admin application, we need to create a user.

This is done by typing this command in the command view:

` py manage.py createsuperuser` 

### To create the rest api in django install the following dependencies

` pip install djangorestframework `

`pip install markdown    ` # Markdown support for the browsable API.


` pip install django-filter ` # Filtering support


Add 'rest_framework' to your INSTALLED_APPS setting.py

```python
INSTALLED_APPS = [
 'rest_framework',
 'django_filters',
] 

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

```
### Requirement.txt

A requirement.txt python file is a type of file that usually stores information about all the libraries, modules, and packages specific to the project used while developing a particular project. This article will guide us in creating a requirements.txt file in Python and installing dependencies from the requirements.txt file. We will be looking into various ways to create requirements.txt in Python.

### To create  requirements.txt  file :

`pip freeze > requirements.txt `

You can install all the required dependencies by running below command:

` pip install -r requirements.txt `


