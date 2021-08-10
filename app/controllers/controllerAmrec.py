from flask import Flask
import csv
import json
import pandas as pd
from itertools import islice
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
    cities2 = [
        {
            'name' : 'Armazém',
             'population' : 8674
        },
        {
            'name' : 'Imaruí',
            'population' : 11672
        },
        {
            'name' : 'Pescaria Brava',
            'population' : 10091
        },
        {
            'name' : 'São Martinho',
            'population' : 3180
        },
        {
            'name' : 'Braço do Norte',
            'population' : 33450
        },
        {
            'name' : 'Imbituba',
            'population' : 44853
        },
        {
            'name' : 'Rio Fortuna',
            'population' : 4611
        },
        {
            'name' : 'Treze de Maio',
            'population' : 7081
        },
        {
            'name' : 'Capivari de Baixo',
            'population' : 24871
        },
        {
            'name' : 'Jaguaruna',
            'population' : 20024
        },
        {
            'name' : 'Sangão',
            'population' : 12678
        },
        {
            'name' : 'Tubarão',
            'population' : 105686
        },
        {
            'name' : 'Grão-Pará',
            'population' : 6223
        },
        {
            'name' : 'Laguna',
            'population' : 45814
        },
        {
            'name' : 'Santa Rosa de Lima',
            'population' : 2142
        },
        {
            'name' : 'Gravatal',
            'population' : 11501
        },
        {
            'name' : 'Pedras Grandes',
            'population' : 3976
        },
        {
            'name' : 'São Ludgero',
            'population' : 13410
        }
    ]
    cities3 = [
        {
            'name' : 'Araranguá',
            'population' : 68228
        },
        {
            'name' : 'Balneário Arroio do Silva',
            'population' : 13071
        },
        {
            'name' : 'Balneário Gaivota',
            'population' : 10979
        },
        {
            'name' : 'Ermo',
            'population' : 2081
        },
        {
            'name' : 'Jacinto Machado',
            'population' : 10416
        },
        {
            'name' : 'Maracajá',
            'population' : 6902
        },
        {
            'name' : 'Meleiro',
            'population' : 7015
        },
        {
            'name' : 'Morro Grande',
            'population' : 2890
        },
        {
            'name' : 'Passo de Torres',
            'population' : 8823
        },
        {
            'name' : 'Praia Grande',
            'population' : 7319
        },
        {
            'name' : 'Santa Rosa do Sul',
            'population' : 8358
        },
        {
            'name' : 'São João do Sul',
            'population' : 7002
        },
        {
            'name' : 'Sombrio',
            'population' : 30374
        },
        {
            'name' : 'Timbé do Sul',
            'population' : 5348
        },
        {
            'name' : 'Turvo',
            'population' : 11854
        }
    ]
    data = pd.DataFrame()
    path = 'app/file/caso_full.csv'

    def __init__(self):
        print('init')

    @app.route('/', methods=['GET'])
    def get_data(self):
        df = pd.read_csv(self.path, header=0)

        for city in self.cities:
            newdf = df[(df.city == city['name']) & (df.is_last == True)]
            self.data = pd.concat([self.data, newdf])
        #self.data.to_csv('app/file/caso_teste.csv')
        return self.data.to_json(orient='records')
        #return json.dumps(self.data)

    @app.route('/daily', methods=['GET'])
    def get_data_daily(self):
        df = pd.read_csv(self.path, header=0)

        for city in self.cities:
            newdf = df[(df.city == city['name'])]
            self.data = pd.concat([self.data, newdf])
        # self.data.to_csv('app/file/caso_teste.csv')
        return self.data.to_json(orient='records')
        # return json.dumps(self.data)
