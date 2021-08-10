from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabeçalho("PRODUTOS CADASTRADOS")
        print(f"{'Produto':>10}{'Preço':>15}{'Quantidade':>17}")
        for linha in a:
            dado = linha.split(";")
            dado[2] = dado[2].replace("\n", "")
            print(f"{dado[0]:<20}{dado[1]:<15}{dado[2]:<15}")
    finally:
        a.close()

def cadastrar(arquivo, nome="desconhecido", preco=0.00, quantidade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            a.write(f'{nome};{preco};{quantidade}\n')
        except:
            print("Houve um erro ao escrever os dados!")
        else:
            print(f"Novo registro de produto adicionado")
            a.close()