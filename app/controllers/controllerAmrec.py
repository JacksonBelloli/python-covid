from flask import Flask
import csv
import json
import pandas as pd
from datetime import date, timedelta
from app.controllers.controllerThread import Thread

app = Flask(__name__)


class controllerAmrec:
    cities = [
        {
            'name': 'Criciúma',
            'population': 215186,
            'cod': 4204608
        },
        {
            'name': 'Balneário Rincão',
            'population': 12760,
            'cod': 4220000
        },
        {
            'name': 'Cocal do Sul',
            'population': 16684,
            'cod': 4204251
        },
        {
            'name': 'Morro da Fumaça',
            'population': 17796,
            'cod': 4211207
        },
        {
            'name': 'Siderópolis',
            'population': 14007,
            'cod': 4217600
        },
        {
            'name': 'Nova Veneza',
            'population': 15166,
            'cod': 4211603
        },
        {
            'name': 'Treviso',
            'population': 3600,
            'cod': 4218350
        },
        {
            'name': 'Orleans',
            'population': 22912,
            'cod': 4211702
        },
        {
            'name': 'Urussanga',
            'population': 21268,
            'cod': 4219002
        },
        {
            'name': 'Forquilinha',
            'population': 25988,
            'cod': 4205456
        },
        {
            'name': 'Lauro Müller',
            'population': 13359,
            'cod': 4209607
        },
        {
            'name': 'Içara',
            'population': 56421,
            'cod': 4207007
        }
    ]
    data = pd.DataFrame()
    path = 'app/file/caso_full.csv'

    def __init__(self):
        print('init')

    def get_data(self):
        yesterday = date.today() - timedelta(days=1)

        yesterday = yesterday.strftime('%Y-%m-%d')

        df = pd.read_csv(self.path, header=0)


        for city in self.cities:
            newdf = df[(df.city == city['name']) & (df.date == yesterday)]
            self.data = pd.concat([self.data, newdf])
        #self.data.to_csv('app/file/caso_teste.csv')
        return self.data.to_json(orient='records')
        #return json.dumps(self.data)

    def get_data_daily(self):
        df = pd.read_csv(self.path, header=0)

        for city in self.cities:
            newdf = df[(df.city == city['name'])]
            self.data = pd.concat([self.data, newdf])
        # self.data.to_csv('app/file/caso_teste.csv')
        return self.data.to_json(orient='records')
        # return json.dumps(self.data)
