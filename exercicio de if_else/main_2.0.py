"""
Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
entrada = int(input("Digitar um valor: "))
if entrada < 0 :
    print("este numero e negativo.")
elif entrada > 0:
    print("este numero e positivo.")
else:
    print("numero que vocé insiro e zero.")