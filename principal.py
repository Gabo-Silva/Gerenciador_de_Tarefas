# Importação dos métodos utilizados.
import texto
import uteis
# Criação do Menu
while True:
    texto.format('MENU PRINCIPAL')
    texto.opcoes('Adicionar tarefa', 'Listar Tarefas', 'Concluir Tarefas', 'Remover Tarefa', 'Sair')
    print('–' * 40)
    opcao = texto.leiaInt('Sua opção: ')
# Após o usúario decidir qual opção ele irá querer, o programa irá verificar qual opcão foi escolhida e chama a devida função, caso a opção escolhida não esteja entre as apresentadas, o programa irá subir uma mensagem de erro.
    if opcao == 1:
        texto.format('NOVA TAREFA')
        uteis.adicionarTarefa()
    elif opcao == 2:
        texto.format('TAREFAS CADASTRADAS')
        uteis.listarTarefas()
    elif opcao == 3:
        texto.format('QUAL TAREFA DESEJA CONCLUIR?')
        uteis.concluirTarefas()
    elif opcao == 4:
        texto.format('QUAL TAREFA DESEJA REMOVER?')
        uteis.removerTarefas()
    elif opcao == 5:
        break
    else:
        print('ERRO! Digite uma opção válida!')
texto.format('Saindo do sistema... Até logo!')