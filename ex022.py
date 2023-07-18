'''
Ex 22:
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e outro em minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
.strip serve para retirar os espaços indesejados antes e depois da frase.
'''

nome = str(input("Digite seu nome completo: ")).strip()

print(f"O seu nome com todas as letras maiusculas é: {nome.upper()}")
print(f"O seu nome com todas as letras minusculas é: {nome.lower()}")
print(f"O seu nome possui {len(nome)-nome.count(' ')} letras")
#print(f"O seu primeiro nome tem {len(nome.find(' '))} letras")
separado = nome.split()
print(f"O seu primeiro nome tem {len(separado[0])} letras")
