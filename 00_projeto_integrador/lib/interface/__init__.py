
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Por favor digite um número inteiro válido")
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("Por favor digite um número inteiro válido")
            continue
        else:
            return n

def linha(tam=62):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(62))
    print(linha())

def menu(lista):
    cabeçalho("Menu Principal")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc