from config import db

#Transaction model
class Transaction(db.Model):
    __tablename__ = 'transaction'
    transaction_id = db.Column(db.String, primary_key=True)
    account_id = db.Column(db.String, db.ForeignKey('account.account_id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(db.DateTime))

    account = db.relationship("Account", back_populates='transactions')

    def to_json(self):
        return {
            "transaction_id": self.transaction_id,
            "account_id": self.account_id,
            "amount": self.amount,
            "created_at": self.created_at
        }

#Account model
class Account(db.Model):
    __tablename__ = 'account'

    account_id = db.Column(db.String(80), primary_key=True)
    balance = db.Column(db.Integer)
    transactions = db.relationship("Transaction", back_populates="account")
    transaction_requests = db.relationship("TransactionRequest", back_populates="account")

    def to_json(self):
        return {
            "account_id": self.account_id,
            "balance": self.balance
        }

#Transaction model
class TransactionRequest(db.Model):
    __tablename__ = 'transaction_request'

    transaction_id = db.Column(db.String, primary_key=True)
    account_id = db.Column(db.String, db.ForeignKey('account.account_id'))
    amount = db.Column(db.Integer)

    account = db.relationship("Account", back_populates="transaction_requests")