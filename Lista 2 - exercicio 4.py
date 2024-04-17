#Exercicio 4 - Calculadora

print ("OPERAÇÃO MATEMÁTICA.")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":

    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
else:
    print("Operação inválida. Use +, -, *, ou /.")

if resultado is not None:
    print(f"Resultado da operação: {resultado:.2f}")