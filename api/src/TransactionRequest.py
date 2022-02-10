import time
from typing import Literal

from flask_pymongo import ObjectId


class TransactionRequest:
  def __init__(self,transaction_request):
    self.type = transaction_request['type']
    self.amount = transaction_request['amount']
    self.status = transaction_request['status'] if 'status' in transaction_request  else 'awaiting'
    self.created_at = transaction_request['created_at'] if 'created_at' in transaction_request else time.time()
    self.finalized_at = transaction_request['finalized_at'] if 'finalized_at' in transaction_request else -1
    self._id = transaction_request['_id'] if '_id' in transaction_request else ObjectId()
    self.transaction_id = transaction_request['transaction_id'] if 'transaction_id' in transaction_request else None
  
  def get_transaction_request_dict(self):
    return {
      'type':self.type,
      'amount': self.amount,
      'status':self.status,
      'created_at':self.created_at,
      'finalized_at':self.finalized_at,
      '_id':self._id,
      'transaction_id': self.transaction_id
    } 
  
  def change_status(self,status: Literal['awaiting' , 'approved' ,'declined']):
    self.status = status
    if status == 'approved':
      self.finalized_at = time.time()
    return
