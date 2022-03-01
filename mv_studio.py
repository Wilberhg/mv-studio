from peewee import *

database = SqliteDatabase('mv_studio.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class TbClientes(BaseModel):
    cep = TextField(column_name='CEP', null=True)
    cpf = TextField(column_name='CPF', primary_key=True)
    complemento = TextField(column_name='Complemento')
    ddd = TextField(column_name='DDD')
    data_nascimento = TextField(column_name='DataNascimento')
    e_mail = TextField(column_name='E-mail')
    logradouro = TextField(column_name='Logradouro')
    nome = TextField(column_name='Nome')
    numero = TextField(column_name='Numero')
    telefone = TextField(column_name='Telefone')

    class Meta:
        table_name = 'TB_Clientes'

class TbCompras(BaseModel):
    data_venda = TextField(column_name='DataVenda')
    id = AutoField(column_name='ID')
    nome_cliente = TextField(column_name='NomeCliente')
    produto = TextField(column_name='Produto')
    qtde = IntegerField(column_name='Qtde')
    situacao = TextField(column_name='Situacao')
    valor_total = FloatField(column_name='ValorTotal')

    class Meta:
        table_name = 'TB_Compras'

class TbInstrutores(BaseModel):
    cpf = TextField(column_name='CPF', primary_key=True)
    cargo = TextField(column_name='Cargo')
    data_registro = TextField(column_name='DataRegistro')
    horario = TextField(column_name='Horario')
    nome = TextField(column_name='Nome')
    quant_alunos = TextField(column_name='QuantAlunos')
    tipo_contrato = TextField(column_name='TipoContrato')

    class Meta:
        table_name = 'TB_Instrutores'

class TbMensalidades(BaseModel):
    cpf = ForeignKeyField(column_name='CPF', field='cpf', model=TbClientes)
    data_pgto = TextField(column_name='DataPgto')
    forma_pgto = TextField(column_name='FormaPgto')
    ordem = AutoField(column_name='Ordem')
    sit_contrato = TextField(column_name='SitContrato')
    situacao = TextField(column_name='Situacao')

    class Meta:
        table_name = 'TB_Mensalidades'

class TbProdutos(BaseModel):
    descricao = TextField(column_name='Descricao', null=True)
    id = AutoField(column_name='ID')
    nome = TextField(column_name='Nome')
    preco = FloatField(column_name='Preco')
    qtde = IntegerField(column_name='Qtde')

    class Meta:
        table_name = 'TB_Produtos'

class TbTreinos(BaseModel):
    cpf = TextField(column_name='CPF')
    dias = TextField(column_name='Dias')
    horario = TextField(column_name='Horario', null=True)
    id = AutoField(column_name='ID')
    instrutor = TextField(column_name='Instrutor')
    modalidade = TextField(column_name='Modalidade')

    class Meta:
        table_name = 'TB_Treinos'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

