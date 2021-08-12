from flask import Flask
import csv
import json
import pandas as pd
from datetime import date, timedelta
app = Flask(__name__)

class controllerAmurel:
    cities = [
        {
            'name': 'Armazém',
            'population': 8674
        },
        {
            'name': 'Imaruí',
            'population': 11672
        },
        {
            'name': 'Pescaria Brava',
            'population': 10091
        },
        {
            'name': 'São Martinho',
            'population': 3180
        },
        {
            'name': 'Braço do Norte',
            'population': 33450
        },
        {
            'name': 'Imbituba',
            'population': 44853
        },
        {
            'name': 'Rio Fortuna',
            'population': 4611
        },
        {
            'name': 'Treze de Maio',
            'population': 7081
        },
        {
            'name': 'Capivari de Baixo',
            'population': 24871
        },
        {
            'name': 'Jaguaruna',
            'population': 20024
        },
        {
            'name': 'Sangão',
            'population': 12678
        },
        {
            'name': 'Tubarão',
            'population': 105686
        },
        {
            'name': 'Grão-Pará',
            'population': 6223
        },
        {
            'name': 'Laguna',
            'population': 45814
        },
        {
            'name': 'Santa Rosa de Lima',
            'population': 2142
        },
        {
            'name': 'Gravatal',
            'population': 11501
        },
        {
            'name': 'Pedras Grandes',
            'population': 3976
        },
        {
            'name': 'São Ludgero',
            'population': 13410
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