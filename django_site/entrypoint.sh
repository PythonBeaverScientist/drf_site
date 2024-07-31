python3 -m poetry run python manage.py migrate
python3 -m poetry run python manage.py createsuperuser --noinput
python3 -m poetry run python manage.py collectstatic --noinput
python3 -m poetry run python manage.py runserver "$DJANGO_HOST:$DJANGO_PORT"
