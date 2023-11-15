import sqlite3

NOMBRE_BASE_DE_DATOS = "ranking.db"

def crear_tabla_carreras():
    try:
        conexion = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
        conexion.execute('''CREATE TABLE IF NOT EXISTS jugadores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nombre TEXT,
                        puntuacion INTEGER
                    )''')
        conexion.close()
    except sqlite3.OperationalError as e:
        print(f"Error al crear la tabla: {e}")

def insertar_jugadores(nombre, puntaje_global):
    try:
        conexion = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
        print("Conexión exitosa a la base de datos")
        conexion.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?,?)", (nombre, puntaje_global))
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        print(f"Error al insertar jugadores: {e}")

def obtener_ranking():
    try:
        conexion = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
        cursor = conexion.execute("SELECT nombre, puntuacion FROM jugadores ORDER BY puntuacion DESC")
        ranking = cursor.fetchall()
        return ranking
    except sqlite3.Error as e:
        print(f"Error al obtener el ranking: {e}")