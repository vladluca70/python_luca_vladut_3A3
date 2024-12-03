import requests
from bs4 import BeautifulSoup
from exchange_money import exchange_money

def get_currency_from_website():
    dict = {}
    url = 'https://www.cursbnr.ro/'

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    table1 = soup.find('table', {'class': 'table table-striped table-lg'})
    table = table1.find('tbody')

    for row in table.find_all('tr'):
        cells = row.find_all('td')

        currency = cells[1].text.strip()
        value = cells[2].text.strip()
        dict.update({currency: value})
    return dict

result=get_currency_from_website()
list_of_currency=[]

for value, key in result.items():
    list_of_currency.append([value,key])
list_of_currency.append(['Lei','1'])



amount=float(input("suma de bani="))
from_currency=input("valuta initiala=")
to_currency=input("valuta finala")



exchange_result=exchange_money(amount, from_currency, to_currency, list_of_currency)
print(f"suma {amount} {from_currency} este egala cu {exchange_result} {to_currency}")
