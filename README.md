# sc-rest-api


## Installation

```
git clone https://github.com/tab-ai/sc-rest-api
cd sc-rest-api
pip3 install -r requirements.txt
```

## Quick Start (SQLite)

```
python3 manage.py makemigrations bt
python3 manage.py migrate
python3 manage.py runserver 0:80
```

## Mysql Start (Not tested yet)
cf. https://docs.djangoproject.com/en/2.0/ref/databases/

```
# sc_project/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}


# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```
