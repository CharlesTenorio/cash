from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property

class Empresa(Node):
    cnpj = ndb.StringProperty(required=True)
    razao_social = ndb.StringProperty(required=True)
    fantasia = ndb.StringProperty(required=True)
    cep = ndb.StringProperty(required=True)
    endereco = ndb.StringProperty(required=True)
    bairro  = ndb.StringProperty(required=True)
    cidade  = ndb.StringProperty(required=True)
    uf  = ndb.StringProperty(required=True)
    fone  = ndb.StringProperty(required=True)
    email  = ndb.StringProperty(required=True)
    responsavel  = ndb.StringProperty(required=True)
    cel_responsavel  = ndb.StringProperty(required=True)
    data_cadastro = ndb.DateTimeProperty(auto_now_add=True)
    status = ndb.StringProperty(default= 'Ativo')

class Corretor(Node):
    cpf = ndb.StringProperty(required=True)
    nome = ndb.StringProperty(required=True)
    sexo = ndb.StringProperty(required=True)
    nascimento = ndb.DateProperty(required=True)
    cep = ndb.StringProperty(required=True)
    endereco = ndb.StringProperty(required=True)
    bairro = ndb.StringProperty(required=True)
    cidade = ndb.StringProperty(required=True)
    uf = ndb.StringProperty(required=True)
    fone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    cel = ndb.StringProperty(required=True)
    data_cadastro = ndb.DateTimeProperty(auto_now_add=True)
    status = ndb.StringProperty(default='Ativo')
    percentual = ndb.FloatProperty(default=10)

class Banco(Node):
    codigo = ndb.StringProperty()
    banco = ndb.StringProperty()



class Emprestimos(Node):
      cnpj_empresa = ndb.StringProperty(required=True)
      empresa = ndb.StringProperty(required=True)
      numero_contrato = ndb.StringProperty(required=True)
      tipo_contrato = ndb.StringProperty(choices=['Novo', 'Portabilidade'], default='Novo', required=True)
      numero_beneficio = ndb.StringProperty(required=True)
      cpf_corretor = ndb.StringProperty(required=True)
      corretor = ndb.StringProperty(required=True)
      percentual_corretor = ndb.FloatProperty(required=True)
      nome = ndb.StringProperty(required=True)
      cpf = ndb.StringProperty(required=True)
      identidade = ndb.StringProperty(required=True)
      nascimento = ndb.DateProperty(required=True)
      sexo = ndb.StringProperty(choices=['Masculino', 'Feminino'])
      pai = ndb.StringProperty(required=True)
      mae= ndb.StringProperty(required=True)
      apelido = ndb.StringProperty(required=True)
      cep = ndb.StringProperty(required=True)
      endereco = ndb.StringProperty(required=True)
      bairro = ndb.StringProperty(required=True)
      cidade = ndb.StringProperty(required=True)
      uf = ndb.StringProperty(required=True)
      referencia = ndb.StringProperty(required=True)
      fone = ndb.StringProperty(required=True)
      celular= ndb.StringProperty(required=True)
      fone_contato = ndb.StringProperty()
      banco_emprestimo = ndb.StringProperty(required=True)
      taxa_banco = ndb.FloatProperty(required=True)
      valor_beneficio = property.SimpleCurrency(required=True)
      total_emprestimo = property.SimpleCurrency(required=True)
      valor_empresa = property.SimpleCurrency(required=True)
      valor_corretor = property.SimpleCurrency(required=True)
      banco_cliente = ndb.StringProperty(required=True)
      agencia_cliente = ndb.StringProperty(required=True)
      conta_cliente = ndb.StringProperty(required=True)
      data_ultima_parcela = ndb.DateProperty(required=True)
      email = ndb.StringProperty(required=True)
      responsavel = ndb.StringProperty(required=True)




