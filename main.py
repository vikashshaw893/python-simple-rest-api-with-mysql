import json
import os
import time

from config import parameters as params
from app import app
from flask import jsonify, request
from helpers import db_deal

print(time.strftime('%Y-%m-%d %H:%M:%S'))  # before timezone change
os.environ['TZ'] = params.TIME_ZONE  # set new timezone
try:
    time.tzset()
except AttributeError:
    pass
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # after timezone change

# creating object to interact with DB
dbDealObj = db_deal.DbDeal()


# CRUD Operation
@app.route('/test', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def test():
    """Test link"""
    response = jsonify({"status": "true", "message": "test link"})
    response.status_code = 200
    return response


@app.errorhandler(404)
def page_not_found(e):
    """404 error"""
    response = jsonify({"status": "false", "message": e.__dict__})
    response.status_code = 404
    return response, 404


@app.errorhandler(400)
def page_not_found(e):
    """400 error"""
    response = jsonify({"status": "false", "message": e.__dict__})
    response.status_code = 400
    return response, 400


@app.errorhandler(500)
def page_not_found(e):
    """500 error"""
    response = jsonify({"status": "false", "message": e.__dict__})
    response.status_code = 500
    return response, 500


@app.route('/getScriptList', methods=['POST', 'GET'])
def getScriptList():
    """----"""
    jsonReq = request.json
    print(jsonReq)
    records = dbDealObj.getSharesToDealWithSocket()
    response = jsonify({"status": "true", "data": records})
    return response


@app.route('/saveFirstSocketData', methods=['POST'])
def saveFirstSocketData():
    """"""
    req = request.json
    print(req)
    status = dbDealObj.saveFirstSocketOpeningData(req)

    if status:
        response = jsonify({"status": "true", "data": None})
    else:
        response = jsonify({"status": "false", "data": None})

    return response


@app.route('/saveOrderDetail', methods=['POST'])
def saveOrderDetail():
    """"""
    req = request.json
    status = dbDealObj.saveOrderDetail(req)
    if status:
        response = jsonify({"status": "true", "data": None})
    else:
        response = jsonify({"status": "false", "data": None})

    return response


if __name__ == "__main__":
    app.run(debug=params.DEV_ENV, port=params.PORT)
