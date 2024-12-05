from crawler import get_currency_from_website

def final_dict():
    result=get_currency_from_website()
    list_of_currency=[]

    for value, key in result.items():
        list_of_currency.append([value,key])
    list_of_currency.append(['Lei','1'])
    return list_of_currency