# Базовое изображение
FROM ubuntu:18.04

# Установка текущего пользователя с root правами
USER root

# Установка Python и pip
RUN apt update -y && \
    apt install python3-pip -y

# Целевая директория
ENV BASE_PATH /server

# Переменные для работы с Flask
ENV LC_ALL=C.UTF-8 
ENV LANG=C.UTF-8
ENV FLASK_ENV=development
ENV FLASK_APP=main.py
RUN set FLASK_APP=$FLASK_APP 

# Копируем локальный requirements.txt внутрь кеша изображения Docker
COPY requirements.txt $BASE_PATH/requirements.txt

# Устанавливаем активную директорию
WORKDIR $BASE_PATH

# Установка зависимостей приложения (cython - требование для scipy)
RUN pip3 install cython --upgrade && \
    pip3 install -r requirements.txt --upgrade

# Копируем все содержимое локальной директории в целевую в изображении
COPY . $BASE_PATH
COPY docker.config $BASE_PATH/local.config

# Открываем порт
EXPOSE 3444

# Запускаем команду при создании контейнера
CMD flask run -h 0.0.0.0 -p 3444