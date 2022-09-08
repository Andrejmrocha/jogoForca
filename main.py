import random


from funcs import *
lista = ['sapataria', 'mochila', 'juventude']
l_p = []
escolher = random.choice(lista)

al = random.randint(0,8)
al1 = random.randint(0,8)
al2 = random.randint(0,8)
al3 = random.randint(0,8)
while al == al1:
    al1 = random.randint(0, 6)
novo = escolher.replace(escolher[al], "_")
novo = novo.replace(novo[al1], "_")
novo = novo.replace(novo[al2], "_")
novo = novo.replace(novo[al3], "_")

print(novo)

while "_" in novo:
    letra = input('informe uma letra ')
    l_p = posicao(escolher, letra)
    novo = lj(novo, l_p, letra)
    print(novo)
print('você conseguiu')







