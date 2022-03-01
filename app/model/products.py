# from ..model.conn_sqlite3 import Database
from conn_sqlite3 import Database
from typing import Union

class Products:

    def __init__(self, product_name: str) -> None:
        self.product_name = self._treat_input(product_name)

    def _treat_input(self, text):
        if text:
            text = text.strip()
            text = text.title()
            return text

    def _treat_money(self, money):
        money = money.replace(',', '.')
        money = float(money)
        return money

    def _treat_qty(self, qty):
        qty = int(qty)
        return qty

    def add_product(self, price: float, item_qty: int, description: str = None):
        desc = self._treat_input(description)
        price = self._treat_money(price)
        item_qty = self._treat_qty(item_qty)
        try:
            obj = Database('mv_studio.db')
            if desc:
                query = f"INSERT INTO TB_Produtos (Nome, Descricao, Preco, Qtde) VALUES ('{self.product_name}', '{desc}', {price}, {item_qty})"
            else:
                query = f"INSERT INTO TB_Produtos (Nome, Preco, Qtde) VALUES ('{self.product_name}', {price}, {item_qty})"
            obj.do_insert_update(query)
            return True
        except BaseException as err:
            return False

    def remove_product(self, id):
        try:
            obj = Database('mv_studio.db')
            obj.do_insert_update(f"DELETE FROM TB_Produtos WHERE ID = {id}")
            return True
        except:
            return False

    def update_product(self, id: int, column: str, new_value: str):
        try:
            obj = Database('mv_studio.db')
            obj.do_insert_update(f"UPDATE TB_Produtos SET {column} = {new_value} WHERE ID = {id}")
            return True
        except:
            return False

    def show_product(self):
        result = []
        try:
            obj = Database('mv_studio.db')
            result = obj.do_select(f"SELECT * FROM TB_Produtos")
            return result
        except:
            return result

if __name__ == '__main__':
    obj = Products('barra cereal bold - chocolate')
    result = obj.show_product()
    if result:
        print('Produto registrado com êxito!')
    else:
        print('Produto NÃO pode ser registrado. Verifique com o administrador do sistema.')
    