# django_api

This repository contains an implimentation of an API using the django pyhton library

## Getting started

clone this repository using
```
git clone https://github.com/vini7148/django_api.git
cd django_api
```

### Prerequisites

The following tools along with basic knowledge of python is required to execute this implimentation of API
```
python==3.7.3
django==2.2.6
djangorestframework==3.10.3
pytz==2019.3
sqlparse==0.3.0
```

### Installing

First you need to activate the python virtual environment (venv)
```
python -m venv 'name of the env' (already present in this repository)
```
To activate this env
* On windows (using git bash)
```
source 'name of the env'/Scripts/activate 
```
* On Unix/Linux
```
source 'name of the env'/Scripts/activate 
```
* On mac
```
source bin/activate
```

After activating the virtual env now run the django api by going into the djangoapi directory by
```
cd djangoapi
```

### Running

Now you can run the server by
```
python manage.py runserver
```

Now the server is up and runnig and you can view the same by going to
```
localhost:8000
```
in any web browser

## Deployment

This api can be used for transfering any form of data by simply edting the model.py file in "\djangoapi\courses"

## Built with

* [PYTHON](https://www.python.org/)
* [DJANGO](https://www.djangoproject.com/)
* [DJANGORESTFRAMEWORK](https://www.django-rest-framework.org)

## Authors

* **Vinayak Goswami** - *Initial work* - [vini7148](https://github.com/vini7148)