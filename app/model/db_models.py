# import constants as const
from datetime import datetime
from xml.dom.minidom import CharacterData
from peewee import (
    SqliteDatabase, 
    Model,
    AutoField,
    CharField, 
    IntegerField, 
    FloatField, 
    DateTimeField, 
    ForeignKeyField, 
    PrimaryKeyField
    )
import os

# db = SqliteDatabase(const.PEEWEE_DATABASE_URI)
db = SqliteDatabase(f"{os.getcwd()}\\mv_studio_orm.db")

class BaseModel(Model):

    class Meta:

        database = db

class Produtos(BaseModel):
    id = AutoField(column_name='ID')
    nome = CharField(column_name='Nome')
    descricao = CharField(column_name='descricao', null=True)
    preco = FloatField(column_name='Preco')
    qtde = IntegerField(column_name='Qtde')

    class Meta:
        table_name = 'TB_Produtos'

class Vendas(BaseModel):
    id = AutoField(column_name='ID')
    nome_cliente = CharField(column_name='NomeCliente')
    produto = CharField(column_name='Produto')
    qtde = IntegerField(column_name='Qtde')
    valor_total = FloatField(column_name='ValorTotal')
    situacao = CharField(column_name='Situacao')
    data_venda = DateTimeField(column_name='DataVenda', default=datetime.now)

    class Meta:
        table_name = 'TB_Vendas'

class Clientes(BaseModel):
    cpf = CharField(column_name='CPF', primary_key=True)
    nome  = CharField(column_name='Nome')
    data_nascimento = CharField(column_name='DataNascimento')
    email = CharField(column_name='Email')
    ddd = CharField(column_name='DDD')
    telefone = CharField(column_name='Telefone')
    logradouro = CharField(column_name='Logradouro')
    numero = CharField(column_name='Numero')
    complemento = CharField(column_name='Complemento')
    cep = CharField(column_name='CEP', null=True)

    class Meta:
        table_name = 'TB_Clientes'

class Mensalidades(BaseModel):
    ordem = PrimaryKeyField(column_name='Ordem')
    cpf = ForeignKeyField(column_name='CPF', field='cpf', model=Clientes)
    forma_pgto = CharField(column_name='FormaPgto')
    situacao = CharField(column_name='Situacao')
    data_pgto = DateTimeField(default=datetime.now)
    sit_contrato = CharField(column_name='SitContrato')

    class Meta:
        table_name = 'TB_Mensalidades'

class Agendas(BaseModel):
    id = AutoField(column_name='ID')
    cpf = ForeignKeyField(column_name='CPF', field='cpf', model=Clientes)
    modalidade = CharField(column_name='Modalidade')
    dias = CharField(column_name="Dias")
    horario = CharField(column_name="Horario")
    instrutor = CharField(column_name="Instrutor")

    class Meta:
        table_name = 'TB_Agendas'

class Instrutores(BaseModel):
    cpf = ForeignKeyField(column_name='CPF', field='cpf', model=Clientes)
    nome = CharField(column_name='Nome')
    cargo = CharField(column_name='Cargo')
    horario = CharField(column_name='Horario')
    tipo_contrato = CharField(column_name='TipoContrato')
    qtde_alunos = CharField(column_name='QtdeAlunos')
    data_registro = DateTimeField(column_name='DataRegistro')
    data_demissao = DateTimeField(column_name='DataDemissao')

    class Meta:
        table_name = 'TB_Instrutores'