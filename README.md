
# Docker
## Источник
https://demo.opencart.com/
## Что сделано
1. Файл dockerignore - внесены файлы, которые нет необходимости копировать в докер контейнер
2. Файл Dockerfile - подготовка контейнера для запуска тестов
3. Скрипт run_tests_in_docker.sh - BASH скрипт для запуска тестов проекта из докера и оформления репорта аллюр
4. Отрефакторены нотации allure  - маркировка щагов из функций, а не непосредственно теста

