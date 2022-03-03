from ..model.products import Products


def insert_products():
    name, qty, price, desc = None, None, None, None
    counter = 1
    while (not name or not qty or not price):
        if not name:
            name = input("Nome do produto: ")
        if not desc and counter == 1:
            desc = input("Descrição do produto (OPCIONAL): ")
        if not qty:
            qty = input("Quantidade do produto: ")
        if not price:
            price = input("Valor unitário do produto: ")
        counter+=1

    obj = Products(name)
    obj.add_product(item_qty=qty, price=price, description=desc)