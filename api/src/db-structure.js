const lololo = {
  user: {
    _id: 'ObjectId',
    account: 1,
    balance: 'int', // The current balance of the account
    credit: 'int', // What is owed to the bank
    // This balance is set to the account balance at the start of the interest period.
    // it freezes the max amount of money that can generate interest
    interest_eligible_balance: 'int',
    transactions: {
      // This is a list of all transactions that ever happened
      type: 'deposit | withdraw | deposit_interest | deposit_recurring | credit_payout | credit_payment ',
      amount: 'int',
      created_at: 'number',
      _id: 'ObjectId',
      request_id: 'ObjectId',
    },
    requests: {
      // This is a list of requests for transactions
      type: 'withdraw | deposit | credit',
      status: 'awaiting | approved | declined',
      amount: 'int',
      created_at: 'number',
      finalized_at: 'number',
      _id: 'ObjectId',
      transaction_id: 'ObjectId',
    },
  },
};
