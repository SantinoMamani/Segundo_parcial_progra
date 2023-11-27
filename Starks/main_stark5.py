from data_stark import *
from stark_5 import *


while True:
    print("\nMenú:")
    print("1- Normalizar datos")
    print("2- Generar CSV")
    print("3- Listar héroes del archivo CSV ordenados por altura ASC")
    print("4- Generar JSON")
    print("5- Listar héroes del archivo JSON ordenados por peso DESC")
    print("6- Ordenar lista por fuerza")
    print("7- Salir")

    opcion = input("Ingresa la opción deseada: ")

    if opcion == '1':
        # Normalizar datos
        lista_personajes = normalizar_datos(lista_personajes)

    elif opcion == '2':
        # Generar CSV
        nombre_archivo_csv = "heroes.csv"
        if generar_csv(nombre_archivo_csv, lista_personajes):
            print(f"Se creó el archivo: {nombre_archivo_csv}")

    elif opcion == '3':
        # Listar héroes del archivo CSV ordenados por altura ASC
        nombre_archivo_csv = "heroes.csv"
        lista_personajes_csv = leer_csv(nombre_archivo_csv)
        if lista_personajes_csv:
            lista_personajes_csv = ordenar_heroes_ascendente(lista_personajes_csv, "altura")
            print("Lista de héroes ordenados por altura ASC:")
            print(f"{'Nombre':<20}{'Altura':<10}")
            print('-' * 30)
            for heroe in lista_personajes_csv:
                nombre = heroe['nombre']
                altura = heroe.get('altura', '')
                print(f"{nombre:<20}{altura:<10}")

    elif opcion == '4':
        # Generar JSON
        nombre_archivo_json = "heroes.json"
        if generar_json(nombre_archivo_json, lista_personajes, "heroes"):
            print(f"Se creó el archivo: {nombre_archivo_json}")

    elif opcion == '5':
        # Listar héroes del archivo JSON ordenados por peso DESC
        nombre_archivo_json = "heroes.json"
        lista_personajes_json = leer_json(nombre_archivo_json, "heroes")
        if lista_personajes_json:
            lista_personajes_json = ordenar_heroes_descendente(lista_personajes_json, "peso")
            print("Lista de héroes ordenados por peso DESC:")
            print(f"{'Nombre':<20}{'Peso':<10}")
            print('-' * 30)
            for heroe in lista_personajes_json:
                nombre = heroe['nombre']
                peso = heroe.get('peso', '')
                print(f"{nombre:<20}{peso:<10}")


    elif opcion == '6':
        # Ordenar lista por fuerza (preguntar al usuario)
        lista_personajes = ordenar_heroes_por_clave(lista_personajes, "fuerza")

    elif opcion == '7':
        # Salir
        break

    else:
        print("Opción no válida. Ingresa un número del 1 al 7.")

