import json
import requests

cache = {}
base_currency = input("What currency do you want to exchange?\n").lower()
url = f"http://www.floatrates.com/daily/{base_currency}.json"
data = requests.get(url)

currencies_json = json.loads(data.text)


if base_currency != 'usd':
    cache['usd'] = currencies_json['usd']
if base_currency != 'eur':
    cache['eur'] = currencies_json['eur']
while True:
    exchange_currency = input("What currency you want to exchange to?\n").lower()
    if exchange_currency == "":
        break
    money = float(input("How much {} do you want to exchange? If you want to end, just press enter\n".format(base_currency)))

    print("Checking the cache...")
    if exchange_currency in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[exchange_currency] = currencies_json[exchange_currency]
    print("You received {} {name}.".format(round((money * cache[exchange_currency.lower()]['rate']), 2), name=exchange_currency.upper()))
