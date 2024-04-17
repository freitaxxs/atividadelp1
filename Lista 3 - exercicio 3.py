#Exercício 3 – Triangulo

def tipo_triangulo(lado1, lado2, lado3):
 if lado1 == lado2 == lado3:
 return "Equilátero"
 elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
 return "Isósceles"
 else:
 return "Escaleno"
def main():
 lado1 = float(input("Digite o primeiro lado do triângulo: "))
 lado2 = float(input("Digite o segundo lado do triângulo: "))
 lado3 = float(input("Digite o terceiro lado do triângulo: "))
 if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
 print("Os valores fornecidos podem formar um triângulo.")
 tipo = tipo_triangulo(lado1, lado2, lado3)
 print("Este triângulo é", tipo)
 else:
 print("Os valores fornecidos não podem formar um triângulo.")
if __name__ == "__main__":
 main()
