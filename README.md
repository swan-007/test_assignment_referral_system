# API Сервис для реферальной системы



Установка:
1. Клонировать репозиторий: git clone https://github.com/swan-007/test_assignment_referral_system.git
2. Установить зависимости: pip install -r requirements.txt
3. Создать файл .env со следующими полями (SECRET_KEY, DEBUG, ALLOWED_HOST, DB_ENGINE, DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)

Использование:

1. Регистрация по номеру телефона, метод post,  url = домен/api/v1/user/register, параметры : phone_number.
2. Подтверждение номера телефона, метод post,  url = домен/api/v1/user/register/confirm, параметры : phone_number, phone_code.
3. Получить данные пользователя, метод get, url = домен/api/v1/user/details,  параметры : Authorization token.
4. Ввести чужой инвайт код, метод post, url = домен/api/v1/user/alienInvitecode,  параметры : Authorization token, alien_invite_code.

Для тестирования Api 
1. Сервис доступен по [Ссылке](http://194.58.92.12/) 
2. К проекту приложена postman коллекция
3. Автоматическая документация API [Ссылка](http://194.58.92.12/api/docs/) 
