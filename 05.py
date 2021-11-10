"""
Nome na vertical em escada invertida. Altere o programa anterior
de modo que a escada seja invertida.

    FULANO
    FULAN
    FULA
    FUL
    FU
    F
"""
nome = 'FULANO'
cont = 0
for n in nome:
    if cont == 0:
        print(nome)
        cont -= 1
    else:
        print(nome[:cont])
        cont -= 1
