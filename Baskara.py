import math

print("Bem vindo ao programa de calculo de Baskara")
print("Exemplos \n A = 10 \n B = 20 \n C = 10 \n Reposta:\n X' = -1.0 \n X'' = -1.0")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

x = (b ** 2) - (4 * a * c)

if x < 0:
    print("Raiz negativa nao pode ser extraida.")
    exit()

else:
    x = math.sqrt(x)
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)
print("\n\nX' = %s \nX'' = " % x1, x2)