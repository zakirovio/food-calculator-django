# SimpleFoodCalculator — калькулятор пищевой ценности продуктов
## Краткое описание

Функционал сайта на сегодняшний день:
- Калькулятор
- Список таблиц с данными продуктов разбитый по категориям
- Примитивный API 
- Стандартная админка: root root

 ## Docker
 - Нужно клонировать репозиторий:
   - https: ```git clone https://github.com/iamxaidar/food-calculator-django.git```
   - ssh: ```git@github.com:iamxaidar/food-calculator-django.git```
 - Структура переменных окружения представлена в **env.template**; 
    - Так как проект не боевой, все необходимые значения уже указаны в шаблоне;
- Нужно создать файлы с переменными окружения:
    - linux: ```$ make dotenv```
    - win: ```>> cd source/config && copy .env.template .env```
       - Вернуться к корню проекта: ```cd ../..```
- Запустить сборку и запуск контейнеров:
  - linux: ```$ make up```
  - win: ```docker compose up```
- После успешного запуска сделать импорт данных из таблицы в базу:
  - linux: ```$ make import```
  - win: ```docker exec -it web poetry run python source/import.py```

## Другие команды управления контейнерами
- Остановить и удалить контейнеры:
  - linux: ```$ make down```
  - win: ```docker compose down```
- Остановить контейнеры:
  - linux: ```$ make stop```
  - win: ```docker stop web db```
- Запустить контейнеры после установки:
  - linux: ```$ make start```
  - win: ```docker start db web```

## Адрес приложения
- Приложение будет доступно по адресу:
  - ```https://127.0.0.1:8000```
