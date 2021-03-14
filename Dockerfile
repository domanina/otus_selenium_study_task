# базовый образ
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем  зависимости
# Точка из текущей директории
COPY requirements.txt .

# Команды терминала
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта из текущей в базовуюю
COPY . .

# Предустанавливаем команду pytest и отчёт
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]

CMD ["--browser", "chrome"]
