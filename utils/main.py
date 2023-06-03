from functions import successful_operations
from datetime import datetime


for item in successful_operations():
    # преобразуем дату в формат DD.MM.YYYY
    date = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f").date()
    date_str = date.strftime("%d.%m.%Y")

    # добавляем переменную description
    description = item['description']

    # преобразуем номер карты
    if "from" in item:
        from_account = item.get("from")
        account_name = from_account.split(" ")[0]
        card_num = item["from"][item["from"].rfind(" ") + 1:]
        card_num = card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]
        personal_account = f"{'*' * 16}{item['to'][-4:]}"
        # выводим данные в нужном формате
        print(f"{date_str} {description}")
        print(f"{account_name} {card_num} -> Счет {personal_account}")
        print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['code']}\n")
    else:
        # выводим данные в нужном формате если нет from
        print(f"{date_str} {description}")
        print(f"Счет {personal_account}")
        print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['code']}\n")
