Инструкция
Для локального тестирования необходимо создать виртуальное окружение командой python3 -m venv venv и активировать его. Команда venv\Scripts\activate.bat - для Windows; source venv/bin/activate - для Linux и MacOS.

Затем необходимо перейти в папку с нужным уроком и установить зависимости командой pip install -r requirements.txt.

Затем запустить команду uvicorn task4:app --reload для запуска сервера uvicorn.

После этого можно зайти в браузере по адресу http://localhost:8000/docs для просмотра доступных эндпоинтов.