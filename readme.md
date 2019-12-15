# Nester app


## TL;DR

Prepare environment:

    make env

Run tests:

    make test

Run development server:

    make devserver

## Structure

Project consists of following packages:

1. nester_app: *Django project folder with router and settings*
1. api: *REST API*
1. helpers: *Basic authentication helper and testing helpers*
1. nester: *Contains the main logic: ```nester.py``` and CLI: ```nest.py```* 
1. test_cases: *Testing scenarios containing inputs and outputs*  

## Authentication

REST API authenticates against backends provided in the project. By default it is sqlite database.
Demo user is provided in ```api/fixtures``` and is loaded automatically using ```make dev_server``` 

### CLI
```bash
cd nester
cat ../test_cases/input/original_task.json \
 | python3 nest.py currency country city
```

### REST API


    curl -d "@test_cases/input/original_task.json" \
    -H "authorization: Basic dXNlcjpwYXNz" \
    -X POST "http://localhost:8000/api/nest?q[]=currency&q[]=country&q[]=city"

## Testing 

The solution uses Django unittest wrapper to deal with requests smoother

As mentioned, to run tests:

    make test

or 

    python manage.py test