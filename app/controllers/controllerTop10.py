from flask import Flask
import csv
import json
import pandas as pd
from datetime import date, timedelta
from app.controllers.controllerThread import Thread

app = Flask(__name__)


class controllerTop10:
    cities = [
        {
            'name' : 'Joinville',
            'population' : 590466
        },
        {
            'name' : 'Florianópolis',
            'population' : 500973
        },
        {
            'name' : 'Blumenau',
            'population' : 357199
        },
        {
            'name' : 'São José',
            'population' : 246586
        },
        {
            'name' : 'Chapecó',
            'population' : 166040
        },
        {
            'name' : 'Itajaí',
            'population' : 219536
        },
        {
            'name' : 'Criciúma',
            'population' : 215186
        },
        {
            'name' : 'Jaraguá do Sul',
            'population' : 177697
        },
        {
            'name' : 'Palhoça',
            'population' : 171797
        },
        {
            'name' : 'Lages',
            'population' : 157544
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
