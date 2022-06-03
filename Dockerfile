FROM python:3.10-alpine as requirements-stage

# 
WORKDIR /tmp

# RUN apk update && apk add python3-dev gcc libc-dev
RUN apk update && apk add gcc libc-dev libffi-dev

# 
RUN pip install poetry

# 
COPY ./pyproject.toml ./poetry.lock* /tmp/

# 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# 
FROM python:3.10-alpine

# 
WORKDIR /code

# 
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
# COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
