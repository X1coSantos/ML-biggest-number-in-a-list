# gerar uma lista, com varias listas de 3 elementos
# lista = []
# lista = [[1,2,3],[4,5,6]]

# importa a função randint para gerar os numeros inteiros aleatorios
from random import randint

def gerar_lista_numeros(elementos_totais, elementos_lista):
    """ Gera uma lista de listas(elementos_totais) de x(elementos_lista) em cada lista """

    # inicializa a lista final e o loop
    lista_x = []
    i = 0
    while i < elementos_totais:
        # inicializa uma lista temporaria para armazenar os elementos de cada lista individual
        ele_lista = []
        # loop para gerar numeros aleatorios e coloca-lo na lista temporaria
        for j in range(elementos_lista):
            # Gera o numero aleatorio
            numero_aleatorio = randint(1,1000)
            # Coloca o numero aleatorio na lista temporaria
            ele_lista.append(numero_aleatorio)

        # incrementa o i do loop
        i += 1

        # adiciona a lista temporaria na lista final
        lista_x.append(ele_lista)

        # printa a lista temporaria
        # print(ele_lista)

    # printa a lista final
    # print(lista_x)

    # retorna a lista final
    return lista_x


def gerar_lista_numeros_respostas(lista_numeros):
    """
        Gera as repostas á lista de numeros criadas, determina o maior e diz em qual posição se encontrava
        Caso na primeira: 'primeira', caso na seguda: 'segunda', caso na terceira: 'terceira'
    """
    # Incializa a lista_y
    lista_y = []

    # Recebe a lista dos numeros gerados, imprimir para debug
    # print(lista_numeros)

    # Loop que passa em cada lista da lista principal
    for lista_secundaria in lista_numeros:
        # printa a lista secundaria
        # print("Lista secundaria")
        # print(lista_secundaria)

        # determina o maximo da lista secundaria
        maximo = max(lista_secundaria)

        # Verifica qual o maior valor e vai mandar para uma lista o resultado
        if lista_secundaria[0] == maximo:
            resultado = 'primeiro'
        elif lista_secundaria[1] == maximo:
            resultado = 'segundo'
        elif lista_secundaria[2] == maximo:
            resultado = 'terceiro'
        else:
            resultado = ""

        # printa o resultado para debug
        # print(resultado)

        lista_y.append(resultado)

    # print(lista_numeros)
    # print(lista_y)
    return lista_y


