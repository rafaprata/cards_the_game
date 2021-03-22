from random import randint

base = {'naipe':['PAUS', 'COPAS', 'ESPADA', 'OUROS'], 
    'numero':['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']} #Colocar o 8, 9, 10 se for usar o baralho inteiro

def embaralhar():
    baral = list()
    carta = dict()
    n = len(baral)
    while len(baral) <= 39: #Se for usar o baralho inteiro <= 51
        n = len(baral)
        carta['naipe'] = base['naipe'][randint(0,3)]
        carta['numero'] = base['numero'][randint(0,9)] #Se for usar o baralho inteiro, até 12
        baral.append(carta.copy())
        for i, v in enumerate(baral):
                if i == len(baral)-1:
                    break
                elif v == carta:
                    baral.pop()
                    break
    return baral

baralho = embaralhar()
jogador1 = distribuir(baralho)
computador = distribuir(baralho)
coringa = coringa(baralho)
jogar(jogador1)

print(f'Jogador 1 - {jogador1}')
print(f'Computador - {computador}')
print(coringa)