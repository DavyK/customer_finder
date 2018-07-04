import json
import click
from customer_finder.io import Reader
from customer_finder.encoders import CustomEncoder
from customer_finder.models import Customer, Location
from customer_finder.distance import great_circle_distance


def get_model_list(filename, model):
    model_list = []
    with open(filename) as fh:
        for item in Reader(fh):
            model_list.append(model(**item))

    return model_list


def filter_for_nearby_customers(destination, customers, max_dist):
    nearby_customers = []
    for customer in customers:
        dist = great_circle_distance(
            customer.coordinates,
            destination.coordinates
        )

        if dist <= max_dist:
            nearby_customers.append(customer)
    sorted_customers = sorted(nearby_customers, key=lambda c: c.uid)

    return sorted_customers


def output(data, output_json):
    if output_json:
        print(json.dumps(data, cls=CustomEncoder))
    else:
        for item in data:
            destination = item['destination']
            customers = item['nearby_customers']
            print('{}:'.format(destination.name))
            print('\tuser_id\t\tname')
            for customer in customers:
                print('\t{}\t\t{}'.format(customer.uid, customer.name))


@click.command()
@click.argument('customers_file')
@click.argument('destinations_file')
@click.option(
    '--max-distance', default=100, type=float,
    help='Maximum distance from destination'
)
@click.option('--output-json', is_flag=True, help='Output results as JSON')
def main(customers_file, destinations_file, max_distance, output_json):
    customers = get_model_list(customers_file, Customer)
    destinations = get_model_list(destinations_file, Location)

    customers_near_destinations = []
    for destination in destinations:
        nearby_customers = filter_for_nearby_customers(
            destination,
            customers,
            max_distance
        )
        customers_near_destinations.append({
            'destination': destination,
            'nearby_customers': nearby_customers,
        })

    output(customers_near_destinations, output_json)
