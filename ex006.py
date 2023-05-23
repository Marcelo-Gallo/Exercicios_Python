#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#variaveis
num = 0.0
dobro = 0.0
triplo = 0.0
raiz = 0.0

#Algoritmo
num = float(input("Digite um número qualquer: "))

dobro = num * 2
triplo = num * 3
raiz = num**(1/2)

print(f"O dobro do número escolhido é: {dobro}")
print(f"O triplo do número escolhido é: {triplo}")
print(f"A raiz do número escolhido é: {raiz}")