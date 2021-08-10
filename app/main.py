from flask import Flask
from app.controllers.controllerAmrec import *
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
@app.route('/api/amesc', methods=['POST'])
def createcsv():
    return 'Csv'