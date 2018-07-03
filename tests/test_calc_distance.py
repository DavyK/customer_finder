import json
from unittest import TestCase
from customer_finder.distance import great_circle_distance


class TestSquid(TestCase):

    def test_distance_between_two_points(self):
        '''
        Test the distance between the Spire in Dublin and Empire State Building
        in New York City is 5111.02 km (https://goo.gl/KTyzjS)
        '''
        d = great_circle_distance(
            (53.349995, -6.260223),  # Dublin Spire
            (40.748652, -73.985640),  # Empire state Building
        )
        d = float("{0:.2f}".format(d))  # round to 2 places for asserting
        assert d == 5111.02

    def test_too_few_coords(self):
        '''
        Test the distance function with nonsensical inputs
        '''
        with self.assertRaises(ValueError):
            great_circle_distance(
                (1,),  # Dublin Spire
                (2,),  # Empire state Building
            )

    def test_too_many_coords(self):
        '''
        Test the distance function with nonsensical inputs
        '''
        with self.assertRaises(ValueError):
            great_circle_distance(
                (1, 2, 3),  # Dublin Spire
                (4, 5, 6),  # Empire state Building
            )

    def test_not_floats(self):
        '''
        Test the distance function with nonsensical inputs
        '''

        with self.assertRaises(ValueError):
            great_circle_distance(
                (42.424242, '42.424242'),
                ('7.77778', 6.66),
            )
