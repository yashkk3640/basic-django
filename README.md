Virtual Environment installed on `user\.virtualenvs\basic-django-<extra>`

First `pipenv install django`
Second `pipenv shell`
Third `django-admin`
Fourth `python manage.py runserver`

`rm -rf venv` to use to remove environment

`python manage.py makemigrations` need to fire after changing the model info which do compare and make old data workable
`python manage.py migrate`

Store dep in file
`pip freeze > requirements.txt`

apply dep in project
`pip install -r requirements.txt`
