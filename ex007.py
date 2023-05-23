#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#variaveis
nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

#Algoritmo
nome = input("\nDigite seu nome: ")
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) /2

print(f"{nome}, a sua média é: {media:,.2f}\n")