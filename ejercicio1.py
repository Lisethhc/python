try:
    numero = int(input("Por favor ingresar un número entero: "))
    if numero % 2 == 0:
        print(f"{numero} es un numero par")
    else:
        print(f"{numero} es un numero impar")
except ValueError:
    print("Debes ingresar un numero entero")
