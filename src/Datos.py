import csv
import matplotlib.pyplot as plt

## Funciones para archivos de texto
def txt_op1(ruta_txt):
    """Cuenta el número de palabras en el archivo de texto."""
    try:
        with open(ruta_txt, 'r') as archivo:
            texto = archivo.read()
            palabras = texto.split()
            print(f"Número total de palabras: {len(palabras)}")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")

def txt_op2(ruta_txt):
    """Reemplaza una palabra por otra en el archivo de texto."""
    palabra_vieja = input("Ingrese la palabra que desea reemplazar: ")
    palabra_nueva = input("Ingrese la nueva palabra: ")
    try:
        with open(ruta_txt, 'r') as archivo:
            texto = archivo.read()
        texto_modificado = texto.replace(palabra_vieja, palabra_nueva)
        with open(ruta_txt, 'w') as archivo:
            archivo.write(texto_modificado)
        print(f"'{palabra_vieja}' ha sido reemplazada por '{palabra_nueva}' en el archivo.")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")

def txt_op3(ruta_txt):
    """Cuenta el número de caracteres en el archivo de texto, con y sin espacios."""
    try:
        with open(ruta_txt, 'r') as archivo:
            texto = archivo.read()
            caracteres_con_espacios = len(texto)
            caracteres_sin_espacios = len(texto.replace(" ", ""))
            print(f"Número de caracteres (con espacios): {caracteres_con_espacios}")
            print(f"Número de caracteres (sin espacios): {caracteres_sin_espacios}")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")

def txt():
    while True:
        txt_op = input("Escoja la opción que desea realizar\n1) Contar numero de palabras\n2) Reemplazar una palabra por otra\n3) Contar el numero de caracteres\n4) Regresar al menu principal\n")
        if txt_op != ("4"):
            ruta_txt= input("Ingrese la ruta del archivo de texto: ").strip('"').strip("'")
            if txt_op == "1":
                txt_op1(ruta_txt)
            elif txt_op == "2":
                txt_op2(ruta_txt)
            elif txt_op == "3":
                txt_op3(ruta_txt)
            else:
                print("Ingrese una opción adecuada.")
        else:
            print("Regresando a menu principal")
            break

## Funciones para archivos CSV
def csv_op1(ruta_csv):
    """Mostrar las 15 primeras filas del archivo CSV."""
    try:
        with open(ruta_csv, 'r') as archivo:
            lector = csv.reader(archivo)
            for i, fila in enumerate(lector):
                if i >= 15:
                    break
                print(fila)
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")

def csv_op2(ruta_csv):
    columna = input("Ingrese el nombre de la columna para calcular estadísticas: ")
    datos = []
    try:
        with open(ruta_csv, 'r') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            
            # Encontrar el índice de la columna
            if columna not in encabezados:
                print(f"Columna '{columna}' no encontrada en el archivo.")
                return
            indice_columna = encabezados.index(columna)
            
            # Recoger datos de la columna
            for fila in lector:
                try:
                    dato = float(fila[indice_columna])
                    datos.append(dato)
                except ValueError:
                    print(f"Valor no numérico encontrado en la fila {fila}. Saltando...")
        
        # Calcular estadísticas
        if datos:
            num_datos = len(datos)
            promedio = sum(datos) / num_datos
            datos_ordenados = sorted(datos)
            mediana = (datos_ordenados[num_datos // 2] if num_datos % 2 != 0 
                       else (datos_ordenados[num_datos // 2 - 1] + datos_ordenados[num_datos // 2]) / 2)
            valor_maximo = max(datos)
            valor_minimo = min(datos)
            
            print(f"Estadísticas para la columna '{columna}':")
            print(f"Número de datos: {num_datos}")
            print(f"Promedio: {promedio}")
            print(f"Mediana: {mediana}")
            print(f"Valor máximo: {valor_maximo}")
            print(f"Valor mínimo: {valor_minimo}")
        else:
            print("No se encontraron datos numéricos en la columna.")
    
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")

def csv_op3(ruta_csv):
    """Graficar los datos de una columna numérica."""
    columna = input("Ingrese el nombre de la columna que desea graficar: ")
    datos = []
    try:
        with open(ruta_csv, 'r') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            
            # Encontrar el índice de la columna
            if columna not in encabezados:
                print(f"Columna '{columna}' no encontrada en el archivo.")
                return
            indice_columna = encabezados.index(columna)
            
            # Recoger datos de la columna
            for fila in lector:
                try:
                    dato = float(fila[indice_columna])
                    datos.append(dato)
                except ValueError:
                    print(f"Valor no numérico encontrado en la fila {fila}. Saltando...")

        # Graficar los datos si hay datos numéricos
        if datos:
            plt.plot(datos)
            plt.title(f"Gráfica de la columna '{columna}'")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
            plt.show()
        else:
            print("No se encontraron datos numéricos en la columna para graficar.")
    
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente de nuevo.")

def Fcsv():
    while True:
        csv_op = input("Que operación con archivos csv desea realizar? \n1) Mostrar las 15 primeras filas\n2) Calcular estadisticas\n3) Graficar una columna\n4) Regresar al menu principal\n")
        if csv_op != ("4"):
            ruta_csv = input("Ingrese la ruta del archivo CSV: ").strip('"').strip("'")
            if csv_op == "1":
                csv_op1(ruta_csv)
            elif csv_op == "2":
                csv_op2(ruta_csv)
            elif csv_op == "3":
                csv_op3(ruta_csv)
            else:
                print("Ingrese una opción adecuada.")
        else:
            print("Regresando a menu principal")
            break


def archivos():
    pass

## Menú principal
def menu_ppl():
    print("Bienvenido al menú principal")
    while True:
        op = input("¿Qué operación desea realizar? \n1) Archivos de texto\n2) Archivos CSV\n3) Listar archivos\n4) Salir\n")
        if op == "1":
            txt()
        elif op == "2":
            Fcsv()
        elif op == "3":
            archivos()
        elif op == "4":
            print("Saliendo del programa...")
            break
        else: 
            print("Ingrese una opción adecuada, por favor")

if __name__ == "__main__":
    menu_ppl()
