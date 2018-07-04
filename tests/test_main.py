import sys
import json
from io import StringIO
from unittest import TestCase
from customer_finder.models import Customer, Location
from customer_finder.encoders import CustomEncoder
from customer_finder.main import filter_for_nearby_customers, output


CUSTOMERS = [
    {  # Dublin City Centre - 8.6 km from Dublin Airport
        "user_id": 1,
        "name": "Foo McBar",
        "latitude": "53.349983",
        "longitude": "-6.260268"
    },
    {  # Eyre Square in Galway - 185 km from Dublin Airport
        "user_id": 2,
        "name": "Bar O'Foo",
        "latitude": "53.274539",
        "longitude": "-9.049253"
    }
]

DESTINATION = {
    'name': 'Dublin Airport',
    'latitude': '53.431141',
    'longitude': '-6.250189',
}


class TestFilter(TestCase):

    def setUp(self):
        self.customers = [Customer(**item) for item in CUSTOMERS]
        self.destination = Location(**DESTINATION)

    def test_filter_for_nearby_customers_1(self):
        result = filter_for_nearby_customers(
            self.destination,
            self.customers,
            100
        )
        assert len(result) == 1
        assert result[0].name == self.customers[0].name

    def test_filter_for_nearby_customers_2(self):
        result = filter_for_nearby_customers(
            self.destination,
            self.customers,
            200
        )
        assert len(result) == 2
        assert result[0].name == self.customers[0].name
        assert result[1].name == self.customers[1].name


class TestOutput(TestCase):
    def setUp(self):
        self.customers = [Customer(**item) for item in CUSTOMERS]
        self.destination = Location(**DESTINATION)
        self.nearby_customers = filter_for_nearby_customers(
            self.destination,
            self.customers,
            100
        )

        self.data = [{
            'destination': self.destination,
            'nearby_customers': self.nearby_customers
        }]

    def test_json_output(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput  # redirect stdout to StringIO.

        output(self.data, output_json=True)
        sys.stdout = sys.__stdout__

        json_string = json.dumps(self.data, cls=CustomEncoder)
        # remove newline character from the stdout string
        assert capturedOutput.getvalue().strip() == json_string

    def test_output(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput  # redirect stdout to StringIO.

        output(self.data, output_json=False)
        sys.stdout = sys.__stdout__

        output_string = "Dublin Airport:\n\tuser_id\t\tname\n\t1\t\tFoo McBar\n"

        assert capturedOutput.getvalue() == output_string
