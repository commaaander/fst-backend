FROM python:3.10-slim-bookworm

# set work directory
WORKDIR /var/lib/cia/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./LICENSE .
COPY ./fst_backend ./fst_backend
COPY ./manage.py .
COPY ./db.sqlite3 .

EXPOSE 9000

CMD ["gunicorn","fst_backend.wsgi:application","--bind","0.0.0.0:9000"]