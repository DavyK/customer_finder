from unittest import TestCase
from customer_finder.models import Location, Customer


class TestLocation(TestCase):

    def setUp(self):
        self.data = {
            'latitude': '66.543759',
            'name': 'Santa Claus Village - Lapland, Finland',
            'longitude': '25.847188',
        }

        self.location = Location(**self.data)

    def test_basic_attributes(self):
        assert self.location.name == self.data['name']
        assert self.location.lat == float(self.data['latitude'])
        assert self.location.lon == float(self.data['longitude'])

    def test_coordinates(self):
        assert isinstance(self.location.coordinates, tuple)
        assert len(self.location.coordinates) == 2
        coordinates = (
            float(self.data['latitude']),
            float(self.data['longitude'])
        )
        assert self.location.coordinates == coordinates

    def test_not_floatable(self):
        with self.assertRaises(ValueError):
            Location(**{
                'name': 'test',
                'latitude': 'not a float',
                'longitude': 4.2,
            })

        with self.assertRaises(ValueError):
            Location(**{
                'name': 'test',
                'latitude': 4.2,
                'longitude': 'not a float',
            })


class TestCustomer(TestCase):

    def setUp(self):
        self.data = {
            'latitude': '66.543759',
            'user_id': 0,
            'name': 'Santa',
            'longitude': '25.847188',
        }

        self.customer = Customer(**self.data)

    def test_basic_attributes(self):
        assert self.customer.name == self.data['name']
        assert self.customer.uid == self.data['user_id']

    def test_coordinates(self):
        assert isinstance(self.customer.location, Location)
        assert isinstance(self.customer.coordinates, tuple)
        assert len(self.customer.coordinates) == 2
        coordinates = (
            float(self.data['latitude']),
            float(self.data['longitude'])
        )
        assert self.customer.coordinates == coordinates
