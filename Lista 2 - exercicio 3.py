#Exercicio 3 - Dias existentes em um mês

print ("QUANTOS DIAS TEM O MÊS.")

def dias_mes(mes, ano):

    if mes == 2:

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return 29
        else:
            return 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

mes_digitado = int(input("Digite o número do mês desejado de 1 a 12: "))
ano_digitado = int(input("Digite o ano desejado: "))
print(f"O mês {mes_digitado} do ano {ano_digitado} tem {dias_mes(mes_digitado, ano_digitado)} dias.")