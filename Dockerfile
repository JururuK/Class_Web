FROM python:3.9.0

WORKDIR /home/

RUN echo "s3aavvv"

RUN git clone https://github.com/hale-in/bbqqweb

WORKDIR /home/bbqqweb/


RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=New.settings.deploy && python manage.py migrate --settings=New.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=New.settings.deploy New.wsgi --bind 0.0.0.0:8000"]