"""
Crie um programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
entrada = input("INSIRA M E F: ")
if entrada == "F":
    print("Feminino")
elif entrada == "M":
    print("Masculino")
else:
    print("Sexo Inválido.") 