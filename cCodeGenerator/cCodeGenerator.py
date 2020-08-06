"""
Generador de código para identificar si un número es par o impar en lenguaje C
by JChaconMencez
"""

import numpy as np
import os

def writetextfile(namefile, text):  # Función para escribir un string en un fichero
    try:
        file = open(namefile, "a")
        file.write(text)
        file.close()
    except:
        return 0
    else:
        return 1


# Inicio del script
nameFile = "par.c"
num2writeCcode = 10
try:
    num2writeCcode = int(input("Ingrese hasta que numero desea que pueda comparar el script: "))
    try:
        os.remove(nameFile)
        print("Previous file removed!")
    except:
        pass
    text2write = "#include <stdio.h>"  # Inclusion de la biblioteca stdio.h para entradas y salidas en C
    text2write += '\n\nint esPar(int numero) {' \
                  '\n\tif(numero == 1) {' \
                  '\n\t\treturn 0;'

    for i in range(num2writeCcode - 1):
        if (i + 2) % 2:
            text2write += '\n\t} else if(numero == ' + str(i + 2) + ') {' \
                                                                    '\n\t\treturn 0;'
        else:
            text2write += '\n\t} else if(numero == ' + str(i + 2) + ') {' \
                                                                    '\n\t\treturn 1;'

    text2write += '\n\t}\n}'
    # Inclusion de una funcion main para que se pueda compilar de manera autonoma por medio de gcc
    text2write += '\nint main() {' \
                  '\n\tint i;' \
                  '\n\tprintf("Ingresa un número: \\n");' \
                  '\n\tscanf("%d", &i);' \
                  '\n\tprintf("\\nIngresaste: %d\\n", i);' \
                  '\n\tint par = esPar(i);' \
                  '\n\tif (par==1){' \
                  '\n\t\tprintf("El número es par!\\n");' \
                  '\n\t} else {' \
                  '\n\t\tprintf("El número no es par!\\n");' \
                  '\n\t}\n\treturn 0;' \
                  '\n}'

    fileWrited = writetextfile(nameFile, text2write)
    if fileWrited:
        print("\nCodigo C creado con exito!")
    else:
        print("\nError creando codigo C!")
except:
    print("Dato invalido!")


