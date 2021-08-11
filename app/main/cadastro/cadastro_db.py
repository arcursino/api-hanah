class CadastroDb:
    items = [
        {
            'id': 1,
            'nome': 'Jozimar Back',
            'cpf': '04353788051',
            'endereco': 'Rua Bosque, 103. cep: 55115670'
        },
        {
            'id': 2,
            'nome': 'Maria Antonieta',
            'cpf': '79463515003',
            'endereco': 'Rua Verdinho, 139. cep: 77115670'
        },
        {
            'id': 3,
            'nome': 'Rebecca Braz',
            'cpf': '15889975021',
            'endereco': 'Rua Bosquinho, 13. cep: 66115670'
        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True
    @classmethod
    def obter(cls, id=None):
        if id:
            return next(filter(lambda x: x['id'] == id,cls.items),{})
        return cls.items
    @classmethod
    def remover(cls, id):
        # cls.items = [for item in cls.items if item['id'] != id]
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}
    @classmethod
    def alterar(cls, id, novo_item:dict):
        item = next(filter(lambda x: x['id'] == id,cls.items),{})
        index = cls.items.index(item)

        if novo_item.get('nome'):
            item['nome'] = novo_item.get('nome')

        if novo_item.get('cpf'):
            item['cpf'] = novo_item.get('cpf')
        
        if novo_item.get('endereco'):
            item['endereco'] = novo_item.get('endereco')

        cls.items[index] = item
        return item