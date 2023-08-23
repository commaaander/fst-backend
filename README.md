# FST Backend

## Requirements
- Git
- Docker

## Installation
```shell
# Get source code
git clone git@github.com:commaaander/fst-backend.git
cd fst-backend

# Build docker image
docker build --pull --rm -f Dockerfile -t fst-backend:develop .
```

## Usage
# Run docker image
```shell
# Run docker 
docker run --rm -p9000:9000 --name fst-backend fst-backend:develop
```

# URLs
- [API v1](http://127.0.0.1:9000/api/v1/)
- [Django Admin](http://127.0.0.1:9000/api/v1/)
