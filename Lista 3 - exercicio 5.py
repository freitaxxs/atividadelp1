#Exercicio 5 - celsius para fahrenheit

def celsius_para_fahrenheit(celsius):
 fahrenheit = celsius * (9 / 5) + 32
 return fahrenheit
def main():
 celsius = float(input("Digite a temperatura em graus Celsius: "))
 fahrenheit = celsius_para_fahrenheit(celsius)
 print("A temperatura em Fahrenheit é:", fahrenheit)
if __name__ == "__main__":
 main()