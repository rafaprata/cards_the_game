def distribuir(baralho):
    jogador = list()
    for i in range(3):
        n = len(baralho)
        jogador.append(baralho[n-1])
        baralho.pop()
    return jogador