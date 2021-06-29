from flask import Flask
from app.controllers.controllerAmrec import *
from app.data.data import Data
app = Flask(__name__)
thread = Data()
thread.start()

@app.route('/api/amrec', methods=['GET'])
def amrec():
    amrecc = controllerAmrec()
    return amrecc.get_data()
@app.route('/api/amesc', methods=['POST'])
def createcsv():
    return 'Csv'