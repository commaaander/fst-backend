FROM python:3.11-slim-bookworm
LABEL maintainer="Commaaanders Intelligence Agency"

# set work directory
ARG DJANGO_WORKDIR=/var/lib/cia/
WORKDIR ${DJANGO_WORKDIR}

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
COPY ./run.sh /usr/local/bin
RUN  chmod u+x /usr/local/bin/run.sh

EXPOSE 8000

CMD ["run.sh"]