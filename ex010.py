#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dolares ela pode comprar.
#considere US$1,00 = R$3,27

#variaveis
carteira = 0.0
dolar = 0.0
comprado = 0.0

#algoritmo
dolar = float(input("\nValor em reais do dolar hoje: "))
carteira = float(input("Reais em mãos: "))

comprado = carteira/dolar

print(f"Com R${carteira:,.2f} você pode comprar US${comprado:,.2f}\n")
