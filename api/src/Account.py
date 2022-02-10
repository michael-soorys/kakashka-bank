from typing import List, Literal

from flask_pymongo import ObjectId

from TransactionRequest import TransactionRequest


class Account:
  
  def __init__(self,user_document=None, _id=ObjectId):
    if user_document:
      self._id = user_document['_id']
      self.account = user_document['account']
      self.balance = user_document['balance']
      self.credit = user_document['credit']
      self.interest_eligible_balance = user_document['interest_eligible_balance']
      self.transactions = user_document['transactions']
      # Initialize a list of TransactionRequest objects
      self.requests = []
      for request in user_document['requests']:
        self.requests.append(TransactionRequest(request))
    else:
      self._id = _id
      self.is_initialized_from_scratch = True
      self.account= 1
      self.balance= 0
      self.credit= 0
      self.interest_eligible_balance= 0
      self.transactions= []
      self.requests= []
    print(self)
  
  def __str__(self):
    return str(self.get_account_document_dict())
  
  def get_account_document_dict(self):
    requests_list = []
    for req in self.requests:
      requests_list.append(req.get_transaction_request_dict())
    return {
      '_id':self._id,
      'account': self.account,
      'balance': self.balance,
      'credit': self.credit,
      'interest_eligible_balance': self.interest_eligible_balance,
      'transactions': self.transactions,
      'requests': requests_list
    }
  
  
  def make_transaction_request(self, amount: int, type: Literal['withdraw' , 'deposit' ,'credit']):
    request = TransactionRequest({'amount':amount,'type':type})
    self.requests.append(request)
  
  # def approve_transaction_request(self, id:int, requests:List(TransactionRequest)):
    
