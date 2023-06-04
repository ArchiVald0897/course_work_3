import datetime
import json
import os


def load_file():
    """Получаем данные из файла operations.json"""
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path, '..', 'utils', 'operations.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def successful_operations():
    """Получаем 5 последних успешных операций"""
    executed_transactions = []
    for transactions in load_file():
        if transactions.get("state") == "EXECUTED":
            executed_transactions.append(transactions)
    last_five_executed_transactions = executed_transactions[-5:]
    return last_five_executed_transactions


def format_date(date_str):
    """Форматирует дату в формат ДД.ММ.ГГГГ"""
    date = datetime.datetime.fromisoformat(date_str)
    return date.strftime("%d.%m.%Y")


def mask_card_number(card_numbers):
    """Маскирует номер карты в формате XXXX XX** **** XXXX"""
    if len(card_numbers) >= 10:
        card_text = card_numbers.split(" ")[0]
        card_num = card_numbers.split(" ")[1]
        mask_number = card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]
        visible_card_number = card_text + " " + mask_number + " -> Счет "
    else:
        visible_card_number = ""
    return visible_card_number


def mask_account_number(account_number):
    """Маскирует номер счета в формате ****************XXXX"""
    if account_number:
        visible_part = "*" * 16 + account_number.split()[-1][-4:]
    else:
        visible_part = ""
    return visible_part


def format_transaction(transaction):
    """Форматирует транзакцию в заданном формате"""
    formatted_date = format_date(transaction.get("date", ""))
    masked_card_number = mask_card_number(transaction.get("from", ""))
    masked_account_number = mask_account_number(transaction.get("to", "")[-4:])
    formatted_description = transaction.get("description", "")
    amount_dict = transaction.get("operationAmount", {"amount": "", "currency": {"name": ""}})
    formatted_amount = amount_dict["amount"] + " " + amount_dict["currency"]["name"]
    return f"{formatted_date} {formatted_description}\n{masked_card_number}{masked_account_number}\n" \
           f"{formatted_amount}\n"


def formatted_successful_operations():
    """Форматирует 5 последних успешных операций"""
    transactions = successful_operations()
    formatted_transactions = []
    for transaction in transactions:
        formatted_transactions.append(format_transaction(transaction))
    return "\n".join(formatted_transactions)
