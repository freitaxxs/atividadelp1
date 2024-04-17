#Exercicio 2 - Calcular o valor do lanche

print ("VALOR A SER PAGO:")

cardapio = {
    100: {"descricao": "Cachorro-quente", "preco": 1.20},
    101: {"descricao": "Bauru simples", "preco": 1.30},
    102: {"descricao": "Bauru com ovo", "preco": 1.50},
    103: {"descricao": "Hamburguer", "preco": 1.20},
    104: {"descricao": "Cheesburguer", "preco": 1.70},
    105: {"descricao": "Suco", "preco": 2.20},
    106: {"descricao": "Refrigerante", "preco": 1.00},
}

def calcular_valor_lanche(codigo, quantidade):
    if codigo in cardapio:
        preco_unitario = cardapio[codigo]["preco"]
        valor_total = preco_unitario * quantidade
        return valor_total
    else:
        return "Código de produto inválido."

codigo_produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

valor_total_lanche = calcular_valor_lanche(codigo_produto, quantidade)

if isinstance(valor_total_lanche, float):
    print(f"Valor total a ser pago: R$ {valor_total_lanche:.2f}")
else:
    print(valor_total_lanche)