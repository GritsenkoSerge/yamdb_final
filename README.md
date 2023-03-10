# Групповой проект «API для YaMDb» [![Yamdb workflow](https://github.com/GritsenkoSerge/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)](https://github.com/GritsenkoSerge/yamdb_final/actions/workflows/yamdb_workflow.yaml)
## Описание
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка.
Произведению может быть присвоен жанр из списка предустановленных. Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв.

## Пользовательские роли
* Аноним — может просматривать описания произведений, читать отзывы и комментарии.
* Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
* Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
* Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
* Суперюзер Django - обладает правами администратора (admin)

## Использованные технологии/пакеты
* Python 3.7
* Django 2.2.28
* PyJWT 2.1.0
* django-filter 2.4.0
* djangorestframework 3.12.4
* djangorestframework-simplejwt 4.8.0
* requests 2.26.0
* gunicorn 20.0.4
* psycopg2-binary 2.8.6
* python-dotenv 0.21.0
* pytz 2020.1
* sqlparse 0.3.1

## Установка
* Сделать fork репозитория
```
https://github.com/GritsenkoSerge/yamdb_final/fork
```
* В Settings - Secrets - Actions добавить переменные
```
DOCKER_USERNAME - логин на DockerHub
DOCKER_PASSWORD - пароль на DockerHub
DB_ENGINE - django.db.backends.postgresql
DB_NAME - db
POSTGRES_USER - postgres
POSTGRES_PASSWORD - postgres
DB_HOST - IP-адрес или доменное имя вашего сервера
DB_PORT - 5432
DJANGO_SECRET_KEY - openssl rand -base64 33
TELEGRAM_TO - id Telegram-аккаунта для уведомлений
TELEGRAM_TOKEN - токен Telegram-бота
```
* Остановить службу nginx
```
sudo systemctl stop nginx
```
* Установить docker
```
sudo apt install docker.io 
```
* Установить docker-compose. [Официальная документация](https://docs.docker.com/compose/install/)
* Создайте на сервере директории для файлов инфраструктуры
```
cd ~
mkdir yamdb_infra
mkdir yamdb_infra/nginx
``` 
* Скопировать файлы docker-compose.yaml и nginx/default.conf
```
scp ./infra/docker-compose.yaml <ваш_username>@<ваш_сервер>:~/yamdb_infra/
scp ./infra/nginx/default.conf <ваш_username>@<ваш_сервер>:~/yamdb_infra/nginx/
```
* Внести изменение в репозиторий и сделать push (для активации деплоя)
* После успешного деплоя подключиться к серверу и перейти в директорию инфраструктуры 
```
cd ~/yamdb_infra
```
* Произвести миграции
```
docker-compose exec web python3 manage.py migrate
```
* Создать суперпользователя
```
docker-compose exec web python3 manage.py createsuperuser
```
* Собрать статику
```
docker-compose exec web python3 manage.py collectstatic --noinput
```
## После запуска контейнеров проект доступен по адресам:
* REST API http://<ваш_сервер>/api/v1/
* ReDoc http://<ваш_сервер>/redoc/
* Администрирование Django http://<ваш_сервер>/admin/

## Полезные команды
* Смена пароля для пользователя user_name
```
docker-compose exec web python3 manage.py changepassword user_name
```
* Загрузка данных из CSV-файлов (./static/data/*.csv). После загрузки потребуется снова создать суперпользователя.
```
docker-compose exec web python3 manage.py load_data
```
* Загрузка данных без вывода в терминал. После загрузки потребуется снова содазть суперпользователя.
```
docker-compose exec web python3 manage.py load_data -v 0
```

## Примеры запросов API
#### Регистрация нового пользователя:
```
(POST) /api/v1/auth/signup/
```
#### Ответ:
```
{ 
    "email": "string",
    "username": "string"
}
```
#### Получение JWT-token:
```
(POST) /api/v1/auth/token/
```
#### Ответ:
```
{
    "username": "string",
    "confirmation_code": "string"
}
```

## Групповой проекта выполнен командой №21 коготры №41 курса "Python-разработчик"
* [Артем  Зимин](https://github.com/G1lza92)
```
Управление пользователями:
    cистема регистрации и аутентификации,
    права доступа,
    работа с токеном,
    система подтверждения через e-mail.
```
* [Сергей Гриценко (team lead)](https://github.com/GritsenkoSerge/)
```
Модели, view и эндпойнты для отзывов, комментариев. Рейтинг произведений.
Импорт данных из csv файлов.
Коммуникация с заказчиком (ревьюером).
Создание конфигурации Docker Compose.
```
* [Марк Британов](https://github.com/M4rk-er)
```
Модели, view и эндпойнты для произведений, категорий, жанров.
```
### Под руководством:
* Олег Портнихин (наставник)
* Андрей Квичанский (ревьюер)

## Постоянный адрес проекта [yamdb.gricen.ru](https://yamdb.gricen.ru/redoc/)
