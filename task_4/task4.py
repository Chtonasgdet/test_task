#Подключение всех нужных модулей
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


#Создание приложения
app = FastAPI(
    title='Trading App'
)


#Импровизированная база данных
fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
    {'id': 4, 'role': 'investor', 'name': 'Homer'},
    {'id': 5, 'role': 'trader', 'name': 'Jessica'},
]

#Класс для валидации данных(используется для проверки правильности введённых данных пользователем)
class User(BaseModel):
    id: int
    role: str
    name: str

    
#Сами запросы
#В FastAPI они строятся по такому принципу: 
#декоратор->имя приложения->название запроса->в скобках часть URL(в фигурных скобках можно прописывать переменные)
#Первоначальный адрес http://127.0.0.1:8000

#Все запросы очень удобно тестировать в самой документации FastAPI
#Адрес: http://127.0.0.1:8000/docs

#Запрос get - получение данных
@app.get('/users/{user_id}') #Пользователь переходит по какому-то id
def get_user(user_id: int): 
    for user in fake_users: #Поиск id в базе
        if user.get('id') == user_id: #Если оно найдено, возвращаются все данные указанного пользователя
            return user
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, 
        content={ 'message': 'Пользователь не найден' }
    ) #Если нет - к нам в терминал приходит соответствующая ошибка, а пользователь видет заданное сообщение
    

#Необязательный запрос
#Нужен для того, чтобы видеть результат работы других запросов(изменения, происходящие в бд)
@app.get('/users')
def get_users():
    return fake_users #Просто возвращает всю бд


#Запрос post - добавление данных
@app.post('/users')
def add_user(user: User): #Проверка правильности введённых пользователем данных
    new_user = user.dict()
    all_id = [id['id'] for id in fake_users] #Создаётся список из всех id, которые есть в базе
    if new_user['id'] not in all_id: #Проверка
        fake_users.append(new_user)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={ 'message': 'Пользователь '+ str(new_user) +' успешно добавлен в базу'}
        ) #Если такого id нет в базе, пользователь добавляется в неё(и пользователю, и нам приходят соответствующие сообщения)
    else:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={ 'message': 'Пользователь с таким id уже существует'}
        ) #Если да - к нам в терминал приходит соответствующая ошибка, а пользователь видет заданное сообщение
    


#Запрос patch - изменение части данных данных
#В данном случае изменяется имя пользователя
@app.patch('/users/{user_id}')
def edit_user(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0] #Получение пользователя по введённому id
    current_user['name'] = new_name #Смена имени на новое
    return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={ 'message': 'Имя пользователя '+ str(current_user) +' успешно обновлено'}
        ) #Сообщение о том, что всё прошло хорошо
    

#Запрос delete - удаление данных    
@app.delete('/users/{user_id}')
def del_user(user_id: int):
    for user in fake_users: #Поиск id в базе
        if user.get('id') == user_id: #Если id найден
            fake_users.remove(user) #Удаление пользователя
            return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={ 'message': 'Пользователь успешно удалён из базы'}
        ) #Возврат сообщения об успешной операции
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, 
        content={ 'message': 'Пользователь не найден' }
    ) #Если пользователь не найден, возврат сообщения об ошибке