from modulo import *

arquivo = 'usuarios.txt'


nome = str(input('Nome : '))
idade =  leiaInt('Idade : ')
sexo = str(input('Sexo : '))

usuario = Usuario(arquivo, nome, idade, sexo)
usuario.cadastro()
usuario.lerArquivo()
