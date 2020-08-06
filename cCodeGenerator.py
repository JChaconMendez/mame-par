"""
Generador de código para identificar si un número es par o impar en lenguaje C
by JChaconMencez

La estructura original es:
function esPar(numero) {
if(numero == 1) {
return false
}
}else if(numero == 2) {
return true
}
}else if(numero == 3) {
return false;

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
num2writeCcode = 9
try:
    os.remove(nameFile)
    print("Previous file removed!")
except:
    pass



text2write = "#include <stdio.h>"                   # Inclusion de la biblioteca stdio.h para entradas y salidas en C
text2write += '\n\nint esPar(int numero) {' \
              '\n\tif(numero == 1) {' \
              '\n\t\treturn 0;'

for i in range(num2writeCcode-1):
    if (i+2)%2:
        text2write += '\n\t} else if(numero == ' + str(i+2) +') {' \
                      '\n\t\treturn 0;'
    else:
        text2write += '\n\t} else if(numero == ' + str(i+2) + ') {' \
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


writetextfile(nameFile, text2write)