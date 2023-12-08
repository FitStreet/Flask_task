### Postresql+SQLalchemy+FLask

Для запуска проекта вам нужно:

1. Склонить репозиторий оп ссылке 
```
https://github.com/FitStreet/Flask_task.git
```
2. Прейти в папку проекта
```bash
cd Flask_task
```
3. Создать файл config.py и записать в него Переменную DATABASE_CONNECTION со своими данными, как указано в примере ниже.
```python
DATABASE_CONNECTION = "postgresql://Ваш username:ваш пароль@localhost/Название вашей базы данных"
```
4. Зайти в Postgresql и создать там базу данных(название БД должно совпадать с названием в ссылке из 3 пункта)
```postgresql
CREATE DATABASE "Название вашей бд"
```
5. В папке проекта создать виртуальное окружение и активировать его.
```bash
python3 -m venv venv
. venv/bin/activate
```
6. Установить все расширения для проекта командой:
```bash
pip install -r req.txt
```
7. После установки открыть папку проекта в IDE (в моем случае VSCode) командой:
```bash
code .
```
8. Запустите код файла server.py

### Swagger

1. Скачайте последнюю версию по ссылке:
https://github.com/swagger-api/swagger-ui/releases/tag/v5.10.3

2. Распакуйте архив.
3. В папке /dist откройте файл swagger-initializer.js в любом текстовом редакторе и замените ссылку "https://petstore.swagger.io/v2/swagger.json" на 
http://127.0.0.1:8000/apispec_1.json, сохраните изменения.
4. В браузере откройте ссылку http://127.0.0.1:8000/apidocs 

### Вам откроется панель с возможными запросами для этого приложения с возможностью протеcтировать все запросы через этот интерфейс.
