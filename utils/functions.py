import json
import os


def load_file():
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path, '..', 'utils', 'operations.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def successful_operations():
    executed_transactions = []
    for transactions in load_file():
        if transactions.get("state") == "EXECUTED":
            executed_transactions.append(transactions)

    last_five_executed_transactions = executed_transactions[-5:]
    return last_five_executed_transactions
