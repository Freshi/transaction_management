from flask import request, jsonify
from config import app, db
from models import Transaction
from datetime import datetime
import logging as log

@app.route('/transactions', methods=['GET', 'POST'])
def transact():
    if request.method == "POST":
        log.warning('....ok....')
        transaction_id = request.json.get('transactionId')
        account_id = request.json.get('accountId')
        amount = request.json.get('amount')
        created_at = request.json.get('createdAt')
        log.warning('ok 2')

        if not transaction_id or not account_id or not amount or not created_at:
            return (jsonify({"description": "Mandatory body parameters missing or have incorrect type"}),
                    400
                    )
        new_transaction = Transaction(transaction_id=transaction_id, account_id=account_id, amount = amount, created_at=created_at)
        
        log.warning('....ok....')
        try:
            db.session.add(new_transaction)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        
        return jsonify({"Transaction created."})
    
    else:
        transactions = Transaction.query.all()
        transactions_json = list(map(lambda x: x.to_json(), transactions))
        return jsonify({"description": 'Get transactions',
                        "content": transactions_json
                        })



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)














#paths to define
#/ping - get - 200 description: 'The service is up and running'
#/transactions/ - post - 201 - description: Transaction created content: transaction