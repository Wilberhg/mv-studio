class Products:

    def __init__(self, product_name: str, item_type: str, flavor: str, price: float, item_qty: int) -> None:
        self.product_name = self._treat_inputs(product_name)
        self.item_type = self._treat_inputs(item_type)
        self.flavor = self._treat_inputs(flavor)
        self.price = self._treat_money(price)
        self.item_qty = self._treat_qty(item_qty)

    def _treat_inputs(self, text):
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

    def add_product(self):
        ...

    def remove_product(self):
        ...

    def update_product(self):
        ...

    def show_product(self):
        ...