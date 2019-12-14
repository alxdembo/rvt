# Nester app

## Usage

Prepare environment:

    make env

Run tests:

    make test

Run development server:

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
