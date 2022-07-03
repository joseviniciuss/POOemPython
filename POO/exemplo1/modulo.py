from traceback import print_tb


class Carro():

    def __init__(self, marca, modelo, ano, problema):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.problema = problema

    def mostrarCaracteristicas(self):
        linha()
        print(f'Marca - {self.marca}     Modelo - {self.modelo}      Ano - {self.ano}')

    def mostrarProblema(self):
        print(f"O problema é '{self.problema}'.")
        linha()

    def tempoDeUso(self):
        uso = 2022 - int(self.ano)
        print(f'O tempo de uso do carro é {uso} anos.')
        

def linha(numero=50):
    print('-'*50)
