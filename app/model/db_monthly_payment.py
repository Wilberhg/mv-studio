from dataclasses import field
from lib2to3.pytree import Base
from peewee import *
from db_models import BaseModel
from db_customers import TB_Clientes

class TB_Mensalidades(BaseModel):
    Ordem = PrimaryKeyField()
    CPF = ForeignKeyField(TB_Clientes, field='CPF')
    FormaPgto = CharField()
    Situacao = CharField()
    DataPgto = DateTimeField()
    SitContrato = CharField()

if __name__ == '__main__':
    TB_Mensalidades.create_table()