import sympy as sp
x = sp.Symbol('x')

texto = input("Digite: ")
function = texto
var = input("Digite2: ")
texto2 = int((function.replace('x', var)))
print(texto2)