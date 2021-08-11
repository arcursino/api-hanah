from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.cadastro.cadastro_db import CadastroDb

api = Namespace('Cadastro',description='Manutenção dados de cadastro')
modelo = api.model('CadastroModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'cpf': fields.String,
    'endereco': fields.String
})
@api.route('/')
class CadastroController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return CadastroDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return CadastroDb.adicionar(request.json), 201

@api.route('/<id>')
class CadastroIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return CadastroDb.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome','Nome da cadastro')
    @api.param('cpf','CPF de cadastro')
    @api.param('endereco','Endereço da cadastro')
    def put(self, id:int):
        return CadastroDb.alterar(int(id), request.json), 201

    def delete(self, id:int):
        return CadastroDb.remover(int(id)), 200
