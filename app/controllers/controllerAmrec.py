from flask import Flask
import csv
import json
app = Flask(__name__)


class controllerAmrec:
    cities = [
            {
                'name':'Criciúma',
                'population': 215186,
                'cod': 4204608
            },
            {
                'name':'Balneário Rincão',
                'population': 12760,
                'cod': 4220000
            },
            {
                'name':'Cocal do Sul',
                'population':16684,
                'cod': 4204251
            },
            {
                'name':'Morro da Fumaça',
                'population':17796,
                'cod': 4211207
            },
            {
                'name':'Siderópolis',
                'population':14007,
                'cod': 4217600
            },
            {
                'name':'Nova Veneza',
                'population':15166,
                'cod': 4211603
            },
            {
                'name':'Treviso',
                'population':3600,
                'cod': 4218350
            },
            {
                'name':'Orleans',
                'population':22912,
                'cod': 4211702
            },
            {
                'name':'Urussanga',
                'population':21268,
                'cod': 4219002
            },
            {
                'name':'Forquilinha',
                'population':25988,
                'cod': 4205456
            },
            {
                'name':'Lauro Müller',
                'population':13359,
                'cod': 4209607
            },
            {
                'name':'Içara',
                'population':56421,
                'cod': 4207007
            }
        ]
    data = []
    path = 'app/file/caso_full.csv'

    def __init__(self):
        print('init')

    def get_data(self):
        with open(self.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                 if row['city_ibge_code'] == '':
                     continue
                 for city in self.cities:
                     if int(row['city_ibge_code']) == city['cod']:
                         self.data.append(row)
        return json.dumps(self.data)
