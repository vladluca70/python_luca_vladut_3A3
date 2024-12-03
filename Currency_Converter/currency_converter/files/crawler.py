import requests
from bs4 import BeautifulSoup

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