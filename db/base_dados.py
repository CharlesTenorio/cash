from google.appengine.ext import ndb

class Empresa(ndb.Model):
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

class Corretor(ndb.Model):
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

class Banco(ndb.Model):
    codigo = ndb.StringProperty()
    banco = ndb.StringProperty()



class Emprestimos(ndb.Model):
      cnpj_empresa = ndb.StringProperty(required=True)
      empresa = ndb.StringProperty(required=True)
      numero_contrato = ndb.StringProperty(required=True)
      tipo_contrato = ndb.StringProperty(required=True)
      nome = ndb.StringProperty(required=True)
      cpf = ndb.StringProperty(required=True)
      identidade = ndb.StringProperty(required=True)
      nascimento = ndb.DateProperty(required=True)
      pai = ndb.StringProperty(required=True)
      mae= ndb.StringProperty(required=True)
      apelido = ndb.StringProperty(required=True)
      cep = ndb.StringProperty(required=True)
      endereco = ndb.StringProperty(required=True)
      bairro = ndb.StringProperty(required=True)
      cidade = ndb.StringProperty(required=True)
      uf = ndb.StringProperty(required=True)
      fone = ndb.StringProperty(required=True)
      email = ndb.StringProperty(required=True)
      responsavel = ndb.StringProperty(required=True)




