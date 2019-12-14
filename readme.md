# Nester app

## Usage

Prepare environment, run tests, run development server:

    make env
    make test
    make devserver


### CLI
```bash
cd nester
cat ../test_cases/input/original_task.json \
 | python3 nest.py currency country city
```

### REST API

Use method POST:

    curl -d "@test_cases/input/original_task.json" \
    -H "authorization: Basic dXNlcjpwYXNz" \
    -X POST "http://localhost:8000/api/nest?q[]=currency&q[]=country&q[]=city"

## Testing 

The solution uses Django unittest wrapper to deal with requests smoother

As mentioned, to run tests:

    make test

or 

    python manage.py test