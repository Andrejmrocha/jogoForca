# nome = 'andre'
# name = list(nome)
# name[1] = 'j'
# nome = "".join(name)
# print(nome)
def posicao(palavra, letra):
    count = 0
    p = palavra
    posicao = []
    for i in p:
        if i == letra:
            posicao.append(count)
        count +=1
    return posicao

def lj(st, pos, subs):
    plv = list(st)
    tam = len(pos)
    for i in range(tam):
        plv[pos[i]] = subs
    st = "".join(plv)
    return st
