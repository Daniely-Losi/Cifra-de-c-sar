CARACTERES = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
texto = input("Digite a palavra: ")

modo = input('Digite 1 para encriptar  \n 2 para decriptar: ')

texto = texto.upper()

convertido = ' '

for caractere in texto:
    if caractere in CARACTERES:
        num = CARACTERES.find(caractere)
        if modo == '1':
            num = num + 3
        elif modo == '2':
            num = num - 3
        
    if num >= len(CARACTERES):
        num = num - len(CARACTERES)
        convertido = convertido + CARACTERES[num]
    elif num < 0:
        num = num + len(CARACTERES)
        convertido = convertido + CARACTERES[num]
    else:
	    convertido = convertido + CARACTERES[num]
	    
print(convertido)
