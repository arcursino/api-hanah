from app.test.test_base import BaseTestCase

class produtoTest(BaseTestCase):
    def test_produto_respondendo(self):
        response = self.client.get('/api/produto/1')
        self.assert200(response)
        self.assertEqual(response.json, {
            'id': 1,
            'nome': 'Samsung j7',
            'processador': 'quadcore',
            'armazenamento': '64Gb',
            'preço':'800,00R$'
        })