from peewee import *
# from ..model.db_models import BaseModel
from db_models import BaseModel

class TB_Produtos(BaseModel):
    Nome = CharField()
    Descricao = CharField(null=True)
    Preco = FloatField()
    Qtde = IntegerField()

if __name__ == '__main__':
    TB_Produtos.create_table()