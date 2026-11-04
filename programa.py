from funcoes import posicao_valida, preenche_frota

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

print(f)