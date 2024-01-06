FROM python:3.11-slim-bookworm
LABEL maintainer="Commaaanders Intelligence Agency"

# set work directory
ARG DJANGO_WORKDIR=/var/lib/cia/
WORKDIR ${DJANGO_WORKDIR}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY ./run*.sh /usr/local/bin/
RUN  chmod +x /usr/local/bin/run.sh
COPY ./LICENSE ./manage.py ./fst_backend ./

EXPOSE 8000

CMD ["run.sh"]