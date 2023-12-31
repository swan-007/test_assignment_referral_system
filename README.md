# API Сервис для реферальной системы



Установка:
1. Клонировать репозиторий:
```
git clone https://github.com/swan-007/test_assignment_referral_system.git
```
2. Прейти в каталог referral_system:
```
cd referral_system
```    
3. Установить зависимости:
 ```
 pip install -r requirements.txt
 ```
4. Создать файл .env со следующими полями 
 ```
 (SECRET_KEY, DEBUG, ALLOWED_HOST, DB_ENGINE, DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)
 ```
5. Применить миграции:
 ```
 python manage.py migrate 
 ```  
6. Запуск сервера:
 ```
 python manage.py runserver
 ```
7. Наслаждаться хорошим API:
 ```
 python manage.py enjoy
 ```

Использование:

1. Регистрация по номеру телефона. 
   - Метод POST  
   - url: ```домен/api/v1/user/register``` 
   - Обязательные параметры: ```phone_number```  
   - Пример запроса: ```Body={"phone_number": "89259669277"}```
   - Пример ответа: ```{"Status": true, "Phone_code": 1111, "id": 1}```  

2. Подтверждение номера телефона.  
   - Метод POST  
   - url:  ```домен/api/v1/user/register/confirm ``` 
   - Обязательные параметры: ```phone_number, phone_code```  
   - Пример запроса: ```Body={"phone_number": "89259669277", "phone_code": "1111"}```   
   - Пример ответа: ```{"Status": True, "Token": token}```
   
3. Получить данные пользователя.  
   - Метод GET  
   - url: ```домен/api/v1/user/details```   
   - Обязательные параметры: ```Authorization token```  
   - Пример запроса: ```Headers={Authorization: Token полученный токен}```   
   - Пример ответа: ```{phone_number: '89259669277', invite_code: "9aLMcJ",
                        alien_invite_code: {"owner_user": 1, "code": "2UwO9p", "code_user": 4},
                        subscribers_your_invite_code:["89259669277", "89259669225"],}```
     
4. Ввести чужой инвайт код.  
   - Метод POST.  
   - url: ```домен/api/v1/user/alienInvitecode```  
   - Обязательные параметры: ```Authorization token, alien_invite_code```   
   - Пример запроса:```Headers={Authorization: Token полученный токен}, Body={"alien_invite_code": '2UwO9p' }```  


Для тестирования Api 
1. Сервис доступен по [Ссылке](http://194.58.92.12/) 
2. К проекту приложена postman коллекция
3. Автоматическая документация API [Ссылка](http://194.58.92.12/api/docs/) 
