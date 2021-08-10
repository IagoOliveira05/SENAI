from lib.arquivo import *
from time import sleep

arquivo = 'teste.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(["Ver produtos", "Cadastrar produto", "Excluir produto", "Sair do sistema"])

    if resposta == 1:
        # Mostrar os produtos em estoque, seus respectivos preços e a quantidade
        lerArquivo(arquivo)
        sleep(2)
    elif resposta == 2:
        # Cadastrar novo produto
        cabeçalho("Novo produto")
        nome = str(input("Nome do produto: "))
        preco = leiaFloat("Preço: ")
        quantidade = leiaInt(f"Quantidade de {nome}: ")
        cadastrar(arquivo, nome, preco, quantidade)
    '''elif resposta == 3:
        # Excluir produto

    elif resposta == 4:
        # Sair do sistema

    else:
        print("Digite uma opção válida!")
'''