import os,csv,json
from data_stark import *

"""
Lee el contenido de un archivo.

Recibe:
- nombre_archivo (str): El nombre del archivo a leer.

Retorna:
- str or False: El contenido del archivo o False en caso de error.
"""

def leer_archivo(nombre_archivo):
    try:
        # Intenta abrir el archivo en modo de lectura ('r') con codificación utf-8
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Lee el contenido del archivo
            contenido = archivo.read()
        # Retorna el contenido si la operación fue exitosa
        return contenido
    except Exception as e:
        # Captura cualquier excepción que ocurra durante la lectura del archivo
        # Imprime un mensaje de error y retorna False
        print(f'Error al leer el archivo {nombre_archivo}: {str(e)}')
        return False

    
"""
Guarda contenido en un archivo.

Recibe:
- nombre_archivo (str): El nombre del archivo a crear o sobrescribir.
- contenido (str): El contenido a escribir en el archivo.

Retorna:
- bool: True si la operación fue exitosa, False en caso contrario.
"""

def guardar_archivo(nombre_archivo, contenido):
    try:
        # Intenta abrir el archivo en modo de escritura ('w') con codificación utf-8
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            # Escribe el contenido en el archivo
            archivo.write(contenido)
        # Imprime un mensaje indicando que se creó el archivo exitosamente
        print(f"Se creó el archivo: {nombre_archivo}")
        # Retorna True para indicar que la operación fue exitosa
        return True
    except Exception as e:
        # Captura cualquier excepción que pueda ocurrir durante el proceso
        # Imprime un mensaje de error y retorna False
        print(f"Error al crear el archivo {nombre_archivo}: {str(e)}")
        return False


"""
Genera un archivo CSV a partir de una lista de superhéroes.

Recibe:
- nombre_archivo (str): El nombre del archivo CSV a crear.
- lista_superheroes (list): La lista de superhéroes.

Retorna:
- bool: True si la operación fue exitosa, False en caso contrario.
"""

# Punto 1.3
def generar_csv(nombre_archivo, lista_superheroes):
    if lista_superheroes:
        # Crear el string CSV
        contenido_csv = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"
        for heroe in lista_superheroes:
            contenido_csv += f"{heroe['nombre']},{heroe['identidad']},{heroe['empresa']},{heroe['altura']},{heroe['peso']},{heroe['genero']},{heroe['color_ojos']},{heroe['color_pelo']},{heroe['fuerza']},{heroe['inteligencia']}\n"

        # Llamada a la función para guardar el archivo
        return guardar_archivo(nombre_archivo, contenido_csv)
    else:
        print("La lista de superhéroes está vacía.")
        return False

"""
Lee un archivo CSV y retorna una lista de superhéroes.

Recibe:
- nombre_archivo (str): El nombre del archivo CSV a leer.

Retorna:
- list or False: La lista de superhéroes o False en caso de error.
"""

# Punto 1.4
def leer_csv(nombre_archivo):
    try:
        lista_superheroes = []  # Inicializa una lista para almacenar los superhéroes
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)  # Utiliza DictReader para obtener un diccionario por cada fila
            for row in lector_csv:
                lista_superheroes.append(row)  # Agrega el diccionario a la lista
        return lista_superheroes
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {str(e)}")
        return False
    

"""
Lee un archivo CSV y retorna una lista de superhéroes.

Recibe:
- nombre_archivo (str): El nombre del archivo CSV a leer.

Retorna:
- list or False: La lista de superhéroes o False en caso de error.
"""

def generar_json(nombre_archivo, lista_superheroes, nombre_lista):
    if lista_superheroes:
        # Normalizar los datos antes de generar el JSON
        lista_normalizada = normalizar_datos(lista_superheroes)

        # Crear un diccionario con una sola clave (nombre_lista)
        diccionario_superheroes = {nombre_lista: lista_normalizada}

        try:
            # Guardar el diccionario como JSON en el archivo con indent=4
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
                json.dump(diccionario_superheroes, archivo_json, indent=4) 

            print(f"Se creó el archivo JSON: {nombre_archivo}")
            return True
        except Exception as e:
            print(f"Error al crear el archivo JSON {nombre_archivo}: {str(e)}")
            return False
    else:
        print("La lista de superhéroes está vacía.")
        return False

"""
Normaliza los datos numéricos en la lista de superhéroes.

Recibe:
- lista_superheroes (list): La lista de superhéroes.

Retorna:
- list: La lista de superhéroes con datos normalizados.
"""
    
def normalizar_datos(lista_superheroes):
    lista_normalizada = []  # Inicializa una lista vacía para almacenar los superhéroes normalizados

    for heroe in lista_superheroes:
        try:
            # Intenta convertir los valores de altura, peso y fuerza a tipos de datos específicos
            heroe["altura"] = float(heroe["altura"]) if heroe["altura"] else None
            heroe["peso"] = float(heroe["peso"]) if heroe["peso"] else None
            heroe["fuerza"] = int(heroe["fuerza"]) if heroe["fuerza"] else None
        except ValueError as e:
            # Captura excepciones de tipo ValueError, como cuando la conversión no es posible
            print(f"Error al convertir valores: {e}. Ignorando este héroe.")
            continue

        # Agrega el héroe normalizado a la lista
        lista_normalizada.append(heroe)

    return lista_normalizada  # Retorna la lista de superhéroes normalizada


def datos_normalizados(heroes, clave):
    for heroe in heroes:
        if not isinstance(heroe[clave], (int, float)):
            return False
    return True


"""
Lee un archivo JSON y retorna la lista de superhéroes.

Recibe:
- nombre_archivo (str): El nombre del archivo JSON a leer.
- nombre_lista (str): El nombre de la lista en el JSON.

Retorna:
- list or False: La lista de superhéroes o False en caso de error.
"""

def leer_json(nombre_archivo, nombre_lista):
    try:
        # Abre el archivo JSON en modo de lectura
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Carga los datos del archivo JSON en un diccionario
            datos = json.load(archivo)
            # Extrae la lista de superhéroes con el nombre especificado
            retorno = datos.get(nombre_lista, [])
    except FileNotFoundError:
        # Captura la excepción si el archivo no se encuentra
        print(f"El archivo {nombre_archivo} no existe.")
        retorno = False
    except Exception as e:
        # Captura cualquier otra excepción que pueda ocurrir durante el proceso
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        retorno = False
    return retorno

"""
Ordena la lista de héroes de manera ascendente según una clave específica.

Recibe:
- heroes (list): La lista de héroes.
- clave (str): La clave para la cual se realiza la ordenación.

Retorna:
- list: La lista de héroes ordenada de manera ascendente.
"""

def ordenar_heroes_ascendente(heroes, clave):
    n = len(heroes)  # Obtiene la longitud de la lista de héroes
    for i in range(n):
        for j in range(0, n-i-1):
            # Compara los valores de la clave para decidir si se necesita intercambio
            if float(heroes[j][clave]) > float(heroes[j+1][clave]):
                # Intercambia los elementos si el valor actual es mayor que el siguiente
                heroes[j], heroes[j+1] = heroes[j+1], heroes[j]
    return heroes  # Retorna la lista de héroes ordenada


"""
Ordena la lista de héroes de manera descendente según una clave específica.

Recibe:
- heroes (list): La lista de héroes.
- clave (str): La clave para la cual se realiza la ordenación.

Retorna:
- list: La lista de héroes ordenada de manera descendente.
"""

def ordenar_heroes_descendente(heroes, clave):
    n = len(heroes)  # Obtiene la longitud de la lista de héroes
    for i in range(n):
        for j in range(0, n-i-1):
            # Compara los valores de la clave para decidir si se necesita intercambio
            if float(heroes[j][clave]) < float(heroes[j+1][clave]):
                # Intercambia los elementos si el valor actual es menor que el siguiente
                heroes[j], heroes[j+1] = heroes[j+1], heroes[j]
    return heroes  # Retorna la lista de héroes ordenada en orden descendente


"""
Ordena la lista de héroes según una clave específica y dirección (ascendente o descendente).

Recibe:
- heroes (list): La lista de héroes.
- clave (str): La clave para la cual se realiza la ordenación.

Retorna:
- list: La lista de héroes ordenada según la clave y dirección especificadas.
"""

def ordenar_heroes_por_clave(heroes, clave):
    # Verifica si los datos están normalizados
    if not datos_normalizados(heroes, clave):
        print("¡Error! Los datos no están normalizados. Por favor, normalice los datos antes de continuar.")
        return heroes
    
    # Pregunta al usuario cómo quiere ordenar los héroes
    direccion = input("¿Cómo quieres ordenar los héroes? ('asc' para ascendente, 'desc' para descendente): ").lower()

    if direccion == 'asc':
        # Si la dirección es 'asc', llama a la función de orden ascendente
        heroes_ordenados = ordenar_heroes_ascendente(heroes, clave)
    elif direccion == 'desc':
        # Si la dirección es 'desc', llama a la función de orden descendente
        heroes_ordenados = ordenar_heroes_descendente(heroes, clave)
    else:
        # Si la dirección no es válida, imprime un mensaje y devuelve la lista sin ordenar
        print("Opción no válida. Se devolverá la lista sin ordenar.")
        return heroes

    # Imprime la lista ordenada en forma de columnas
    print(f"{'Nombre':<20}{'Fuerza':<10}")
    print('-' * 30)
    for heroe in heroes_ordenados:
        nombre = heroe['nombre']  # Asegúrate de ajustar el nombre del campo según tu estructura de datos
        fuerza = heroe['fuerza']  # Asegúrate de ajustar el nombre del campo según tu estructura de datos
        print(f"{nombre:<20}{fuerza:<10}")

    return heroes_ordenados  # Retorna la lista de héroes ordenada
