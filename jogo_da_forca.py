import random
tentativa = 0
acerto = 0
u = 0
j = ''
k = ''
#palavraMisteriosa = []

#Lista de palavras para usar na forca
palavra = ['acerola']

#Sorteando uma palavra para usar no jogo da forca
numero = random.randint(0,len(palavra)-1)
palavraSorteada = list(palavra[numero])


#Mensagem de boas vindas do jogo
nome = input("Digite o nome do jogador: ")

print("")
print("***__________JOGO DA FORCA__________***")
print("")
print("    *** Seja Bem-Vindo", nome,"***    ")

print("")
print("")
#print("Instruções:")


for x in range(0,len(palavraSorteada)):
    j = j + '_'

print("A palavra tem", len(palavraSorteada),"letras!")
print("")
print(j)
k = j


while (tentativa < 6) and (acerto < len(palavraSorteada)):
    print("")
    letra = input("Digite uma letra: ")
    print("\n"*80)
    for elemento in palavraSorteada:
        if letra == elemento:
            indice = palavraSorteada.index(letra)
            palavraMisteriosa = list(j)
            palavraMisteriosa.insert(indice, letra)
            palavraMisteriosa.pop(indice+1)
            acerto = acerto + 1
            j=''
            for y in palavraMisteriosa:
                j = j + y
    
    if k == j:
        tentativa = tentativa + 1
        print("")
        print("A palavra misteriosa não possui a letra: ", letra)
        print("")
        print(j)
        print("")
    else:
        print("")
        print("Parabéns, acertou a letra!")
        print("")
        print(j)
        print("")
        k = j

    print("Acerto:", acerto)
    print("Erro:", tentativa)

if (tentativa == 6):
    print("Você perdeu!")
elif (acerto == len(palavraMisteriosa)):
    print("Parabéns", nome, "!")
    print("***Você venceu***")


