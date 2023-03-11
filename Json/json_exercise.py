from dataclasses import dataclass as dc
from datetime import datetime, date
from json import dump

@dc
class Exchange:
    date: datetime
    USD_exchange: float
    EUR_exchange: float
    exchange_id: str


def read_exchange_csv_file(file_name: str) -> list:
    exchanges_list = []
    with open(file_name) as exchanges_file:
        for line in exchanges_file.readlines()[1:]:
            line_splitted = line.split(",")
            data_object = date.fromisoformat(line_splitted[0])
            one_exchange = Exchange(data_object, float(line_splitted[1]), float(line_splitted[2]), line_splitted[3])
            exchanges_list.append(one_exchange)
    return exchanges_list


if __name__ == "__main__":
    exchanges_list = read_exchange_csv_file("C:\\Users\\Hania\\Documents\\Python_projects\\Exercises\\Exercises\\CSV\\kursy_usd_eur.csv")
    with open("C:\\Users\\Hania\\Documents\\Python_projects\\Exercises\\Exercises\\Json\\kursy_usd_eur.txt", "w") as json_file:
        for exchange in exchanges_list:
            exchange_dict = {"date": exchange.date, "USD_exchange": exchange.USD_exchange, "EUR_exchange": exchange.EUR_exchange, "exchange_id": exchange.exchange_id}
            dump(exchange_dict, json_file, indent=4, sort_keys=True, default=str, )


