import json
from customer_finder.models import Customer, Location


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Customer) or isinstance(obj, Location):
            return obj.as_dict()

        return super(CustomEncoder, self).default(obj)
