# Django Tree Menu

Django Tree Menu — это приложение, которое позволяет создавать древовидные меню, редактируемые через стандартную админку Django и выводимые на странице через template tag.

## Функционал

- Реализация меню через template tag.
- Возможность хранения меню в базе данных и редактирования через админку Django.
- Определение активного пункта меню на основе текущего URL.

## Как развернуть проект в Docker?

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/mank000/django-tree-menu.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd django-tree-menu
    ```

4. Запустите проект с помощью Docker Compose:
    ```bash
    sudo docker-compose up -d --build
    ```

5. Выполните миграции базы данных:
    ```bash
    sudo docker-compose exec web python manage.py migrate
    ```

6. Создайте суперпользователя для доступа к админке:
    ```bash
    sudo docker-compose exec web python manage.py createsuperuser
    ```

7. Проект будет доступен по адресу: `http://localhost:8000`

## Стек технологий
Python 3.9+

Django 3.2+

PostgreSQL

Docker