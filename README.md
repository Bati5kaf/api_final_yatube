# API Yatube
####Author: Batiskaf/Encoded
#### Technologies: Django ORM, Django REST

Проект **API Yatube** позволяет отправлять запросы к сайту **YaTube**,
при этом не находясь  на нём.

Проект работает на версии __Python 3.9__ .

## Запуск проекта

Чтобы развернуть проект вам нужно:

**1. Развернуть и активировать виртуальное окружение.**


   - Для Windows
   ```bash
      py -3.9 -m venv venv
      source venv/Scripts/activate
   ```
   - Для MAC и Linux
   ```bash
      python -m venv venv 
      source venv/bin/activate
   ```
**2. Установить зависимости.**
````bash
    pip install  -r requirements.txt
````
**3. Применить миграции (сделать если изменились модели)**
   ```bash
      cd yatube_api
      python manage.py migrate
   ```
**4. Запустить проект.**
```bash
    python manage.py runserver
```

## Запросы

Чтобы сделать запросы через, например, **PostMan**
вам нужно зарегестрировать пользователя, 
это можно сделать 2 способами:
1. Создать суперпользователя через терминал.
```bash
    cd yatube_api    
    python manage.py createsuperuser
```
2. Или же с помощью самого **PostMan**'a:

    Для этого нужно отправить POST запрос по адресу `http://127.0.0.1:8000/api/v1/users/`
```json
    # такой запрос нужно передать (необязательно именно такой,
это пример)
    {
      "username":"batiskaf",
      "password": "MoyParolOchenSlogni123"
    }
    #такой ответ вам должен вернуться
    {
    "email": "",
    "username": "batiskaf",
    "id": 4
    }
```
После создания пользователя вам доступны такие возможности
запросов. 

_все показывать не буду их можно посмотреть здесь -> `http://127.0.0.1:8000/redoc/`_

## И так примеры запросов:
Пример __POST__ запроса по адресу `http://127.0.0.1:8000/api/v1/posts/` (создание поста):
```json
  # примерные данные для запроса
  {
  "text":"some text"
  }
  # ответ
  {
    "id": 1,
    "author": "artem", #ваш username
    "text": "some text",
    "pub_date": "2023-03-31T17:26:38.550489Z",
    "image": null, # необязательно поле
    "group": null # необязательное поле
  }
```

Пример __GET__ запроса по адресу `http://127.0.0.1:8000/api/v1/posts/` (получение всех постов):

```json
   # пример ответа, здесь данные передавать не нужно
   [
   ... # здесь будут остальные возможные посты
    {
        "id": 1,
        "author": "artem",
        "text": "some text",
        "pub_date": "2023-03-31T17:26:38.550489Z",
        "image": null,
        "group": null
    }
    ... # тут тоже
   ]
```
Пример GET запроса по адресу `http://127.0.0.1:8000/api/v1/posts/{post_id}/`, где `post_id` это __ID__ конкретного поста:

_В моём случае я буду обращаться по адресу `http://127.0.0.1:8000/api/v1/posts/1/`_
```json
   # пример ответа, здесь данные тоже не нужны

   {
    "id": 1,
    "author": "artem",
    "text": "some text",
    "pub_date": "2023-03-31T17:26:38.550489Z",
    "image": null,
    "group": null
   }
```
Примерно также работают **endpoint**'ы :

`http://127.0.0.1:8000/api/v1/posts/comments/`