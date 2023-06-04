#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num = float(input("Informe um valor real: "))
print(f"A parte inteira do número {num} vale {math.trunc(num)}")
