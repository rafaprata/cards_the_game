def distribuir(baralho):
    jogador = list()
    for i in range(3):
        n = len(baralho)
        jogador.append(baralho[n-1])
        baralho.pop()
    return jogador

def coringa(baralho):
    coringa = baralho[len(baralho)-1]
    baralho.pop()
    return coringa

def jogar(jogador):
    n = 1
    print(coringa)
    if n == 1:
        pos = 1
        for i in jogador:
            print(f'[{pos}]{i["numero"]}, {i["naipe"]}')
            pos += 1
        carta = int(input('Qual carta vai jogar: '))