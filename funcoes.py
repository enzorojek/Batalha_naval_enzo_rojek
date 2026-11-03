def define_posicoes(l,c,o,t):
    p=[]

    for i in range(t):
        if o=='vertical':
            p.append([l+i,c])
        elif o=='horizontal':
            p.append([l,c+i])

    return p

def preenche_frota(f,n,l,c,o,t):
    p=define_posicoes(l,c,o,t)

    if n not in f:
        f[n]=[]

    f[n].append(p)

    return f

def faz_jogada(tabuleiro,l,c):
    if tabuleiro[l][c] == 1:
        tabuleiro[l][c] = 'X'
    elif tabuleiro[l][c] == 0:
        tabuleiro[l][c] = '-'

    return tabuleiro

def posiciona_frota(f):
    tab=[]

    for i in range(10):
        tab.append([0] * 10)

    for n in f:
        for j in f[n]:
            for p in j:
                l=p[0]
                c=p[1]
                tab[l][c] = 1

    return tab