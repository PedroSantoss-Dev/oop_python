class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf 

    def correr(self):
        print('Estou correndo')
    
    def beber(self, bebida):
        if bebida == 'Cerveja':
            self.__apresentar_documento()
            if self.idade < 18:
                return print('Você não pode comprar bebidas alcolicas')
        print('bebendo ...')
    def __apresentar_documento(self):
        print(self.__cpf)
    
Ronaldo = Pessoa('Ronaldo', 15, '452222222')
Ronaldo.correr()
Ronaldo.beber('Cerveja')

Janaina = Pessoa('Janaina', 30 , '12233355549')
Janaina.beber('Cerveja')

