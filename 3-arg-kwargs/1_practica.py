# 1. Calcular el mayor de dos números ingresados por teclado usando un operador
# ternario
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

print(f'{num1} es el mayor numero' if num1 > num2 else f'{num2} es el mayor numero.')
