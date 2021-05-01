import requests
import json

"""
Fuera de uso!!
"""

lista = ['AAPL']


def get_close(ticker):
    url = f"https://query1.finance.yahoo.com/v7/finance/spark?symbols={ticker}%3DF&range=1d&interval=5m&indicators=close&includeTimestamps=false&includePrePost=false&corsDomain=finance.yahoo.com&.tsrc=finance"
    dsa = f'https://query1.finance.yahoo.com/v7/finance/spark?symbols=%5ERUT&range=1d&interval=5m&indicators=close&includeTimestamps=false&includePrePost=false&corsDomain=finance.yahoo.com&.tsrc=finance'
    json = requests.get(url).json()
    result = json['spark']['result']
    for element in result:
        response = element['response']

    for item in response:
        get_close = item['indicators']['quote']

    for list_close in get_close:
        close = list_close['close']

    return close


for ticker in lista:
    close = get_close(ticker)
    print(f'EL CLOSE PARA {ticker} es: {close}')