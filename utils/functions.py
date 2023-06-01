import json


def load_file():
    """загружаем данных из файла"""
    with open('operations.json', "r", encoding='utf-8') as f:
        return json.load(f)


def successful_operations():
    executed_transactions = []
    for transactions in load_file():
        if transactions.get("state") == "EXECUTED":
            executed_transactions.append(transactions)

    last_five_executed_transactions = executed_transactions[-5:]
    return last_five_executed_transactions
