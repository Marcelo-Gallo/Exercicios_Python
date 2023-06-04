#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = str(input("Nome 1: "))
a2 = str(input("Nome 2: "))
a3 = str(input("Nome 3: "))
a4 = str(input("Nome 4: "))

lista = [a1,a2,a3,a4]
random.shuffle(lista)

print("A ordem de apresentação será: ")
print(lista)