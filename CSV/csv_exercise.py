from dataclasses import dataclass as dc
from datetime import datetime, date
from math import ceil


@dc
class Exchange:
    date: datetime
    USD_exchange: float
    EUR_exchange: float
    exchange_id: str


def sort_eur_decrease(exchanges_list_to_sort: list) -> list:
    exchanges_list = exchanges_list_to_sort.copy()
    n = len(exchanges_list)
    while n > 0:
        for exchange in exchanges_list[0:n-1]:
            position = exchanges_list.index(exchange)
            position_to_compare = position + 1
            next_exchange = exchanges_list[position_to_compare]
            if exchange.EUR_exchange > next_exchange.EUR_exchange:
                exchanges_list[position] = next_exchange
                exchanges_list[position_to_compare] = exchange
        n -= 1
    return exchanges_list


def sort_usd_increase(exchanges_list_to_sort: list) -> list:
    exchanges_list = exchanges_list_to_sort.copy()
    n = len(exchanges_list)
    while n > 0:
        for exchange in exchanges_list[0:n-1]:
            position = exchanges_list.index(exchange)
            position_to_compare = position + 1
            next_exchange = exchanges_list[position_to_compare]
            if exchange.USD_exchange < next_exchange.USD_exchange:
                exchanges_list[position] = next_exchange
                exchanges_list[position_to_compare] = exchange
        n -= 1
    return exchanges_list


def read_exchange_csv_file(file_name: str) -> list:
    exchanges_list = []
    with open(file_name) as exchanges_file:
        for line in exchanges_file.readlines()[1:]:
            line_splitted = line.split(",")
            data_object = date.fromisoformat(line_splitted[0])
            one_exchange = Exchange(data_object, float(line_splitted[1]), float(line_splitted[2]), line_splitted[3])
            exchanges_list.append(one_exchange)
    return exchanges_list


def binary_search_of_USD_value(value: float, sorted_increasingly_USD_exchanges_list: list):
    searching_list = sorted_increasingly_USD_exchanges_list.copy()
    while len(searching_list) > 1:
        middle_position = int(ceil((len(searching_list)-1)/2))
        if searching_list[middle_position].USD_exchange > value:
            del searching_list[middle_position:]
        elif searching_list[middle_position].USD_exchange < value:
            del searching_list[0:middle_position]
    print(searching_list)
    return searching_list


if __name__ == '__main__':
    file_name = "kursy_usd_eur.csv"
    exchanges_list = read_exchange_csv_file(file_name)
    sorted_list_eur_decrease = sort_eur_decrease(exchanges_list)
    sorted_list_usd_increase = sort_usd_increase(exchanges_list)
    print("%-8s" %"EURO", "data")
    for exchange in sorted_list_eur_decrease[0:9]:
        print("%-8s" % exchange.EUR_exchange, exchange.date)
    print("%-8s" %"USD", "data")
    for exchange in sorted_list_usd_increase[0:9]:
        print("%-8s" % exchange.USD_exchange, exchange.date)

    binary_search_of_USD_value(3.9011, sorted_list_usd_increase)


