from app.test.test_base import BaseTestCase

class CadastroTest(BaseTestCase):
    def test_cadastro_respondendo(self):
        response = self.client.get('/api/cadastro/1')
        self.assert200(response)
        self.assertEqual(response.json, {
            'id': 1,
            'nome': 'Jozimar Back',
            'cpf': '04353788051'
        })