# Описание задания на 2 спринт
 
Описание структуры и порядок выполнения проекта:

1. `docker_compose` — задача про настройку Nginx, Docker и Django.
2. `django_api` — задача про реализацию API для выдачи информации о фильме.

Напоминаем, что все части работы нужно сдавать на ревью одновременно.

Успехов!

# Запуск контейнеров
Скопировать содержимое .env.example в .env перед запуском
```bash
cp .env.example .env
```

Запуск контейнеров
```bash
make compose-up-detached
```

Собрать статику
```bash
make django-collectstatic
```

Выполнить миграции
```bash
make django-migrate
```

Создать супер пользователя
```bash
make django-createsuperuser
```
