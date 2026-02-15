сделайте виртуальное окружение  
python -m venv .venv  
актвируйте его  
установите зависимости  
pip install -r  requirements.txt  
примените миграцию к бд  
flask db upgrade  
сгенерируйте квест   
flask --app run seed-db  
запустите приложение  
квест будет доступен по адресу: localhost:5000/quest  
