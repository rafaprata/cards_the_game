from random import randint

base = {'naipe':['PAUS', 'COPAS', 'ESPADA', 'OUROS'], 
    'numero':['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']} #Colocar o 8, 9, 10 se for usar o baralho inteiro

def embaralhar_21():
    baral = list()
    carta = dict()
    n = len(baral)
    while len(baral) <= 51:
        n = len(baral)
        carta['naipe'] = base['naipe'][randint(0,3)]
        carta['numero'] = base['numero'][randint(0,12)]
        if carta['numero'] in 'JQK':
            carta['valor'] = 10
        elif carta['numero'] in 'A':
            carta['valor'] = 1
        else:
            carta['valor'] = int(carta['numero'])

        baral.append(carta.copy())
        for i, v in enumerate(baral):
                if i == len(baral)-1:
                    break
                elif v == carta:
                    baral.pop()
                    break
    return baral

def embaralhar_truco():
    baralho = list()
    carta = dict()
    n = len(baralho)
    for i in range(3):
        base['numero'].pop(7)
    while len(baralho) <= 39:
        n = len(baralho)
        carta['naipe'] = base['naipe'][randint(0,3)]
        carta['numero'] = base['numero'][randint(0,9)]
        if carta['numero'] in 'Q':
            carta['valor'] = 8
        elif carta['numero'] in 'A':
            carta['valor'] = 1
        elif carta['numero'] in 'J':
            carta['valor'] = 9
        elif carta['numero'] in 'K':
            carta['valor'] = 10
        else:
            carta['valor'] = int(carta['numero'])

        baralho.append(carta.copy())
        for i, v in enumerate(baralho):
                if i == len(baralho)-1:
                    break
                elif v == carta:
                    baralho.pop()
                    break
    return baralho