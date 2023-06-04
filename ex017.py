#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt

co = float(input("Informe o valor do cateto oposto: "))
ca = float(input("Informe o valor do cateto adjacente: "))
h = ((ca**2) + (co**2))

print(f"O valor da hipotenusa é: {sqrt(h)}")