from flask import Flask, request
from featurizer import extract
from retrain import retrain as retrain_model
from flask_executor.executor import Executor
import json
from tensorflow.keras.models import load_model
from numpy import ndarray
from os import pardir
from sys import exc_info

api = Flask(__name__)
executor = Executor(api)
api.config['EXECUTOR_PROPAGATE_EXCEPTIONS'] = True

@api.route('/postData', methods=['POST'])
def postData():
    '''
    Received data is committed to DB for retraining
    ---------------------------------------------------------------------------------------
    NOTE: This can also be done asynchronously using a flask_executor instance.
    Here I do it synchronously since I design api to handle only one datapoint at a time.
    In prod, this can be easily extended to a json array and then handled asynchronously.
    ---------------------------------------------------------------------------------------
    '''
    try:
        data = request.data
        jsonData = json.loads(data)
        f = open("assets/data/name_gender.csv", "a")
        f.write("{},{}\n".format(jsonData["name"], jsonData["gender"]))
        f.close()
        return "success !!!"
    except Exception as e:
        return type(e).__name__

@api.route('/retrain/<password>', methods=['GET'])
def retrain(password):
    '''
    Initiates a re-training thread
    ---------------------------------------------------------------------------------------
    NOTE: Security features can be added in prod
    For ease of verification I am making this synchronous GET;
    This can be made async using POST & flask-executor or celery
    Also updated model is automatically owerwritten in this limited demo
    In prod, a report can be sent and an additional api trigger can be launched to update
    In prod, requests can be tracked by returning a rangen key instead of "Thread started"
    ---------------------------------------------------------------------------------------
    '''
    if password == "p@$$w0rd":
        try:
            #executor.submit(retrain)
            retrain_model()
            return "model updated successfully !!!"
        except Exception as e:
            return type(e).__name__
    else:
        return "Not Allowed"

@api.route('/predict/<name>', methods=['GET'])
def predict(name):
    '''
    A simple prediction endpoint
    '''
    if name:
        try:
            nparr = extract(name)
            if type(nparr) == ndarray:
                lstm = load_model("assets/model/LSTMSimple")
                prediction = lstm.predict_classes(nparr)
                return "Male" if prediction < 1 else "Female"
            else:
                return nparr
        except Exception as e:
            return ''.join("Error on line " + str(exc_info()[-1].tb_lineno) + " | " + str(type(e).__name__) + " | " + str(e))
    else:
        return "Name Needed"

if __name__ == '__main__':
    api.run(host= '0.0.0.0')