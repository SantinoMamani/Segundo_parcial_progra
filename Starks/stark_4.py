from data_stark import lista_personajes
import re


"""
Extrae las iniciales de un nombre de héroe.

Recibe:
- nombre_heroe (str): El nombre del héroe.

Retorna:
- str: Las iniciales del nombre en formato abreviado. Si no hay iniciales, retorna "N/A".
"""

def extraer_iniciales (nombre_heroe:str):
    if nombre_heroe == "":
        return "N/A"

    nombre_limpio = nombre_heroe.replace('-', ' ').replace("the", "")

    palabras = nombre_limpio.split()
    iniciales = [palabra[0].upper() for palabra in palabras if palabra.isalpha()]

    if iniciales:
        iniciales_str = '.'.join(iniciales) + '.'
        return iniciales_str
    else:
        return "N/A"

"""
Obtiene un dato en formato de texto seguro para su uso en el código.

Recibe:
- dato (str): El dato a formatear.

Retorna:
- str: El dato formateado y seguro para su uso en el código.
"""

def obtener_dato_formato(dato:str):
    if type(dato) == str:

        dato = dato.lower()
        dato = re.sub('[a-zA-Z0-9]+', '_', dato)

        return dato
    else:
        return False

"""
Imprime los nombres de los héroes junto con sus iniciales.

Recibe:
- lista_heroes (str): La lista de héroes.

Retorna:
- None
"""

def stark_imprimir_nombre_con_iniciales(lista_heroes:str):
    nombres = []

    for heroe in lista_heroes:
        nombre = heroe["nombre"]
        iniciales = extraer_iniciales(nombre)
        nombres.append(f"{nombre}({iniciales})")

    resultado = "-".join(nombres)
    print(resultado)


"""
Imprime los nombres de los héroes junto con sus iniciales.

Recibe:
- lista_heroes (list): La lista de héroes.

Retorna:
- bool: True si al menos un héroe tiene iniciales, False en otros casos.
"""

def stark_imprimir_nombre_con_iniciales_dos(lista_heroes:list):
    cadena = False
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if stark_imprimir_nombre_con_iniciales(heroe):
                cadena = True
    return cadena


"""
Genera el código único de un héroe basado en su género y posición en la lista.

Recibe:
- heroe (dict): El diccionario que representa al héroe.
- id (int): La posición del héroe en la lista.

Retorna:
- str: El código único del héroe.
"""

def generar_codigo_heroe(heroe, id):
    # Valida que el parámetro heroe sea un diccionario y contenga la clave 'genero'
    if not isinstance(heroe, dict) or 'genero' not in heroe:
        return 'N/A'

    # Obtener el género del héroe
    genero = heroe['genero']

    # Valida que el género sea uno de los valores esperados
    if genero not in ['M', 'F', 'NB']:
        return 'N/A'

    # Determina el primer número del código según el género
    primer_numero = {'M': '1', 'F': '2', 'NB': '0'}[genero]

    # Formatear el código
    codigo = f"{genero}-{primer_numero}{'0' * (7 - len(str(id)))}{id}"

    return codigo


"""
Genera y muestra los códigos únicos de los héroes en la lista.

Recibe:
- lista_heroes (list): La lista de héroes.

Retorna:
- None
"""

def stark_generar_codigo_heroes(lista_heroes: list):
    for personaje, heroe in enumerate(lista_heroes, start=1):
        if isinstance(heroe, dict) and 'nombre' in heroe:
            codigo = generar_codigo_heroe(heroe, personaje)
            print(f"*{heroe['nombre']}({extraer_iniciales(heroe['nombre'])})|  {codigo}")
        else:
            return False

"""
Convierte un número en formato de cadena a un entero positivo, o retorna None si no es posible.

Recibe:
- numero_str (str): El número en formato de cadena.

Retorna:
- int or None: El número entero positivo o None si no es posible convertirlo.
"""

def sanitizar_entero(numero_str: str):
    try:
        numero_entero = int(numero_str)
        if numero_entero >= 0:
            return numero_entero
    except (ValueError, TypeError):
        pass

    return None

"""
Convierte un número en formato de cadena a un número flotante positivo, o retorna None si no es posible.

Recibe:
- numero_str (str): El número en formato de cadena.

Retorna:
- float or None: El número flotante positivo o None si no es posible convertirlo.
"""

def sanitizar_flotante(numero_str: str):
    resultado = None

    if type(numero_str) == float:
        return numero_str

    numero_str = numero_str.strip()

    if numero_str.replace(".", "", 1).isdigit():
        numero = float(numero_str)
        if numero >= 0:
            resultado = numero
        else:
            resultado = None  # Número negativo
    else:
        resultado = None  # Si no es un número válido

    return resultado

"""
Sanitiza una cadena de texto, convirtiéndola a minúsculas y eliminando caracteres no alfabéticos.

Recibe:
- valor_str: La cadena de texto a sanitizar.
- valor_por_defecto: El valor por defecto a retornar si la cadena está vacía.

Retorna:
- str: La cadena sanitizada o el valor por defecto si es necesario.
"""

def sanitizar_string(valor_str, valor_por_defecto=None):
    if valor_str is None or valor_str.strip() == "":
        return valor_por_defecto

    valor_str = str(valor_str).strip()

    if re.match(r"^[a-zA-Z\s]*$", valor_str):
        valor_str = valor_str.replace('/', ' ')
        return valor_str.lower()
    else:
        return valor_por_defecto

"""
Sanitiza un dato específico de un héroe según su tipo (string, entero, flotante).

Recibe:
- heroe (dict): El diccionario que representa al héroe.
- clave (str): La clave del dato a sanitizar.
- tipo_dato (str): El tipo de dato a sanitizar.

Retorna:
- str or None: Un mensaje de error si la sanitización falla, None si tiene éxito.
"""

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
        # Valida que tipo_dato sea uno de los valores permitidos
    tipo_dato = tipo_dato.lower()  # Convierte a minúsculas para hacer la validación insensible a mayúsculas
    if tipo_dato not in ['string', 'entero', 'flotante']:
        print("Tipo de dato no reconocido")
        return False

    # Valida si la clave existe en el diccionario heroe
    if clave not in heroe:
        print("La clave especificada no existe en el héroe")
        return False

    # Obtiene el valor asociado a la clave
    valor = heroe[clave]

    # Sanitiza el valor dependiendo del tipo de dato
    if tipo_dato == 'string':
        heroe[clave] = sanitizar_string(valor)
    elif tipo_dato == 'entero':
        resultado = sanitizar_entero(valor)
        if resultado is not None:
            heroe[clave] = resultado
        else:
            return f"El valor '{valor}' no es un entero positivo"
    elif tipo_dato == 'flotante':
        resultado = sanitizar_flotante(valor)
        if resultado is not None:
            heroe[clave] = resultado
        else:
            return f"El valor '{valor}' no es un número flotante positivo"

    return None

"""
Normaliza los datos numéricos en la lista de héroes.

Recibe:
- lista_heroes (list): La lista de héroes.

Retorna:
- None
"""

def stark_normalizar_datos(lista_heroes: list):
    if len(lista_heroes) != 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe, "altura", "flotante")
            sanitizar_dato(heroe, "peso", "flotante")
            sanitizar_dato(heroe, "color_ojos", "flotante")
            sanitizar_dato(heroe, "color_pelo", "flotante")
            sanitizar_dato(heroe, "fuerza", "flotante")
            sanitizar_dato(heroe, "inteligencia", "flotante")
        print("Datos normalizados")
    else:
        print("Lista vacia error")

"""
Imprime el índice y nombre de los héroes junto con sus iniciales.

Recibe:
- lista_heroes (list): La lista de héroes.

Retorna:
- None
"""

def stark_imprimir_indice_nombre(lista_heroes:list):
    for i, heroe in enumerate(lista_heroes, start=1):
        nombre = heroe.get("nombre", "")
        iniciales = extraer_iniciales(nombre)
        print(f"{i}. {nombre}({iniciales})")

"""
Genera un separador utilizando un patrón y longitud específicos.

Recibe:
- patron (str): El patrón para el separador.
- largo (int): La longitud del separador.
- imprimir (bool): Indica si imprimir el separador.

Retorna:
- str: El separador generado.
"""

def generar_separador(patron:str, largo:int, imprimir = True):
    if (len(patron) > 0 and len(patron) < 3) and (type(largo) == int) and (largo > 0 and largo < 236):
        retorno = patron *largo
        if imprimir:
            print(retorno)
    else:
        retorno = "N/A"

    return retorno

"""
Genera un encabezado en mayúsculas utilizando un título específico.

Recibe:
- titulo (str): El título del encabezado.

Retorna:
- str: El encabezado generado.
"""

def generar_encabezado(titulo:str):
    titulo = titulo.upper()
    separador = generar_separador("*", 149, False)
    encabezado = f"{separador}\n{titulo}\n{separador}"
    return encabezado


"""
Imprime la ficha de un héroe con información detallada.

Recibe:
- heroe (dict): El diccionario que representa al héroe.

Retorna:
- None
"""

def imprimir_ficha_heroe(heroe: dict):
    separador_largo = generar_separador('*', 80)
    separador_corto = generar_separador('*', 30)
    titulo_principal = generar_encabezado("Principal")
    titulo_fisico = generar_encabezado("Físico")
    titulo_senas_particulares = generar_encabezado("Señas Particulares")

    # Obtener datos del héroe
    nombre_heroe = sanitizar_string(heroe.get("nombre", ""))
    nombre_codigo = generar_codigo_heroe(heroe, 1)
    identidad_secreta = sanitizar_string(heroe.get("identidad", ""))
    consultora = sanitizar_string(heroe.get("empresa", ""))
    altura = sanitizar_flotante(heroe.get("altura", ""))
    peso = sanitizar_flotante(heroe.get("peso", ""))
    
    # Manejar el caso de fuerza como float
    fuerza_heroe = sanitizar_entero(heroe.get("fuerza", ""))
    if fuerza_heroe is None:
        fuerza_heroe = "N/A N"
    else:
        fuerza_heroe = f"{fuerza_heroe}"

    color_ojos = sanitizar_string(heroe.get("color_ojos", ""))
    color_pelo = sanitizar_string(heroe.get("color_pelo", ""))

    # Imprimir la ficha
    print(separador_largo)
    print(titulo_principal)
    print(separador_largo)
    print(f"NOMBRE DEL HÉROE: {nombre_heroe} ({nombre_codigo})")
    print(f"IDENTIDAD SECRETA: {identidad_secreta}")
    print(f"CONSULTORA: {consultora}")
    print(f"CÓDIGO DE HÉROE: {nombre_codigo}")

    print(separador_corto)
    print(titulo_fisico)
    print(separador_corto)
    print(f"ALTURA: {altura} cm.")
    print(f"PESO: {peso} kg.")
    print(f"FUERZA TOTAL: {fuerza_heroe}")

    print(separador_corto)
    print(titulo_senas_particulares)
    print(separador_corto)
    print(f"COLOR DE OJOS: {color_ojos}")
    print(f"COLOR DE PELO: {color_pelo}")


"""
Permite navegar entre las fichas detalladas de los héroes en la lista.

Recibe:
- lista_heroes (list): La lista de héroes.

Retorna:
- None
"""

def stark_navegar_fichas(lista_heroes):
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        

    indice = 0

    while True:
        # Imprimir la ficha del héroe actual
        imprimir_ficha_heroe(lista_heroes[indice])

        # Solicitar al usuario que ingrese una opción
        print("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ 3 ] Salir")
        opcion = input("Elija una opción: ")

        if opcion == '1':
            # Ir a la izquierda (anterior héroe)
            indice = (indice - 1) % len(lista_heroes)
        elif opcion == '2':
            # Ir a la derecha (siguiente héroe)
            indice = (indice + 1) % len(lista_heroes)
        elif opcion == '3':
            # Salir
            break
        else:
            # Opción no válida
            print("Opción no válida. Por favor, elija una opción válida.")
            
"""
Imprime el menú principal con las opciones disponibles.

Retorna:
- None
"""
def imprimir_menu_principal():
    print("Menú Principal:")
    print("1 - Imprimir la lista de nombres junto con sus iniciales")
    print("2 - Imprimir la lista de nombres y el código del mismo")
    print("3 - Normalizar datos")
    print("4 - Imprimir índice de nombres")
    print("5 - Navegar fichas")
    print("6 - Salir")

"""
Implementa el menú principal para interactuar con las funciones disponibles.

Recibe:
- lista_heroes (list): La lista de héroes.

Retorna:
- None
"""

def stark_menu_principal(lista_heroes):            
    while True:
            imprimir_menu_principal()
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                # Imprimir la lista de nombres junto con sus iniciales
                stark_imprimir_nombre_con_iniciales(lista_heroes)
            elif opcion == '2':
                # Imprimir la lista de nombres y el código del mismo
                stark_generar_codigo_heroes(lista_heroes)
            elif opcion == '3':
                # Normalizar datos
                stark_normalizar_datos(lista_heroes)
                print("Datos normalizados")
            elif opcion == '4':
                # Imprimir índice de nombres
                stark_imprimir_indice_nombre(lista_heroes)
            elif opcion == '5':
                # Navegar fichas
                stark_navegar_fichas(lista_heroes)
            elif opcion == '6':
                # Salir
                break
            else:
                print("Opción no valida. Por favor, ingrese un número válido.")