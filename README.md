# API Yamdb — программный интерфейс для социальной сети
### Описание
Благодаря этому проекту можно находить произведения по жанрам и категориям и делиться ими с зарегистрированными пользователями, оставлять и читать рецензиями, которые можно комментировать.
### Технологии
- Python 3.7
- Django 2.2.19
- DjangoRestFramework 3.12.4
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```

### Описание эндпоинтов (еще в разработке)
Запросы к API начинаются с /api/v1/ ```api/v1/```

- **```/auth/signup/ (POST)```** — передаём почту и логин, получаем код подтверждения.
- **```/auth/token/ (POST)```** — передаём логин код подтверждения, получаем токен.
- **```/categories/ (GET, POST, DELETE) ```** — получение и управление информацией по категориям.
- **```/genres/ (GET, POST, DELETE) ```** — получение и управление информацией по жанрам.
- **```/titles/ (GET, PUT, PATCH, DELETE)```** — работаем со списком произвдений. 
- **```/titles/{title_id}/ (GET, PUT, PATCH, DELETE)```** — получаем, редактируем или удаляем произведение по *id*.
- **```/reviews/ (GET, PUT, PATCH, DELETE)```** — получаем список рецензий по произведению. 
- **```/reviews/{review_id}/ (GET, PUT, PATCH, DELETE)```** — получаем, редактируем или удаляем рецензию по *id*.
- **```/comments/ (GET, PUT, PATCH, DELETE)```** — получаем список комментариев по рецензии. 
- **```/reviews/{review_id}/ (GET, PUT, PATCH, DELETE)```** — получаем, редактируем или удаляем комментарий по *id*.
### Авторы
- Давид Амиров
- Максим  Доцев
- Никита Михайлов
