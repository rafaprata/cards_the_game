from random import randint

base = {'naipe':['PAUS', 'COPAS', 'ESPADA', 'OUROS'], 
    'numero':['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']} #Colocar o 8, 9, 10 se for usar o baralho inteiro

def embaralhar():
    baral = list()
    carta = dict()
    n = len(baral)
    while len(baral) <= 51: #Se for usar o baralho inteiro <= 51
        n = len(baral)
        carta['naipe'] = base['naipe'][randint(0,3)]
        carta['numero'] = base['numero'][randint(0,12)] #Se for usar o baralho inteiro, até 12
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
