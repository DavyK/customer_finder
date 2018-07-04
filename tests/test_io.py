import json
from io import StringIO
from unittest import TestCase
from customer_finder.io import Reader

test_data = [
    {
        "user_id": 12,
        "name": "Foo McBar",
        "latitude": "52.98",
        "longitude": "-6.04"
    },
    {
        "user_id": 1,
        "name": "Bar O'Foo",
        "latitude": "51.92",
        "longitude": "-10.27"
    }
]


class TestReader(TestCase):

    def setUp(self):
        self.stream = StringIO()
        for datum in test_data:
            self.stream.write(json.dumps(datum))
            self.stream.write('\n')
        self.stream.seek(0)

    def test_read(self):
        reader = Reader(self.stream)
        count = 0
        for i, data in enumerate(reader):
            count += 1
            assert type(data) == dict

            assert 'user_id' in data
            assert data['user_id'] == test_data[i]['user_id']

            assert 'name' in data
            assert data['name'] == test_data[i]['name']

            assert 'latitude' in data
            assert data['latitude'] == test_data[i]['latitude']

            assert 'longitude' in data
            assert data['longitude'] == test_data[i]['longitude']

        assert count == len(test_data)
