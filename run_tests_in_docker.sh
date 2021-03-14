#!/bin/bash

# Собираем image с тегом tests_open_cart
docker build -t tests_open_cart .

# Запускаем контейнер под именем my_run из image tests_open_cart
docker run --name my_run tests_open_cart --browser chrome

# Копируем из контейнера созданный allure-report
docker cp my_run:/app/allure-report .

#собирает репорт
/Users/Alena/Downloads/allure-2.13.8/bin/allure serve allure-report

# Удаляем из системы созданный контейнер
docker system prune -f