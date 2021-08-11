from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.produtocel.produto_db import ProdutoDbcel

api = Namespace('Cadastro',description='Manutenção dados de cadastro')
modelo = api.model('CadastroModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'armazenamento': fields.String,
    'preço': fields.float
})
@api.route('/')
class ProdutoController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return ProdutoDbcel.obter(), 200
    @api.expect(modelo)
    def post(self):
        return ProdutoDbcel.adicionar(request.json), 201

@api.route('/<id>')
class ProdutoIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return ProdutoDbcel.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome','Nome da cadastro')
    def put(self, id:int):
        return ProdutoDbcel.alterar(int(id), request.json), 201

    def delete(self, id:int):
        return ProdutoDbcel.remover(int(id)), 200