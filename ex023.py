'''
Ex 23:
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
import math

numero = int(input("Digite um número: "))
print(f"Analisando o número {numero}")
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"Unidades: {u}")
print(f"Dezenas: {d}")
print(f"Centenas: {c}")
print(f"Milhares: {m}")