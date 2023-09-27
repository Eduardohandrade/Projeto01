
import json
banco_dados = {}
opcao = 1
# preciso carregar o que estiver no arquivo
try:
    with open("banco_dados/estoque.json", 'r') as arquivo:
        banco_dados = json.load(arquivo)
except:
    print('o arquivo nao existe')

while opcao != 4:
    print("="*10)
    print("1- Adicionar")
    print("2- Consultar por codigo")
    print("3- Consultar todos")
    print("4- Alterar o preço de um produto")
    print("5- Aplicar acréscimo ou desconto em todos os produtos")
    print("6- Excluir um registro de produto")
    print("7- Sair")
    opcao = int(input("Escolha a opcao: "))
    if opcao==1:
        print('-'*10)
        print("CADASTRO")
        codigo = input('Digite codigo: ')
        nome = input('Digite nome do produto: ')
        preco = float(input('Digite o preco do kg/unidade: '))
        banco_dados[codigo] = {"nome": nome, "preco": preco}
        # adicionar no arquivo
        with open("banco_dados/estoque.json", "w") as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
    elif opcao == 2:
        print('-'*10)
        print("CONSULTAR POR CODIGO")
        produto = banco_dados[codigo]
        print(produto['nome'])
        print(banco_dados[codigo]['nome'])
    elif opcao == 3:
        print('-'*10)
        print("CONSULTAR TODOS")
        print(banco_dados)
    elif opcao == 4:
        print('-' * 10)
        print("ALTERAR O PREÇO DE UM PRODUTO")
        codigo = input('Digite o código do produto que deseja alterar: ')
        produto= banco_dados[codigo] 
        if produto:
            novo_preco = float(input('Digite o novo preço do kg/unidade: '))
            produto = novo_preco
            print('Preço do produto atualizado com sucesso.')
        else:
            print("Produto não encontrado.")

    elif opcao == 5:
        print('-' * 10)
        taxa = float(input('Digite a taxa de acrescimo ou desconto(-): '))
        for codigo in banco_dados:
            produto = banco_dados[codigo]
            preco = produto['preco']
            novo_preco = preco*(1+taxa/100)
            # atualizar novo preço
            produto['preco'] = novo_preco

    elif opcao == 6:
        print('-' * 10)
        print("EXCLUIR UM REGISTRO DE PRODUTO")
        codigo = input('Digite o código do produto que deseja excluir: ')
        produto = banco_dados[codigo]
        if produto:
            del banco_dados[codigo]
            print('Produto excluído com sucesso.')
        else:
            print("Produto não encontrado.")

    elif opcao == 7:
        print('-' * 10)
        print('SAINDO')
        with open("banco_dados/estoque.json", "w") as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
        break
    else:
        print('-'*10)
        print('opcao invalida')