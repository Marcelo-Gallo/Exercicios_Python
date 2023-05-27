#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#variaveis
desconto = 0.0
preco = 0.0
npreco = 0.0

#algoritmo

preco = float(input("Informe qual o preço do produto: R$"))
desconto = float(input("Informe qual o desconto que deseja aplicar em %: "))
desconto = (desconto/100)
npreco = preco - (preco*desconto)
print(f"O novo preço do produto com o desconto aplicado é R${npreco}")