# Тестовое задание в IT Factory

Установите все нужное из *requirements.txt*.

Создайте в Postgres базу данных и укажите все что нужно в **DATABASES** в файле **itfactory_task/settings.py**.

Прогоните миграции с помощью комманды **python3 manage.py migrate** и создайте админа с помощью комманды **python3 manage.py createsuperuser**

Запустите сервер командой **python3 manage.py runserver**

Для получения списка Торговых точек используйте GET запрос *http://127.0.0.1:8000/sales_point/?phone=phone_number*.

Для Посещения торговой точки отправьте POST запрос с параметрами **sales_point**, **latitude**, **longitude** на адрес *http://127.0.0.1:8000/sales_point/?phone=phone_number*.

Я оставил методы GET для адресов */worker/* и */visiting/* для того, чтоб можно было посмотреть, какие данные есть на данный момент в базе.

