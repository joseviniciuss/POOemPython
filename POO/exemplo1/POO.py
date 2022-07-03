from modulo import *

linha()
marca = str(input('Marca : '))
modelo = str(input('Modelo : '))
ano = int(input('Ano : '))
problema = str(input('Qual o problema? '))


carro = Carro( marca, modelo, ano, problema)
carro.mostrarCaracteristicas()
carro.tempoDeUso()
carro.mostrarProblema()
