# FST Backend

## Requirements

### For Development
- [Poetry](https://python-poetry.org/)
- [Visual Studio Code](https://code.visualstudio.com/)

### For Deployment
- Run locally
    - Python
    - Python Modules venv and pip
- Git
- Docker with compose Add-on

## Installation
```shell
# Get source code
git clone git@github.com:commaaander/fst-backend.git
cd fst-backend
```

## Configuration
```shell
# Get source code
cp .env.template .env
vi .env
```

## Usage
### Run for development
```shell
docker compose build
docker compose up -d
```

### Run for production
TODO

## URLs
- [API v1](http://fst-backend.localhost:8000/api/v1/)
- [API Schema](http://fst-backend.localhost:8000/api/schema/v1/)
- [Django Admin](http://fst-backend.localhost:8000/admin)
- [pgAdmin](http://fst-pgadmin.localhost:8000)
- [Traefik Dashboard](http://localhost:8001)
