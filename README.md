# FST Backend

## Requirements
- Run locally
    - Python
    - Python Modules venv and pip
- Git
- Docker

## Installation
```shell
# Get source code
git clone git@github.com:commaaander/fst-backend.git
cd fst-backend
```

## Usage
### Run as docker image
```shell

# Build docker image
docker build --pull --rm -f Dockerfile -t fst-backend:develop .

# Run docker 
docker run --rm -p8000:8000 --name fst-backend fst-backend:develop
```

### Run localy
The following commands create a running Django instance with an empty database
```shell
# Create virtual environment (only one time needed)
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install Packages
python -m pip install -r requirements.txt

# Create Migrations
python ./manage.py migrate --noinput

# Start Django Webserver
python ./manage.py runserver 127.0.0.1:8000
```

## Load/Save database
```shell
# Save database content as JSON
python ./manage.py dumpdata > ./db/db_data.json 

# Load databaes content
python ./manage.py loaddata ./db/db_data.json 
```
## URLs
- [API v1](http://127.0.0.1:8000/api/v1/)
- [API Schema](http://127.0.0.1:8000/api/schema/v1/)
- [Django Admin](http://127.0.0.1:8000/api/v1/)

