from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.produtopc.produtopc_db import ProdutoDbpc

api = Namespace('Cadastro',description='Manutenção dados de cadastro')
modelo = api.model('CadastroModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'armazenamento': fields.String,
    'preço':fields.float
})
@api.route('/')
class ProdutoController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return ProdutoDbpc.obter(), 200
    @api.expect(modelo)
    def post(self):
        return ProdutoDbpc.adicionar(request.json), 201

@api.route('/<id>')
class ProdutoIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return ProdutoDbpc.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome','Nome da cadastro')
    def put(self, id:int):
        return ProdutoDbpc.alterar(int(id), request.json), 201

    def delete(self, id:int):
        return ProdutoDbpc.remover(int(id)), 200