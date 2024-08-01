"""
1.Faça um programa que peça dois números e imprima o maior deles.
"""
num_1 = int(input("Digite um numero: "))
num_2 = int(input('Digite outros numero: '))
if num_1 > num_2:
    print(f"Numero {num_1} e que ", end="\n"
          f"Menor que {num_2}")
elif num_1 == num_2:
    print("são iguias.")
else:
    print(f"Numero {num_2} e maior ", end="\n"
          f"menor que {num_1}")
