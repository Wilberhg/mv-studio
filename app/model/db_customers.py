from lib2to3.pytree import Base
from peewee import *
from db_models import BaseModel

class TB_Clientes(BaseModel):
    CPF = CharField(primary_key=True)
    Nome  = CharField()
    DataNascimento = CharField()
    Email = CharField()
    DDD = CharField()
    Telefone = CharField()
    Logradouro = CharField()
    Numero = CharField()
    Complemento = CharField()
    CEP = CharField(null=True)

if __name__ == '__main__':
    TB_Clientes.create_table()
