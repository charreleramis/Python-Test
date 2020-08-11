del /s /q /f "*db.sqlite3"

@RD /S /Q "App/migrations"
python manage.py makemigrations App
python manage.py migrate


python manage.py runserver