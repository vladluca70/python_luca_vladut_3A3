def exchange_money(amount, from_currency, to_currency, lista_of_currency):
    y=0
    from_currency_value=0
    to_currency_value=0
    for x in lista_of_currency:
        if x[0]==from_currency:
            y=y+1
            from_currency_value=float(x[1])
        if x[0]==to_currency:
            y=y+2
            to_currency_value=float(x[1])
    if y!=3:
        print ("moneda nu exista")
        return None
    amount=amount*from_currency_value
    amount=amount/to_currency_value
    return amount