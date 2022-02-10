
import re

from dotenv import dotenv_values
from flask import Flask, request

from Account import Account
from Db import Db

app = Flask(__name__)

db = Db(app)

db.get_user_account()

db.make_transaction_request(69,'deposit')


@app.route("/balance", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/transaction/request", methods=['POST'])
def make_transaction_request():
    req_data = request.form
    print(req_data)
    if not req_data:
        return {'error':True,'msg':'Missing request data, specify an amount and type.'}
    if 'amount' not in req_data:
        return {'error':True,'msg':'Missing transaction request amount in request, please provide an int'}
    if 'type' not in req_data:
        return {'error':True,'msg':'''Missing transaction request type in request, please provide 'withdraw' | 'deposit' | 'credit' '''}
    
    # Type check
    number_pattern = '^[0-9]*$'
    amount_str = req_data['amount']
    if not re.match(number_pattern, amount_str):
        return {'error':True,'msg':'Please provide an int as the amount'}
    amount = int(amount_str)
    transaction_type = req_data['type']
    
    if transaction_type != 'withdraw' and transaction_type != 'deposit' and transaction_type != 'credit':
        return {'error':True,'msg':'''Wrong request type, please provide 'withdraw' | 'deposit' | 'credit' '''}
    try:
        #success = db.make_transaction_request(req_data['amount'], req_data['type'])
        if success:
            return {'error':False, 'msg':'Success'}
    except:
        return {'error':True, 'msg': "Failed to save transaction request"}

if __name__ == "__main__":
    app.run()
