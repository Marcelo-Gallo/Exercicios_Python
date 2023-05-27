#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#variaveis: 
sal = 0.0
nsal = 0.0
aumento = 0.0

sal = float(input("Informe o salário do funcionário: R$"))
aumento = float(input("Informe o percentual de aumento do salário: "))
aumento = aumento/100
nsal = sal + (sal*aumento)
print(f"O salário com o aumento é: R${nsal}")