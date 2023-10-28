
En este documento se explica el codigo y el funcionamiento del proyecto GENERADOR DE CONTRASEÑAS. Se utilizó para el proyecto la version de Python 3.10.13 debido a que fue la version que me salió disponible en ese rango y pyenv 3.10.13, se instalaron las dependencias de request y la extension isort.

Iniciamos con el titulo para que el usuario pueda identificar de que se trata
print("****GENERADOR DE CONTRASEÑAS****")

En el siguiente codigo primeramente se establece una función que se llama generar_contrasena utilizando el guion en el piso para separar las palabras, se le pasa como argumentos los requisitos minimos del proyecto que se le solicita al usuario.

def generar_contrasena(min_minuscula, min_mayuscula, min_numeros, longitud):
    
#Se crea la variable caracteres_disponibles para realizar la lista de todos los caracteres que se pueden usar para la contraseña solicitada dejando vacío dentro de los corchetes para luego poder aisgnar los valores.    
   
    caracteres_disponibles = []

#En estos codigos se extrae los rangos de las letras "a" a la "z" en minuscula, de la "A" a la "Z" en Mayuscula utilizando los rangos de la tabla ASCII y convertirlos con la funcion chr y los digitos del 0 al 9.

    caracteres_disponibles.extend([chr(i) for i in range(97, 123)])  
    caracteres_disponibles.extend([chr(i) for i in range(65, 91)])  
    caracteres_disponibles.extend([str(i) for i in range(10)])

#Se establece un condicional de si la sumatoria de los minimos requeridos es mayor que la longitud de la contraseña no podría cumplir con la regla y saldrá un msj para avisar que no cumple con los requisitos.

    if min_minuscula + min_mayuscula + min_numeros > longitud:
        return "Numero de requisito mayor a la longitud permitida"

#Se crea la variable contraseña donde se va a guardar los caracteres aleatorios que se le asignará y el resultado sera una lista.

    contrasena = []

#Con la funcion random.choices se selecciona aleatoriamente los caracteres de la lista antes creadas de caracteres_disponibles, identificando que solo puede seleccionar una cantidad minima de la lista llamada k y estableciendo el rango de la posicion 0 a 25 que sería las letras minusculas, de 26 a 51 que serian las letras mayusculas y desde la 52 hasta el final de la lista que son los digitos.

    contrasena.extend(random.choices(caracteres_disponibles[:26], k=min_minuscula))
    contrasena.extend(random.choices(caracteres_disponibles[26:52], k=min_mayuscula))
    contrasena.extend(random.choices(caracteres_disponibles[52:], k=min_numeros))
    
#En esta parte se rellenan los vacios en el caso que la longitud sea mayor a la sumatoria de las cantidades minimas con caracteres aleatorios, se determina la variable de caracteres_restantes para saber el numero de espacios sin caracter asignado.

    caracteres_restantes = longitud - min_minuscula - min_mayuscula - min_numeros
    contrasena.extend(random.choices(caracteres_disponibles, k=caracteres_restantes))

#Con la funcion random.shuffle se mezclan los caracteres de la contraseña, debido a que antes de este punto aun se encontraban en orden.
    
    random.shuffle(contrasena)

#Con ''.join se convierte la contraseña que antes de este punto se encontraba en lista en una cadena de texto sin ningun tipo de separadores entre ellos que lo hace ''.
    contrasena = ''.join(contrasena)

#Al final de la funcion retorna la contrasena que es la que estamos necesitando para mostrar al usuario.

    return contrasena

#En esta parte se solicita al usuario las cantidades minimas de minusculas, mayusculas, numeros y la longitud para poder realizar la contraseña.

min_minuscula = int(input("Indique número mínimo de minúsculas: "))
min_mayuscula = int(input("Indique número mínimo de mayúsculas: "))
min_numeros = int(input("Indique número mínimo de caracteres numéricos: "))
longitud = int(input("Indique longitud de la contraseña: "))

#Aqui se imprime para mostrar al usuario la contraseña que se generó.

print("Contraseña generada:", generar_contrasena(min_minuscula, min_mayuscula, min_numeros, longitud))