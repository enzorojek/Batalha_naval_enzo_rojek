from funcoes import posicao_valida,preenche_frota,posiciona_frota,faz_jogada,afundados,monta_tabuleiros

f={}

n=[['porta-aviões',4,1],['navio-tanque',3,2],['contratorpedeiro',2,3],['submarino',1,4]]

for tipo,t,q in n:
    p=0

    while p < q:
        print(f'Insira as informações referentes ao navio {tipo} que possui tamanho {t}')

        l = int(input('Linha: '))
        c = int(input('Coluna: '))

        if t > 1:
            o = int(input('[1] Vertical [2] Horizontal >'))

            if o == 1:
                o = 'vertical'
            elif o == 2:
                o = 'horizontal'

        if posicao_valida(f,l,c,o,t):
            f=preenche_frota(f,tipo,l,c,o,t)
            p += 1
        else:
            print('Esta posição não está válida!')

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tab1=posiciona_frota(f)
tab2=posiciona_frota(frota_oponente)

m=True

while m:
    print(monta_tabuleiros(tab1,tab2))

    r=True

    while r:
        l=int(input('Linha: '))

        while l<0 or l>9:
            print('Linha inválida!')
            l=int(input('Linha: '))

        c=int(input('Coluna: '))

        while c<0 or c>9:
            print('Coluna inválida!')
            c=int(input('Coluna: '))

        if tab2[l][c] in ['X', '-']:
            print(f'A posição linha {l} e coluna {c} já foi informada anteriormente!')
        else:
            r=False

    tab2=faz_jogada(tab2,l,c)

    if afundados(frota_oponente,tab2) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        m=False