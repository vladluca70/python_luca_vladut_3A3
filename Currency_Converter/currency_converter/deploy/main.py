from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


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


def exchange_money(amount, from_currency, to_currency, lista_of_currency):
    y = 0
    from_currency_value = 0
    to_currency_value = 0
    for x in lista_of_currency:
        if x[0] == from_currency:
            y += 1
            from_currency_value = float(x[1])
        if x[0] == to_currency:
            y += 2
            to_currency_value = float(x[1])
    if y != 3:
        return None
    amount = amount * from_currency_value
    amount = amount / to_currency_value

    amount = round(amount, 4)

    return amount


def final_dict():
    result = get_currency_from_website()
    list_of_currency = []

    for value, key in result.items():
        list_of_currency.append([value, key])
    list_of_currency.append(['Lei', '1'])
    return list_of_currency


@app.route('/', methods=['GET', 'POST'])
def index():
    currencies = [currency[0] for currency in final_dict()]
    selected_from_currency = currencies[0]
    selected_to_currency = currencies[0]
    amount = 0
    result = None

    if request.method == 'POST':
        selected_from_currency = request.form.get('from_currency')
        selected_to_currency = request.form.get('to_currency')
        amount = float(request.form.get('amount'))

        result = exchange_money(amount, selected_from_currency, selected_to_currency, final_dict())

    return render_template('index.html',
                           currencies=currencies,
                           selected_from_currency=selected_from_currency,
                           selected_to_currency=selected_to_currency,
                           amount=amount,
                           result=result)


if __name__ == '__main__':
    app.run(debug=True)
