
class Location:
    def __init__(self, name, latitude, longitude):
        self.name = name
        try:
            self.lat = float(latitude)
            self.lon = float(longitude)
        except ValueError:
            raise ValueError(
                'latitude and longitude must be floating point numbers'
            )

    @property
    def coordinates(self):
        return (self.lat, self.lon)

    def __str__(self):
        return '({}, {})'.format(self.lat, self.lon)

    def __repr__(self):
        return self.__str__()

    def as_dict(self):
        return {
            'name': self.name,
            'latitude': self.lat,
            'longitude': self.lon,
        }


class Customer:
    def __init__(self, user_id, name, latitude, longitude):
        self.uid = user_id
        self.name = name
        self._location = Location(None, latitude, longitude)

    @property
    def location(self):
        return (self._location)

    @property
    def coordinates(self):
        return (self._location.coordinates)

    def __str__(self):
        return '{} - {}'.format(self.uid, self.name)

    def __repr__(self):
        return self.__str__()

    def as_dict(self):
        """
        Returns the Customer object to the format whence it came!
        """
        return {
            'user_id': self.uid,
            'name': self.name,
            'latitude': str(self.location.lat),
            'longitude': str(self.location.lon),
        }
