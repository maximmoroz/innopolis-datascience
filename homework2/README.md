# Домашнее задание 2. Про-версия
## 1. Установить Docker, вы вести версию докера с помощью команды docker –v
```shell
$ docker -v
Docker version 20.10.7, build 20.10.7-0ubuntu1~18.04.1
```
## 2. Распакуйте  архив docker_flask и соберите Контейнер с помощью команды build
```shell
$ cd ex1/docker_flask
$ docker build .
<!-- SKIP OUTPUT -->
Successfully built 34391da16168
```

Проверяем, какие образы доступны Docker
```shell
$ docker images
REPOSITORY                   TAG                   IMAGE ID       CREATED         SIZE
<none>                       <none>                34391da16168   3 minutes ago   198MB
tiangolo/uwsgi-nginx-flask   python3.6-alpine3.7   cdec3b0d8f20   16 months ago   189MB
```

Если при сборке указать флаг `-t`, получим удобное имя образа(вместо id) 
## 3. Запустите контейнер на 8888 порту, перейдите в браузере по адресу http://localhost:8888/ и сделайте скриншот результата

```shell
$ docker run -p 8888:80 34391da16168
```

![Скриншот](ex1/docker_flask.png "Скриншот открытого окна с приложением из контейнера в браузере")

Видно, что это не то, что мы ожидали.

```shell
python3 -mvenv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```
![Скриншот](ex1/flask_app.png "Скриншот открытого окна с приложением в браузере")

Для исправления, потребуется доработать `Dockerfile`