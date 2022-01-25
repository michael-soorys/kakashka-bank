
class Account:
  
  def __init__(self,user_document=None):
    if user_document:
      self._id = user_document['_id']
      self.account = user_document['account']
      self.balance = user_document['balance']
      self.credit = user_document['credit']
      self.interest_eligible_balance = user_document['interest_eligible_balance']
      self.transactions = user_document['transactions']
      self.requests = user_document['requests']
    else:
      self.is_initialized_from_scratch = True
      self.account= 1
      self.balance= 0
      self.credit= 0
      self.interest_eligible_balance= 0
      self.transactions= []
      self.requests= []
  
  def get_user_document_dict(self):
    return {
      '_id':self._id,
      'account': self.account,
      'balance': self.balance,
      'credit': self.credit,
      'interest_eligible_balance': self.interest_eligible_balance,
      'transactions': self.transactions,
      'requests': self.requests
  }
  
  
