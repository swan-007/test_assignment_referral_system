# API Сервис для реферальной системы



Установка:
1. Клонировать репозиторий: git clone https://github.com/swan-007/test_assignment_referral_system.git
2. Установить зависимости: pip install -r requirements.txt
3. Создать файл .env со следующими полями (SECRET_KEY, DEBUG, ALLOWED_HOST, DB_ENGINE, DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)

Использование:

1. Регистрация по номеру телефона. 
   - Метод Post.  
   - url = домен/api/v1/user/register.  
   - Обязательные параметры: phone_number.  
   - Пример запроса:
     \```Body={"phone_number" :  "89259669277"}\```
   - Пример ответа: {"Status": true, "Phone_code": 1111, "id": 1}  

2. Подтверждение номера телефона.  
   - Метод Post.  
   - url = домен/api/v1/user/register/confirm.  
   - Обязательные параметры: phone_number, phone_code.  
   - Пример запроса: Body={"phone_number" :  "89259669277", "phone_code": "1111"}  
   - Пример ответа:{"Status" : True, "Token": token}
   
3. Получить данные пользователя.  
   - Метод Get.  
   - url = домен/api/v1/user/details.  
   - Обязательные параметры: Authorization token.  
   - Пример запроса: Headers={Authorization : Token полученный токен}  
   - Пример ответа:{
                  phone_number: ,  
                  invite_code: ,  
                  alien_invite_code: {},  
                  subscribers_your_invite_code:[],  
                 }
      
4. Ввести чужой инвайт код.  
   - Метод Post.  
   - url = домен/api/v1/user/alienInvitecode.  
   - Обязательные параметры: : Authorization token, alien_invite_code.  
   - Пример запроса:
                     Headers={Authorization : Token полученный токен},  
                     Body={"alien_invite_code": }  


Для тестирования Api 
1. Сервис доступен по [Ссылке](http://194.58.92.12/) 
2. К проекту приложена postman коллекция
3. Автоматическая документация API [Ссылка](http://194.58.92.12/api/docs/) 
