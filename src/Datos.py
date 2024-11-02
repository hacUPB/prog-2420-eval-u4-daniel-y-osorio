## Funciones para archivos de texto
def txt_op1():
    """Cuenta el número de palabras en el archivo de texto."""
    ruta_archivo = input("Ingrese la ruta del archivo de texto: ")
    try:
        with open(ruta_archivo, 'r') as archivo:
            texto = archivo.read()
            palabras = texto.split()
            print(f"Número total de palabras: {len(palabras)}")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")
def txt_op2():
    """Reemplaza una palabra por otra en el archivo de texto."""
    ruta_archivo = input("Ingrese la ruta del archivo de texto: ")
    palabra_vieja = input("Ingrese la palabra que desea reemplazar: ")
    palabra_nueva = input("Ingrese la nueva palabra: ")
    try:
        with open(ruta_archivo, 'r') as archivo:
            texto = archivo.read()
        texto_modificado = texto.replace(palabra_vieja, palabra_nueva)
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(texto_modificado)
        print(f"'{palabra_vieja}' ha sido reemplazada por '{palabra_nueva}' en el archivo.")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")
def txt_op3():
    """Cuenta el número de caracteres en el archivo de texto, con y sin espacios."""
    ruta_archivo = input("Ingrese la ruta del archivo de texto: ")
    try:
        with open(ruta_archivo, 'r') as archivo:
            texto = archivo.read()
            caracteres_con_espacios = len(texto)
            caracteres_sin_espacios = len(texto.replace(" ", ""))
            print(f"Número de caracteres (con espacios): {caracteres_con_espacios}")
            print(f"Número de caracteres (sin espacios): {caracteres_sin_espacios}")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")
def txt():
    while True:
        txt_op = input("Escoja la opción que desea realizar\n1) Contar numero de palabras\n2) Reemplazar una palabra por otra\n3) Contar el numero de caracteres\n4) Regresar al menu principal")
                
        if txt_op == ("1"):
            txt_op1()
            break
        elif txt_op == ("2"):
            txt_op2()
            break
        elif txt_op == ("3"):
            txt_op3()
            break
        elif txt_op == ("4"):
            print("Regresando a menu principal")
        else:
            print("Ingrese una opcion adecuada")
## Funciones para archivos CSV
def csv_op1():
    pass
def csv_op2():
    pass
def csv_op3():
    pass
def csv():
    while True:
        csv_op = input("Que operación con archivos csv desea realizar? \n1) Mostrar las 15 primeras filas\n2) Calcular estadisticas\n3) Graficar una columna\n4) Regresar al menu principal")
        if csv_op == ("1"):
            csv_op1()
            break
        elif csv_op == ("2"):
            csv_op2()
            break
        elif csv_op == ("3"):
            csv_op3()
            break
        elif csv_op == ("4"):
            print("Regresando a menu principal")
        else:
            print("Ingrese una opcion adecuada")
def archivos():
    pass
## Menu principal
def menu_ppl():
    print("Bienvenido al menu principal")
    while True:
        op = input("Que operación con archivos de texto desea realizar? \n1) Archivos de texto\n2) Archivos CSV\n3) Listar archivos\n4) Salir")

        if op == ("1"):
            txt()
                    
        elif op == ("2"):
            csv()
            
        elif op == ("3"):
            archivos()
            pass
        elif op == ("4"):
            print("Saliendo del programa...")
            break
        else: 
            print("Ingrese una opcion adecuada, por favor")
if __name__ == "__main__":
    menu_ppl()