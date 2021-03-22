from baralho import embaralhar_21

def distribuir(baralho):
    jogador = list()
    for i in range(3):
        n = len(baralho)
        jogador.append(baralho[n-1])
        baralho.pop()
    return jogador

def compar(jogador):
    jogador.append(baralho_21[0])
    baralho_21.pop(0) 


baralho_21 = embaralhar_21()
jogador1 = distribuir(baralho_21)
computador = distribuir(baralho_21)

print(jogador1)
compar(jogador1)
print(jogador1)
