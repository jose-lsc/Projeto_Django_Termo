import random


palavras = [
    "algoz",
    "arroz",
    "fazer",
    "girar",
    "facas",
    "nobre",
    "afeto",
    "sobre",
    "inato",
    "carne",
    "honra",
    "tempo",
    "saber",
    "entre",
    "censo"
]

palavra = random.choice(palavras).upper()
conjuntoDeLetras = list(palavra)
resposta = ''
palavraTermo= ['','','','','']
vidas = 6

print('\n\n', (palavra).upper())
print(conjuntoDeLetras)


print("\n\n\033[1;34mTERMO\033[m\n")
# for letras in palavra:
#         print("_ ", end='')

while resposta != palavra:
    
    resposta = input("\nDigite a Palavra: ").upper()
    while len(resposta) > 5 or len(resposta) < 5:
        print("\nDigite Apenas Palavras De Cinco Caracteres: ", end='')
        resposta = input("").upper()


    if resposta == palavra:
        print("\n","\033[0;32mACERTOU!\033[m\n")
    else:
        letras_corretas = []
        vidas -= 1

        if vidas == 0:
            print("\n\033[0;31mVOCE PERDEU HAHA\033[m\n")
            print("\033[0;32mPALAVRA CORRETA: ",palavra, "\n\033[m")
            break

        for contador, letras_certas in enumerate(list(resposta)):
            ##print(letras_certas)
            
            if letras_certas == conjuntoDeLetras[contador]:
                letras_corretas.append(letras_certas)

            else:
                letras_corretas.append('_ ')

        ##print(letras_corretas)

        for i,acertos in enumerate(letras_corretas):
            if acertos != '_ ':
                palavraTermo[i] = acertos
        print(palavraTermo)
        print("vidas restantes: ", vidas)
