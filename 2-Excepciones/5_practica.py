# 5. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
# captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.


try:
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese otro numero: '))

    res = num1 / num2
    print(res)

except ValueError:
    print('Se ingresó un valor no numérico.')
except ZeroDivisionError:
    print('El segundo número no debe ser cero.')
except Exception as e:
    print(f'Algo pasó: {e}')


