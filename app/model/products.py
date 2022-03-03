# from ..model.conn_sqlite3 import Database
from ..model.conn_sqlite3 import Database
from ..model.db_models import Produtos
from prettytable import PrettyTable

class Products:

    def __init__(self, product_name: str) -> None:
        self.product_name = self._treat_input(product_name)

    def _treat_input(self, text):
        if text:
            text = text.strip()
            text = text.title()
            return text

    def _treat_money(self, money):
        money = money.strip()
        money = money.replace(',', '.')
        money = float(money)
        return money

    def _treat_qty(self, qty):
        qty = qty.strip()
        qty = int(qty)
        return qty

    def add_product(self, price: float, item_qty: int, description: str = None):
        desc = self._treat_input(description)
        price = self._treat_money(price)
        item_qty = self._treat_qty(item_qty)
        Produtos.create(
            nome=self.product_name,
            descricao=desc,
            preco=price,
            qtde=item_qty
        )

    def remove_product(self, id):
        Produtos.delete().where(Produtos.id == id)

    def update_product(self, id: int, column: str, new_value: str):
        Produtos.update({Produtos.nome: new_value}).where(Produtos.id == id)

    def show_product(self):
        result = Produtos.select()
        result = result.tuples()
        return result

    def beautiful_view(self, result):
        table = PrettyTable()
        for row in result:
            table.add_row(row)
        return table

if __name__ == '__main__':
    obj = Products('barra cereal bold - chocolate')
    # obj.add_product('5,25', '10')
    result = obj.show_product()
    if len(result) > 0:
        print('Produto registrado com êxito!')
    else:
        print('Produto NÃO pode ser registrado. Verifique com o administrador do sistema.')
    