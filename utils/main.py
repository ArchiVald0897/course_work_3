import json


def load_file():
    """загружаем данных из файла"""
    with open('operations.json', "r", encoding='utf-8') as f:
        return json.load(f)


def successful_operations():
    executed_transactions = []
    for transaction in load_file():
        if transaction.get("state") == "EXECUTED":
            executed_transactions.append(transaction)

    last_five_executed_transactions = executed_transactions[-5:]
    return last_five_executed_transactions


print(successful_operations())
