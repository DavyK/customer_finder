# Nearest Customer List

I've made some assumptions about the environment in which this code will run.
 - Python 3
    - setuptools & pip installed
    - pytest to run the test suite and pytest-cov to report unittest coverage
 - Destinations (i.e - the office in Dublin) are provided in a similar format to the customers. See the data directory.

Install the package:
```
python setup.py sdist
```
or
```
pip install -e .
```

Run the tests:
```
pytest --cov=customer_finder --cov-report term-missing
```

Run program:
See the help
```
customers_nearby --help
Usage: customers_nearby [OPTIONS] CUSTOMERS_FILE DESTINATIONS_FILE

Options:
  --max-distance FLOAT  Maximum distance from destination
  --output-json         Output results as JSON
  --help                Show this message and exit.
```
Default Arguments
```
customers_nearby data/customers.txt data/destinations.txt
... results ...
```

Change Max distance
```
customers_nearby data/customers.txt data/destinations.txt --max-distance 50
... fewer results ...
```

Output as JSON
```
customers_nearby data/customers.txt data/destinations.txt  --output-json
... JSON results ...
```
