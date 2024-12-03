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

        if len(cells) > 1:
            currency = cells[1].get_text(strip=True)
            value = cells[2].get_text(strip=True)
            dict.update({currency: value})
    return dict

result=get_currency_from_website()
for x, y in result.items():
    print(f"{x} : {y}")
