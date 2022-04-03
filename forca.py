import random

def abertura():
    print("*********************************")
    print("   Bem vindo ao jogo da forca!   ")
    print("*********************************")

def arquivo_de_exportação():
    arquivo = open("../palavras.txt", "r")
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()
    palavra_escolhida = random.randrange(0, len(palavras))
    palavra_secreta = palavras[palavra_escolhida].upper()
    return palavra_secreta


abertura()
palavra_secreta = arquivo_de_exportação()

letras_acertadas = ["_" for linha in palavra_secreta]

forca = False
acerto = False
erros = 0
tentativas = 6
print(letras_acertadas)

while(not forca and not acerto):

    chute = input("Digite a letra: ")
    chute = chute.strip().upper()

    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index = index + 1
    else:
        erros = erros + 1
        tentativas = tentativas - 1
        print("Você tem ",tentativas," tentativas")

    forca = erros == 7
    acerto = "_" not in letras_acertadas
    print(letras_acertadas)


    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(acerto):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
else:
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

print("Fim de jogo!")

