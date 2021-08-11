from flask import Flask
from app.controllers.controllerAmrec import *
from app.controllers.controllerAmesc import *
from app.controllers.controllerAmurel import *
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