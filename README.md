# Foodgram
### Описание
Проект **Foodgram** позволяет постить рецепты, делиться и скачивать списки продуктов
### Алгоритм регистрации пользователей:
Регистрация проходит на сайте, по форме регистрации
### Установка
Проект собран в Docker 20.10.06 и содержит четыре образа:
- backend - образ бэка проекта
- frontend - образ фронта проекта
- postgres - образ базы данных PostgreSQL v 12.04
- nginx - образ web сервера nginx
#### Команда клонирования репозитория:
```bash
git clone https://github.com/phpstal/foodgram-project-react 
```
#### Запуск проекта:
- [Установите Докер](https://docs.docker.com/engine/install/)
- Выполнить команду: 
```bash
docker pull 19870208/foodgram :latest
```
#### Первоначальная настройка Django:
```bash
- docker-compose exec backend python manage.py migrate --noinput
- docker-compose exec backend python manage.py collectstatic --no-input
```
#### Создание суперпользователя:
```bash
- docker-compose exec backend python manage.py createsuperuser
```
#### Заполнение .env:
Чтобы добавить переменную в .env необходимо открыть файл .env в корневой директории проекта и поместить туда переменную в формате имя_переменной=значение.
Пример .env файла:

DB_ENGINE=my_db
DB_NAME=db_name
POSTGRES_USER=my_user
POSTGRES_PASSWORD=my_pass
DB_HOST=db_host
DB_PORT=db_port

### Информация про технологии в этом проекте
Тут, собственно, все по классике. Вот такие технологии использовались:
- python - язык программирования, на нем написан фрейморк Django
- django - фрейморк, на основе которого создан проект
- docker - эмулятор образов ОС, различных сервисов и ОС. Чтобы работло везде также как и у разработчика.
- github - чтобы работать с кодом в разных частях света, причем не один, а целой командой.
- postgresql - СУБД, одна из лучших в мире система управления базами данных
- nxing - веб-сервер. Один из самых распространенных в мире. На нем работает проект.
- gunicorn - это программа связывает между собой Django и NGinx.
- ubuntu - ОС, в которой все вышепереисленное происходит.
- Yandex.Cloud - Это сервис, предоставляющий виртуаные сервера с Ubuntu.

#### Автор:
Автор Владимир Половников. Задание было выполнено в рамках курса от Yandex Praktikum бэкенд разработчик.
#### Workflow badge:
https://github.com/phpstal/foodgram-project-react/actions/workflows/main.yml/badge.svg
#### Server address:
http://178.154.223.189
#### Superuser pass&email:
email: admin@admin.ru
pass: admin
