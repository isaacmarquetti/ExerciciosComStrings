"""
Nome na vertical em escada. Modifique o programa anterior de forma
a mostrar o nome em formato de escada.

    F
    FU
    FUL
    FULA
    FULAN
    FULANO
"""
nome = 'FULANO'
cont = 0
for n in nome:
    cont += 1
    print(nome[:cont])

