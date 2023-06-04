#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantidade de Km's percorridos: "))
dias = int(input("Dias alugados: "))
pagar = (dias*60)+(km * 0.15)

print(f"{dias} alugados com um total de {km}Km's percorridos resultam em um total de R${pagar} à pagar")