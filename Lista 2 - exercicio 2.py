#Exercicio 2 - Vogal ou consoante

print ("VOGAL OU CONSOANTE!")

print ("PARA TER UMA RESPOSTA CORRETA, DIGITE A LETRA EM MAIUSCÚLO!!!")

letra = input('Digite uma letra em maiuscúlo: ')

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('É uma vogal.')
else:
    print('É uma consoante.')