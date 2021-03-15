import random
baralho = {'naipe':['PAUS', 'COPAS', 'ESPADA', 'OUROS'], 
    'numero':['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
}


embaralhado = []
carta = {}
n = len(embaralhado)
while len(embaralhado) <= 51:
    n = len(embaralhado)
    carta['naipe'] = baralho['naipe'][random.randint(0,3)]
    carta['numero'] = baralho['numero'][random.randint(0,12)]
    embaralhado.append(carta.copy())
    for i, v in enumerate(embaralhado):
            if i == len(embaralhado)-1:
                break
            elif v == carta:
                embaralhado.pop()
                break
print(embaralhado)