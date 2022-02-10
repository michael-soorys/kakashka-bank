import os
from typing import Literal

from dotenv import dotenv_values
from flask import Flask
from flask_pymongo import ObjectId, pymongo

from Account import Account
from config import Config


class Db:
  
  def __init__(self,app:Flask):
    config = Config.getConfig(app.config['ENV'])
    dir_path = os.path.dirname(os.path.realpath(__file__))
    env = dotenv_values(dir_path + '/.env')

    # Connect to database
    connection_string = env['MONGO_URI']
    client = pymongo.MongoClient(connection_string)
    db = client.get_database('main')
    self.user_collection = pymongo.collection.Collection(db, config['dbCollection'])
    
    # Initialize the starter document if missing
    userObjTest = self.get_user_account_doc()
    if userObjTest is None:
      print('- No account exists, creating it...')
      self.init_user_account()
    else:
      print('- Found a user account, all good.')
  
  def get_user_account_doc(self):
    return self.user_collection.find_one({"account": 1})
  
  def get_user_account(self):
    db_account = self.user_collection.find_one({"account": 1})
    return Account(db_account)

  def init_user_account(self):
    _id = ObjectId()
    initAccount = Account(_id=_id)
    print('- Initialized the account document with an id ' + str(_id))
    self.save(initAccount)
  
  def save(self, account: Account):
    account_dict = account.get_account_document_dict()
    res = self.user_collection.update_one({'_id':account._id},{'$set':account_dict}, upsert=True)
    return res.acknowledged
  
  def make_transaction_request(self, amount: int, type: Literal['withdraw' , 'deposit' ,'credit']):
    account = self.get_user_account()
    account.make_transaction_request(amount,type)
    success = self.save(account)
    return success
