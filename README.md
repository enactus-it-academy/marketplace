# marketplace
Онлайн единая торговая сеть для рынков.
## Installation

Первое, что нужно сделать, это клонировать репозиторий:

```shell
$ git clone https://github.com/enactus-it-academy/marketplace.git
$ cd marketplace
```

Создайте виртуальную среду для установки зависимостей и ее активации:

```shell
$ virtualenv venv
$ source venv/bin/activate
```

Затем установите зависимости:

```shell
(venv)$ pip install -r requirements.txt
```

Применяем миграции и запускаем сервер:

```shell
(venv)$ python manage.py migrate
  ...
(venv)$ python manage.py runserver
```
