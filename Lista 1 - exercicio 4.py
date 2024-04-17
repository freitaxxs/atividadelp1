#Exercicio 4 - Mês correspondente

print ("MÊS CORRESPONDENTE.")

numero_mes = int(input("Digite um número inteiro entre 1 e 12: "))

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

if 1 <= numero_mes <= 12:
    nome_mes = meses[numero_mes - 1]
    print(f"O mês correspondente ao número {numero_mes} que foi digitado é {nome_mes}.")
else:
    print("Número inválido, tente novamente!")