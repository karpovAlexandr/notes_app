# Приложение для управления заметками пользователя NOTES APP

## Описание
Notes App - приложение для сохранения и управления заметками пользователя согласно [требованиям](https://disk.yandex.ru/i/kS4uO2KN2t3ELA)

### Стек:
- бэкенд Django 3.1.4
- база данных Postgres 12.0
- фронтэнд - django templates + bootstrap
- http сервер - gunicorn
- прокси сервер - nginx

### Улучшения:

помимо обязательного функционала были добавлены следующие улучшения:

 - детальное представление заметки с возможностью редактирования и удаления (только для создателя заметки или суперпользователя)
 - локализация (RU/ENG)
 - CRUD api

## Подготовка
 - необходимо установить docker и docker-compose https://docs.docker.com/engine/install/
 - создать группу docker и добавить в нее текущего пользователя
```commandline
sudo groupadd docker
sudo usermod -a -G docker $USER
```
 - добавить сервис docker в автозапуск
```commandline
sudo sysytemctl enable docker
```

## Запуск приложения
запускаем проект скриптом "build_app_docker.sh":
```commandline
./build_app_docker.sh
```
собираем статику и запускаем миграции в контейнере web скриптом "django_commands.sh"
```commandline
./django_commands.sh
```

проверяем доступность по [http://127.0.0.1:80](http://127.0.0.1:80)