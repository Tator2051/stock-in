import requests
import json
from yafi import YaFi

# Otra clase que se llame MAIN y que se le pase el comando y el período, de allí se deriva a las apis según
# lo que diga el config
apple = YaFi('AAPL')
apple.getClose()

