#Exercicio 1 - Olimpíada Brasileira de Informática

print ("NOTAS DA PROVA")

print ("Digite uma nota de 0 a 100:")

nota = int(input())

if (0 <= nota < 1):
  print('E')
elif (1 <= nota <= 35):
  print('D')
elif (36 <= nota <= 60):
  print('C')
elif (61 <= nota <= 85):
  print('B')
else:
  print('A')