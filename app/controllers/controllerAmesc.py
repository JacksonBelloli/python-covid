from flask import Flask
import csv
import json
import pandas as pd
from datetime import date, timedelta
app = Flask(__name__)

class controllerAmesc:
    cities = [
        {
            'name': 'Araranguá',
            'population': 68228
        },
        {
            'name': 'Balneário Arroio do Silva',
            'population': 13071
        },
        {
            'name': 'Balneário Gaivota',
            'population': 10979
        },
        {
            'name': 'Ermo',
            'population': 2081
        },
        {
            'name': 'Jacinto Machado',
            'population': 10416
        },
        {
            'name': 'Maracajá',
            'population': 6902
        },
        {
            'name': 'Meleiro',
            'population': 7015
        },
        {
            'name': 'Morro Grande',
            'population': 2890
        },
        {
            'name': 'Passo de Torres',
            'population': 8823
        },
        {
            'name': 'Praia Grande',
            'population': 7319
        },
        {
            'name': 'Santa Rosa do Sul',
            'population': 8358
        },
        {
            'name': 'São João do Sul',
            'population': 7002
        },
        {
            'name': 'Sombrio',
            'population': 30374
        },
        {
            'name': 'Timbé do Sul',
            'population': 5348
        },
        {
            'name': 'Turvo',
            'population': 11854
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
            newdf = df[(df.city == city['name']) & (df.is_last == True)]
            self.data = pd.concat([self.data, newdf])
        # self.data.to_csv('app/file/caso_teste.csv')
        return self.data.to_json(orient='records')
        # return json.dumps(self.data)

    def get_data_daily(self):
        df = pd.read_csv(self.path, header=0)

        for city in self.cities:
            newdf = df[(df.city == city['name'])]
            self.data = pd.concat([self.data, newdf])
        # self.data.to_csv('app/file/caso_teste.csv')
        return self.data.to_json(orient='records')
        # return json.dumps(self.data)