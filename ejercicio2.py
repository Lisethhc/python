import random

print("***GENERADOR DE CONTRASEÑAS***")

def generar_contrasena(min_minuscula, min_mayuscula, min_numeros, longitud):
    caracteres_disponibles = []
    
    caracteres_disponibles.extend([chr(i) for i in range(97, 123)])  
    caracteres_disponibles.extend([chr(i) for i in range(65, 91)])  
    caracteres_disponibles.extend([str(i) for i in range(10)])

    if min_minuscula + min_mayuscula + min_numeros > longitud:
        return "Numero de requisito mayor a la longitud permitida"

    contrasena = []
    contrasena.extend(random.choices(caracteres_disponibles[:26], k=min_minuscula))
    contrasena.extend(random.choices(caracteres_disponibles[26:52], k=min_mayuscula))
    contrasena.extend(random.choices(caracteres_disponibles[52:], k=min_numeros))
    
    #Rellenar los vacios con caracteres aleatorios
    caracteres_restantes = longitud - min_minuscula - min_mayuscula - min_numeros
    contrasena.extend(random.choices(caracteres_disponibles, k=caracteres_restantes))

    #Mezclar la contraseña
    random.shuffle(contrasena)

    contrasena = ''.join(contrasena)

    return contrasena

while True:
    min_minuscula = int(input("Indique número mínimo de minúsculas: "))
    min_mayuscula = int(input("Indique número mínimo de mayúsculas: "))
    min_numeros = int(input("Indique número mínimo de caracteres numéricos: "))
    longitud = int(input("Indique longitud de la contraseña: "))

    print("SU CONTRASEÑA:", generar_contrasena(min_minuscula, min_mayuscula, min_numeros, longitud))

    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() != 's':
        break