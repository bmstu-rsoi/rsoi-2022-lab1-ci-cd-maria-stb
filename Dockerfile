FROM python:3.11.0-alpine3.15

#ENV DEBUG 0

#install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

#install zlib to alliw Pillow wheel build
#RUN apk add zlib-dev jpeg-dev gcc musl-dev

#install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy entrypoint.sh and make it executable
#COPY ./entrypoint.sh .
#RUN chmod +x entrypoint.sh

# copy project
COPY . .

#run entrypoint.sh
#ENTRYPOINT [ "/app/entrypoint.prod.sh" ]

#comment out since we are now using docker compose to with postgres service to build the image
#make migrations and migrate
RUN python manage.py makemigrations && python manage.py migrate

# run gunicorn  Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model.
CMD gunicorn Lab1Rsoi.wsgi:application --bind 0.0.0.0:$PORT


#COPY requirements.txt /app/requirements.txt
#
#RUN set -ex \
#    && pip install --upgrade pip \
#    && pip install --no-cache-dir -r /app/requirements.txt
#
#ADD . .
#
#EXPOSE 8000
#
#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "Lab1Rsoi.wsgi:application"]