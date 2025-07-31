# Método criado para deixar o texto padronizado.
def format(msg):
# Função feita para deixar o texto centralizado, e deixá-lo com uma quantidade exata de linhas para que ele fique elegante e padronizado.
    print('–' * 40)
    print(msg.center(40))
    print('–' * 40)


def opcoes(* escolhas):
# Função para deixar o menu de uma maneira mais automática.
    for i, e in enumerate(escolhas):
        print(f'{i+1} – {e}')


def leiaInt(msg):
# Função que ler um número inteiro, e verifica se ele é realmente é um número inteiro. Caso seja ele retorna o número, caso não, retorna 0, que normalmente significa falha no programa.
    while True:
        try:
            escolha = int(input(msg))
        except:
            return 0
        else:
            return escolha
 
