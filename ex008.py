#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

#Variaveis
metros = 0.0
centimetros = 0.0
milimetros = 0.0

#Algoritmo
metros = float(input("\nDigite o valor em metros a ser convertido: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros} metros em centímetros é: {centimetros}")
print(f"{metros} metros em milímetros é: {milimetros}\n")
