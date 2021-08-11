class produtonotDb:
    items = [
        {
            'id': 1,
            'nome': 'Samsung',
            'processador': 'intel 3',
            'armazenamento':'120Gb',
            'preço':'1.000,00R$'
        },
        {
            'id': 2,
            'nome': 'Lenovo',
            'processador': 'intel 5',
            'armazenamento':'500gb',
            'preço':'2.500,00R$'
        },
        {
            'id': 3,
            'nome': 'Macbook',
            'processador': 'intel 8',
            'armazenamento':'1Tb',
            'preço':'5.000,00R$'
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
        if  novo_item.get('armazenamento'):

            item['preço'] = novo_item.get('preço')   

        cls.items[index] = item
        return item
