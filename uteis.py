# Esse método foi criado para as principais funções do projeto, adicionar tarefa, listar as tarefas, concluir tarefas e remover tarefas.

# Importação das funções utilizadas.
import texto

def adicionarTarefa():
# Nessa função ele irá adicionar uma tarefa ao txt, um adendo que vale ressaltar é que caso o arquivo txt não tenha sido criado a função irá criá-lo automáticamente.
    arquivo = open('tarefas.txt', 'a+')
    tarefa = str(input('Cadastrar Tarefa: '))
    texto = f'{tarefa}'
    arquivo.write(f'[] {texto}\n')
    arquivo.close()
    print(f'Tarefa "{texto}" cadastrada com sucesso!')
    
       
def listarTarefas():
# Nessa função ele irá primeiramente tentar abrir o arquivo, que caso não tenha sido criado, irá apresentar uma mensagem de "erro" que também irá aparecer se não tiver nenhuma tarefa cadastrada.
    try:
        arquivo = open('tarefas.txt', 'r+')
    except:
        print('Nenhuma tarefa cadastrada!')
    else:
        linhas = arquivo.readlines()
        if len(linhas) == 0:
            print('Nenhuma tarefa cadastrada!')
# Caso o arquivo tenha sido criado e tenha atividades cadastradas, tudo será apresentado corretamente.
        for a in linhas:
            print(f'{a}', end='')
        arquivo.close()
        
        
def concluirTarefas():
# Nessa função ele irá primeiramente tentar abrir o arquivo, que caso não tenha sido criado, irá apresentar uma mensagem de "erro" que também irá aparecer se não tiver nenhuma tarefa cadastrada.
    try:
        arquivo = open('tarefas.txt', 'r+')
    except:
        print('Nenhuma tarefa cadastrada!')
    else:
        linhas = arquivo.readlines()
        if len(linhas) == 0:
            return print('Nenhuma tarefa cadastrada!')
# Aqui ele irá verificar se existe alguma tarefa para se concluida, caso não ele irá soltar uma mensagem que todas as tarefas já foram feitas.
        cont = 0
        for linha in linhas:
            if '[]' in linha:
                cont += 1
        if cont == 0:
            return print('Todas as tarefas foram concluídas!')
        while True:
                res = 0
                parar = ''
# Ele irá primeiro apresentar todas as atividades, as feitas e as não feitas.
                for i, l in enumerate(linhas):
                    print(f'{i + 1} – {l}', end='')
                while res <= 0 or res > len(linhas):
                    print('–' * 40)
# Depois disso irá perguntar qual tarefa o usuário deseja concluir.
                    res = texto.leiaInt('Qual atividade deseja concluir: ')
# Aqui ocorre uma verificação de erro, que caso o usuário digite um número igual ou menor que zero ou um número maior que a quantidade de tarefas, irá aparecer uma mensagem de erro.
                    if res <= 0 or res > len(linhas):
                        print('ERRO! Digite uma opção válida!')
#Caso o usuário digite um número que tenha na lista de tarefas pode ocorre duas coisas. 
                    
#Primeiro: se a tarefa já tiver sido concluída, irá aparece uma mensagem de que ela já foi concluida. 

#Segundo: se a tarefa não tiver sido concluída ainda, o programa irá soltar uma mensagem de conclusão da tarefa e a caixa vazia irá ganhar um "x" representando que aquela tarefa foi concluída com sucesso.
                    else:
                        for i, l in enumerate(linhas):
                            if res - 1 == i:
                                if '[x]' in l:
                                    print('Essa tarefa já foi concluída!')
                                elif '[]' in l:
                                   linhas[i] = l.replace('[]', '[x]')
                                   print(f'Tarefa "{l.replace('[]', '').strip()}" foi concluída com sucesso!')
    # Nessa parte, ocorre o salvamento das informações.
                                   arquivo = open('tarefas.txt', 'w+')
                                   arquivo.writelines(linhas)
                                   arquivo.close()
# Mais uma ele verifica se tem uma tarefa para ser concluida, caso não ele encerrar o uso dessa função.
                cont = 0
                for linha in linhas:
                            if '[]' in linha:
                                cont += 1
                if cont == 0:
                    print('–' * 40)
                    return print('Todas as tarefas foram concluídas!')
# Aqui ele perguntar se o usuário que continuar a concluir atividades, se sim a função continuar, se não ela termina.
                while parar not in ('S', 'N'):
                           print('–' * 40)
                           parar = str(input('Quer continuar [S/N]? ').strip().upper())
# Uma outra verificação de possíveis erros, caso usuário digite uma outra coisa sem ser "S" ou "N", irá aparecer uma mensagem de erro e o loop irá continuar até que "S" ou "N" sejam digitados.
                           if parar not in ('S', 'N'):
                               print('ERRO! Digite uma opção válida!')
                if parar in 'N':
                     break
                elif parar in 'S':
                    print('–' * 40)
                
                
def removerTarefas():
# Importação das funções utilizadas.
    import texto
# Nessa função ele irá primeiramente tentar abrir o arquivo, que caso não tenha sido criado, irá apresentar uma mensagem de "erro" que também irá aparecer se não tiver nenhuma tarefa cadastrada.
    try:
        arquivo = open('tarefas.txt', 'r+')
    except:
        print('Nenhuma tarefa cadastrada!')
    else:    
        linhas = arquivo.readlines()
        if len(linhas) == 0:
            return print('Nenhuma tarefa cadastrada!')
        while True:
            res = 0
            parar = ''
            for i, linha in enumerate(linhas):
# Ele irá primeiro apresentar todas as atividades.
                print(f'{i + 1} – {linha}', end='')
            while res <= 0 or res > len(linhas):
                print('–' * 40)
# Depois disso irá perguntar qual tarefa o usuário deseja excluir.
                res = texto.leiaInt('Qual tarefa deseja excluir? ')
# Aqui ocorre uma verificação de erro, que caso o usuário digite um número igual ou menor que zero ou um número maior que a quantidade de tarefas, irá aparecer uma mensagem de erro.
                if res <= 0 or res > len(linhas):
                    print('ERRO! Digite um valor válido!')
# Caso o número seja válido, a atividade em questão será excluida e uma mensagem referente a remoção da atividade será mostrada.
            else:
                print(f'Tarefa "{linhas[res - 1].replace('[]', '').replace('[x]', '').strip()}" foi removida com sucesso.')
                del linhas[res - 1]
# Nessa parte, ocorre o salvamento das informações.
                arquivo = open('tarefas.txt', 'w+')
                arquivo.writelines(linhas)
                arquivo.close()
# Ele verifica se ainda há mensagens no arquivo txt, se não, a função termina.
                if len(linhas) == 0:
                    print('–' * 40)
                    return print('Todas as tarefas foram excluídas!')
# Aqui ele perguntar se o usuário que continuar a excluir atividades, se sim a função continuar, se não ela termina.
                while parar not in ('S', 'N'):
                    print('–' * 40)
                    parar = str(input('Quer continuar [S/N]? ').strip().upper())
# Uma outra verificação de possíveis erros, caso usuário digite uma outra coisa sem ser "S" ou "N", irá aparecer uma mensagem de erro e o loop irá continuar até que "S" ou "N" sejam digitados.
                    if parar not in ('S', 'N'):
                        print('ERRO! Digite uma opção válida!')
                if parar in 'S':
                    print('–' * 40)
                if parar in 'N':
                    break
            