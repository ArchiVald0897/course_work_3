from functions import successful_operations
from datetime import datetime


for item in successful_operations():
    # преобразуем дату в формат DD.MM.YYYY
    date = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f").date()
    date_str = date.strftime("%d.%m.%Y")
    from_account = item.get("from")
    if from_account is not None:
        account_name = from_account.split(" ")[0]
    else:
        account_name = ""

    # заменяем значения в строке description
    description = item['description'].replace('Maestro', 'MasterCard')
    description = description.replace('Visa Platinum', 'Visa')
    description = description.replace('открытие вклада', 'открытие депозита')

    # преобразуем номер карты
    if "from" in item:
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
