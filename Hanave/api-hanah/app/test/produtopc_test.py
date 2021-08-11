from app.test.test_base import BaseTestCase

class produtopcTest(BaseTestCase):
    def test_produtopc_respondendo(self):
        response = self.client.get('/api/produtopc/1')
        self.assert200(response)
        self.assertEqual(response.json, {
            'id': 1,
            'nome': 'Samsung',
            'processador': 'intel 3',
            'armazenamento':'120Gb',
            'preço':'1.000,00R$'
        })