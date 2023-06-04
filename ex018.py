#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input("Informe o angulo que deseja detalhar: "))

seno = math.sin(math.radians(angulo))
#seno recebe o valor de angulo convertido para radianos e logo apos convertido para seno.
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"Para o angulo {angulo}°, o seno vale {seno:,.2f}, o cosseno vale {cosseno:,.2f}, e a tangente vale {tangente:,.2f}")