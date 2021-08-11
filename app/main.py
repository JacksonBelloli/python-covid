from flask import Flask
import pandas as pd
from app.controllers.controllerAmrec import *
from app.controllers.controllerAmesc import *
from app.controllers.controllerAmurel import *
from app.controllers.controllerTop10 import *
from app.data.data import Data
app = Flask(__name__)
thread = Data()
thread.start()

@app.route('/', methods=['GET'])
def init():
    return 'Api is running!!!'
@app.route('/api/amrec', methods=['GET'])
def amrec():
    amrecc = controllerAmrec()
    return amrecc.get_data()
@app.route('/api/amrec/daily', methods=['GET'])
def amrec_daily():
    amrecc = controllerAmrec()
    return amrecc.get_data_daily()
@app.route('/api/amesc', methods=['GET'])
def amesc():
    amescc = controllerAmesc()
    return amescc.get_data()
@app.route('/api/amesc/daily', methods=['GET'])
def amesc_daily():
    amescc = controllerAmesc()
    return amescc.get_data_daily()
@app.route('/api/amurel', methods=['GET'])
def amurel():
    amurelc = controllerAmurel()
    return amurelc.get_data()
@app.route('/api/amurel/daily', methods=['GET'])
def amurel_daily():
    amurelc = controllerAmurel()
    return amurelc.get_data_daily()
@app.route('/api/sc', methods=['GET'])
def sc():
    df = pd.read_csv('app/file/caso_full.csv')
    return df.to_json(orient='records')
@app.route('/api/top10', methods=['GET'])
def top10():
    top10c = controllerTop10()
    return top10c.get_data()
@app.route('/api/top10/daily', methods=['GET'])
def top10_daily():
    top10c = controllerTop10()
    return top10c.get_data_daily()