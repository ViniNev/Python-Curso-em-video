class Carro:
    def __init__(self, marca, cor, ano):
        self.marca = marca
        self.cor = cor
        self.ano = ano


    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def ExibirInformacoesDesteCarro(self):
        print(self.marca, self.cor, self.ano)


carro1 = Carro('Audi A3,', 'Vermelho,', '2022')
carro1.Ligar()
carro1.Desligar()
carro1.ExibirInformacoesDesteCarro()
