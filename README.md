# Описание задания на 2 спринт
Админ панель для онлайн кинотеатра. 

Необходима для загрузки модераторами/администраторами сайта информации о фильмах

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

Доступ к shell postgres. В базе должна быть создана схема **content**
``` bash
make postgres-shell
```

Выполнить миграции
```bash
make django-migrate
```

Создать супер пользователя
```bash
make django-createsuperuser
```
