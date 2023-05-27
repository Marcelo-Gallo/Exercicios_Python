#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

#variaveis
largura = 0.0
altura = 0.0
area = 0.0
pintura = 0.0
rendimento = 0.0

#algoritmo

largura = float(input("Informe a largura da parede em metros: "))
altura = float(input("Agora, informe a altura da parede em metros: "))

area = largura*altura

print(f"Certo, você informou que a parede possui {largura}mts de largura e {altura}mts de altura, totalizando {area}mts² de area. ")

rendimento = float(input("Quantos metros quadrados cada litro de tinta cobre? Rendimento = "))

pintura = area/rendimento

print(f"Você irá usar {pintura}lts de tinta para pintar esta parede.")
