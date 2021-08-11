from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.produtocel.produto_db import ProdutoDbcel

api = Namespace('Celular',description='Descrição de Celulares')
modelo = api.model('CadastroModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'armazenamento': fields.String,
    'preço': fields.Integer
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

@api.route('/<preco>')
class ProdutoIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, preco:int):
        return ProdutoDbcel.obter(int(preco)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('preco','Preço do Produto')
    def put(self, preco:int):
        return ProdutoDbcel.alterar(int(preco), request.json), 201

    def delete(self, preco:int):
        return ProdutoDbcel.remover(int(preco)), 200

@api.route('/<armazenamento>')
class ProdutoIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, armazenamento:str):
        return ProdutoDbcel.obter(str(armazenamento)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('armazenamento','Armazenamento do Produto')
    def put(self, armazenamento:str):
        return ProdutoDbcel.alterar(str(armazenamento), request.json), 201

    def delete(self, armazenamento:str):
        return ProdutoDbcel.remover(str(armazenamento)), 200