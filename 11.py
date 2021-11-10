"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma
lista de palavras lidas de um arquivo texto e escolherá uma
aleatoriamente. O jogador poderá errar 6 vezes antes de ser
enforcado.

    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!

    Digite uma letra: O
    A palavra é: _ _ _ _ O

    Digite uma letra: E
    A palavra é: _ E _ _ O

    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!
"""

encontradas = []
secreto = []

palavra_secreta = 'PYTHON'

for p in palavra_secreta:
    secreto.append("_")

cont = 0
print("------------------------")
print("      JOGO DA FORCA     ")
print("------------------------")
print('A palavra é: ', end='')
print(' '.join(secreto))
print()
while True:
    letra = input("Digite uma letra: ").upper()

    for pos, char in enumerate(palavra_secreta):
        if char == letra:
            encontradas.append(pos)
            secreto.pop(pos)
            secreto.insert(pos, palavra_secreta[pos])

    if letra not in palavra_secreta:
        cont += 1
        print(f"-> Você errou pela {cont}ª vez. Tente novamente!")

    print('A palavra é: ', end='')
    print(' '.join(secreto))

    if len(palavra_secreta) == len(encontradas):
        print("Você VENCEU!!! Parabéns !!!")
        break
    elif cont == 7:
        print("Você PERDEU!!!")
        break
    print()

