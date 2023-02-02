
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

TextoFinal =' '

print("Digite um opção")
print("1- Criptografar")
print("2- Descriptografar")

opcao = int(input ("Sua escolha:"))
texto = ' '.join(str(input("Digite o Texto")).upper().split())
key = str(input("Digite a chave: ")).upper()
keyFinal = " "

if(len(key)>len(texto)):
    print("A chave é maior que a frase")
else:
        i = int (0)
        while(len(keyFinal)<len(texto)):
            keyFinal += key[i]
            i +=1
            if(i==len(key)):
                i =  0
        for i in range(len(texto)):
            if(texto[i]) != ' ':
                posicao_letra_frase = int(alfabeto.index(texto[i]))
                posicao_letra_chave = int(alfabeto.index(keyFinal[i]))
                if(opcao == 1):
                    TextoFinal += str(alfabeto[(posicao_letra_frase+posicao_letra_chave) % len(alfabeto)])
                else:
                        TextoFinal += str(alfabeto[(posicao_letra_frase+posicao_letra_chave) % len(alfabeto)])
            else:
                    TextoFinal += ' '
                    print("Frase final: {}".format(TextoFinal))
                    input()
                    
pass





