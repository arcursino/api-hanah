class ProdutoDbcel:
    items = [
        {
            'id': 1,
            'nome': 'Samsung j7',
            'processador': 'quadcore',
            'armazenamento':'64Gb',
            'preço': 800
        },
        {
            'id': 2,
            'nome': 'Iphone 6s',
            'processador': 'iOs',
            'armazenamento':'128Gb',
            'preço':1.200

        },
        {
            'id': 3,
            'nome': 'Iphone 10',
            'processador': 'iOs',
            'armazenamento':'128Gb',
            'preço': 5.000
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

        if novo_item.get('processador'):
            item['processador'] = novo_item.get('processador')

        if novo_item.get('armazenamento'):
            item['armazenamento'] = novo_item.get('armazenamento')

        cls.items[index] = item
        return item


