class ControleRemoto:

    def __init__ (self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
    
    def avancar_canal(self):
        print('canal avançado')
    
    def voltar_canal(self):
        print('voltar canal')
    
    def escolher_canal(self, canal):
        print('Alterar canal para o canal: {}'.format(canal))

controle_sala = ControleRemoto('sansung', 'quarto')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_quarto = ControleRemoto('lg', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)
controle_quarto.avancar_canal()
controle_quarto.escolher_canal(15)