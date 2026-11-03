def define_posicoes(l,c,o,t):
    p=[]

    for i in range(t):
        if o=='vertical':
            p.append([l+i,c])
        elif o=='horizontal':
            p.append([l,c+i])

    return p