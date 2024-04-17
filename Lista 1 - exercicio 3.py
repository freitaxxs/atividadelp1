#Exercicio 3 - Raíz quadrada

print("CALCULADORA DE RAIZ QUADRADA.")

import math

def calcular_raiz_quadrada():
    try:
        numero = float(input("Digite um número: "))
        if numero >= 0:
            raiz = math.sqrt(numero)
            print(f"A raiz quadrada de {numero:.2f} é {raiz:.2f}.")
        else:
            print("Número inválido. Digite um número positivo.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

calcular_raiz_quadrada()