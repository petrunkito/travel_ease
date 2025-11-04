
rm db.sqlite3
find . -path "*/migrations/*.py" ! -name "__init__.py" -delete
find . -type d -name "__pycache__" -exec rm -r {} +

python manage.py makemigrations
python manage.py migrate

