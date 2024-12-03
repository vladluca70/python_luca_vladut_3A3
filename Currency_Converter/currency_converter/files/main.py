from exchange_money import exchange_money
from crawler import get_currency_from_website




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
