
def leiaInt(texto):
    while True:  

        try:
            numero = int(input(texto))

        except (ValueError, KeyboardInterrupt):

            print(f"ERRO! Foi encontrado um erro.")
            continue

        except Exception as erro:

            print(f"ERRO! Foi encontrado um erro em relação com {erro.__class__}.")
            continue
        else:
            return numero



class Usuario:

    def __init__(self, arquivo, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.arquivo = arquivo

    def cadastro(self):
        a = open(self.arquivo, 'at')
        a.write(f'{self.nome}:{self.idade}:{self.sexo}\n')
        a.close()

    def lerArquivo(self):
        a = open(self.arquivo, 'rt')
        for linha in a:
            dado = linha.split(':')
            dado[2] = dado[2].replace('\n', '')
            print(f'Nome - {dado[0]:<15} Idade - {dado[1]:>3} anos     Sexo - {dado[2]}')
        a.close()