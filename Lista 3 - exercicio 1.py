#Exercício 1 - Escreva um programa que leia três números e mostre o maior deles

def encontrar_maior(num1, num2, num3):
 if num1 >= num2 and num1 >= num3:
 return num1
 elif num2 >= num1 and num2 >= num3:
 return num2
 else:
 return num3
def main():
 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 num3 = float(input("Digite o terceiro número: "))
 maior_numero = encontrar_maior(num1, num2, num3)
 print("O maior número é:", maior_numero)
if __name__ == "__main__":
 main()