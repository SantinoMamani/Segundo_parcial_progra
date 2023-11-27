import pygame,random,sys
from clases import AutoEnemigo, AutoJugador, AutoEnemigo2, AutoEnemigo3
from ranking import crear_tabla_carreras, insertar_jugadores, obtener_ranking

crear_tabla_carreras()
"""
Crea una tabla para el juego de carreras. Esta función contiene la lógica para inicializar
la tabla que almacene información sobre las puntajes del juego.

Retorna:
- None
"""

# Definición de la función del menú
"""
Muestra el menú principal del juego utilizando Pygame. Permite al jugador navegar por diferentes opciones
como seleccionar un nivel, salir del juego, ver las instrucciones, etc.

Retorna:
- None
""" 
def mostrar_menu():
    pygame.init()
    pantalla = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Menú de Juego")

    imagen_menu = pygame.image.load("imagen_menu.jpg")
    imagen_menu = pygame.transform.scale(imagen_menu, (800, 600))

    mostrar_imagen = True

    while mostrar_imagen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mostrar_imagen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(event.pos)
                print(posicion_click)
                # Opción A
                if (posicion_click[0] > 299 and posicion_click[0] < 504) and (posicion_click[1] > 142 and posicion_click[1] < 205):
                    print("A")
                    seleccionar_nivel()
                # Opción B
                elif (posicion_click[0] > 299 and posicion_click[0] < 510) and (posicion_click[1] > 423 and posicion_click[1] < 485):
                    print("B")
                    salir_del_juego()
                # Opción C
                elif (posicion_click[0] > 291 and posicion_click[0] < 500) and (posicion_click[1] > 325 and posicion_click[1] < 401):
                    print("C")
                    mostrar_como_jugar()
                # Opción D
                elif (posicion_click[0] > 299 and posicion_click[0] < 504) and (posicion_click[1] > 249 and posicion_click[1] < 304):
                    print("D")
                    ranking()
        pantalla.blit(imagen_menu, (0, 0))
        pygame.display.flip()
    pygame.quit()
    
"""
Permite al jugador seleccionar un nivel dentro del juego. Carga la interfaz gráfica correspondiente
para que el jugador elija el nivel deseado.

Retorna:
- None
"""

def seleccionar_nivel():
    pantalla = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Nivel completado")

    imagen_nivel_completado = pygame.image.load("seleccionar_nivel.jpg")
    imagen_nivel_completado = pygame.transform.scale(imagen_nivel_completado, (800, 600))
    
    mostrar_imagen = True

    while mostrar_imagen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mostrar_imagen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(event.pos)
                print(posicion_click)
                if (posicion_click[0] > 150 and posicion_click[0] < 269) and (posicion_click[1] > 293 and posicion_click[1] < 410):
                    print("A")
                    iniciar_nivel_1()
                elif (posicion_click[0] > 337 and posicion_click[0] < 453) and (posicion_click[1] > 292 and posicion_click[1] < 410):
                    print("B")
                    iniciar_nivel_2()
                elif (posicion_click[0] > 519 and posicion_click[0] < 634) and (posicion_click[1] > 293 and posicion_click[1] < 410):
                    print("C")
                    iniciar_nivel_3()
                    
        pantalla.blit(imagen_nivel_completado, (0, 0))
        pygame.display.flip()


"""
Cierra la aplicación del juego al salir. Detiene todos los procesos y libera recursos.

Retorna:
- None
"""

# Definición de la función para salir del juego
def salir_del_juego():
    pygame.quit()
    sys.exit()


"""
Muestra una imagen indicando que el nivel se ha completado. Permite al jugador avanzar al siguiente nivel
o volver al menú principal.

Parameters:
- pantalla (pygame.Surface): La superficie de Pygame donde se muestra la imagen.

Retorna:
- None
"""

# Definición de la función para mostrar la imagen "Nivel Completado"
def mostrar_imagen_nivel_completado(pantalla):
    pantalla = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Nivel completado")
    sonido_nivel_completado  = pygame.mixer.Sound("nivelcompleto.mp3")
    sonido_nivel_completado.play()
    # Define y carga la imagen de "Nivel Completado" antes de cualquier función
    imagen_nivel_completado = pygame.image.load("nivel_completado.png")
    imagen_nivel_completado = pygame.transform.scale(imagen_nivel_completado, (800, 600))
    
    mostrar_imagen = True

    while mostrar_imagen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(event.pos)
                print(posicion_click)
                if (posicion_click[0] > 316 and posicion_click[0] < 439) and (posicion_click[1] > 401 and posicion_click[1] < 454):
                    print("A")
                    sonido_nivel_completado.stop()
                    seleccionar_nivel()
                elif (posicion_click[0] > 513 and posicion_click[0] < 549) and (posicion_click[1] > 114 and posicion_click[1] < 156) and nivel_1_completado == True:
                    print("B")   
                    sonido_nivel_completado.stop()
                    salir_del_juego()
        pantalla.blit(imagen_nivel_completado, (0, 0))
        pygame.display.flip()


"""
Muestra la pantalla de Game Over, permitiendo al jugador ingresar su nombre y guardar su puntuación.

Parameters:
- pantalla (pygame.Surface): La superficie de Pygame donde se muestra la pantalla de Game Over.
- puntaje_global (int): El puntaje total del jugador.

Retorna:
- None
"""

def mostrar_game_over(pantalla, puntaje_global):
    pantalla = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Game Over")
    pygame.mixer.music.pause()
    sonido_game_over = pygame.mixer.Sound("gameover.mp3")
    sonido_game_over.set_volume(0.4)
    sonido_game_over.play()
    imagen_game_over = pygame.image.load("game_over.jpg")
    imagen_game_over = pygame.transform.scale(imagen_game_over, (800, 600))
    pantalla.blit(imagen_game_over, (0, 0))
    pygame.display.flip()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(event.pos)
                print(posicion_click)
                if (posicion_click[0] > 276 and posicion_click[0] < 472) and (posicion_click[1] > 473 and posicion_click[1] < 540):
                    print("A")
                    ingresar_nombre(puntaje_global)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


"""
Permite al jugador ingresar su nombre después de haber perdido. Guarda el nombre y el puntaje en algún lugar,
como un archivo de ranking.

Parameters:
- puntaje_global (int): El puntaje total del jugador.

Retorna:
- None
"""

def ingresar_nombre(puntaje_global):
    pantalla = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Guardar score")
    pygame.mixer.music.pause()
    fuente = pygame.font.SysFont("Arial", 26)
    nombre = " "
    textbox_width, textbox_height = 300, 32
    
    # Ajusta las posiciones para centrar verticalmente el rectángulo
    textbox_rect = pygame.Rect((pantalla.get_width() - textbox_width) // 2, (pantalla.get_height() - textbox_height) // 2, textbox_width, textbox_height)
    
    imagen_final = pygame.image.load("score.jpg")
    imagen_final = pygame.transform.scale(imagen_final, (800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.key == pygame.K_RETURN:
                    # Guardar el nombre y puntaje en el archivo ranking
                    insertar_jugadores(nombre, puntaje_global)
                    mostrar_menu()
                else:
                    if len(nombre) < 18:
                        nombre += event.unicode

        pantalla.blit(imagen_final, (0, 0))
        pygame.draw.rect(pantalla, (255,255,255), textbox_rect, 2)

        texto = fuente.render(nombre, True, (255,255,255))
        ingresar_nombre_texto = fuente.render("Ingresar nombre:", True, (255,255,255))
        
        # Ajusta la posición del texto "Ingresar nombre" para que aparezca arriba del rectángulo y comience desde el inicio del rectángulo
        y_offset = (textbox_rect.height - fuente.get_height()) // 2
        pantalla.blit(ingresar_nombre_texto, ((pantalla.get_width() - ingresar_nombre_texto.get_width()) // 2, textbox_rect.y - fuente.get_height() - y_offset))
        pantalla.blit(texto, (textbox_rect.x + 5, textbox_rect.y - 5))
        pygame.display.flip()


"""
Muestra una pantalla de ranking con los mejores puntajes alcanzados por los jugadores. Permite al jugador
ver la clasificación de los mejores jugadores.

Retorna:
- None
"""

def ranking():
    pantalla = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("RANKING")
    imagen_ranking = pygame.image.load("score.jpg")
    imagen_ranking = pygame.transform.scale(imagen_ranking, (800, 600))

    modo_ranking = True

    while modo_ranking:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    modo_ranking = False

        if not pygame.get_init():  # Verificar si pygame ha sido inicializado
            break

        pantalla.blit(imagen_ranking, (0, 0))
        lista_ranking = obtener_ranking()

        if lista_ranking is not None:
            fuente = pygame.font.SysFont("Arial", 36)
            color_fuente = (255, 255, 255)
            espacio_entre_elementos = 100  # Ajusta este valor según tus necesidades
            x = 100  # Ajusta la posición inicial en el eje x

            # Iterar solo sobre los primeros 5 elementos
            for i, (nombre, puntuacion) in enumerate(lista_ranking[:5]):
                y = 100 + i * espacio_entre_elementos  # Ajusta la posición en el eje y según necesites

                texto_puesto = f"{i + 1}. {nombre}"
                text_puesto = fuente.render(texto_puesto, True, color_fuente)
                pantalla.blit(text_puesto, (x, y))

                # Ajusta las coordenadas para centrar los nombres y mover los puntajes hacia la derecha
                x_puntajes =650
                text_puntuacion = fuente.render(str(puntuacion), True, color_fuente)
                pantalla.blit(text_puntuacion, (x_puntajes, y))

        pygame.display.flip()


"""
Muestra una pantalla indicando que el jugador ha ganado el juego. Permite al jugador ingresar su nombre
y guardar su puntuación.

Retorna:
- None
"""
    
def ganaste():
    pantalla = pygame.display.set_mode([800,600])
    pygame.display.set_caption("GANASTE")
    pygame.mixer.music.pause()
    sonido_ganaste = pygame.mixer.Sound("ganaste.mp3")
    sonido_ganaste.set_volume(0.4)
    imagen_ganaste = pygame.image.load("ganaste.png")
    imagen_ganaste = pygame.transform.scale(imagen_ganaste, (800, 600))
    pantalla.blit(imagen_ganaste, (0, 0))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(event.pos)
                print(posicion_click)
                if (posicion_click[0] > 288 and posicion_click[0] < 509) and (posicion_click[1] > 514 and posicion_click[1] < 574):
                    print("A")
                    ingresar_nombre(puntaje_global)
                    
"""
Muestra una pantalla con las instrucciones y reglas del juego. Permite al jugador entender cómo jugar
y qué objetivos alcanzar.

Retorna:
- None
"""

# Definición de la función para mostrar cómo jugar
def mostrar_como_jugar():
    pantalla = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Cómo Jugar")

    imagen_instrucciones = pygame.image.load("pantallainstrucciones.png")
    imagen_instrucciones = pygame.transform.scale(imagen_instrucciones, (800, 600))
    instrucciones = True
    
    while instrucciones:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instrucciones = False

        pantalla.fill((0, 0, 0))
        pantalla.blit(imagen_instrucciones, (0, 0))
        pygame.display.flip()
    

"""
Inicia el primer nivel del juego de carreras. Controla la lógica del juego, la interacción con el jugador,
y maneja eventos como colisiones y puntuaciones.

Retorna:
- None
"""

# Definición de la función para iniciar el nivel 1
def iniciar_nivel_1():
    pygame.init()
    global puntaje_global
    global vidas_global
    global nivel_1_completado
    pantalla = pygame.display.set_mode([1100, 440])
    pygame.display.set_caption("Carreras")

    imagen = pygame.image.load("Road.jpg")
    imagen = pygame.transform.scale(imagen, (400, 1100))
    imagen = pygame.transform.rotate(imagen, 90)
    pygame.mixer.music.load("fondo.mp3")
    pygame.mixer.music.play(-1)
    autos_enemigos = []  # Lista para gestionar autos enemigos
    auto_jugador = AutoJugador(19, 250, pantalla)
    auto_jugador.velocidad = 3  # Establece la velocidad del auto jugador
    imagen_explosion = pygame.image.load("choque_1_vida.png")
    imagen_explosion = pygame.transform.scale(imagen_explosion, (100, 100))
    sonido_explosion = pygame.mixer.Sound("explosion.mp3")
    sonido_explosion.set_volume(0.5)
    tiempo_explosion = 2000  # Duración de la explosión en milisegundos (1 segundo)
    # Definicion de las coordenadas 'y' para las posiciones de aparición de los autos
    coordenadas_y = [60, 250]
    puntaje_global = 0
    vidas_global = 3
    autos_enemigos_cruzados = 0
    bandera_correr = True
    autos_adelantados = {}
    tiempo_aparicion = 0  # Inicializacion del temporizador para la aparición de nuevos autos
    velocidad_auto = 3  # Velocidad de los autos enemigos
    autos_a_aparecer = 7  # Cantidad de autos a aparecer
    distancia_entre_autos = 3500  # Espacio entre autos enemigos
    
    # Defincion de variables de estado para las teclas
    tecla_arriba_presionada = False
    tecla_abajo_presionada = False
    tecla_derecha_presionada = False
    tecla_izquierda_presionada = False
    
    velocidad_maxima = 5
    velocidad_actual = 0  
    velocidad_aceleracion = 0.1  # Cuánto aumenta la velocidad con cada cuadro
    velocidad_frenado = 0.1  # Cuánto disminuye la velocidad al soltar la tecla de acelerar

    # Definicion de una variable para controlar la visualización de la imagen "Nivel Completado"
    mostrar_imagen_nivel_completado_flag = False
    pausado = False
    colision = False
    nivel_1_completado = False
    todos_autos_cruzados = False
    while bandera_correr:
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                bandera_correr = False
        # Procesar eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                auto_jugador.presionando_arriba = True
            if event.key == pygame.K_DOWN:
                auto_jugador.presionando_abajo = True
            if event.key == pygame.K_RIGHT:
                auto_jugador.presionando_derecha = True
            if event.key == pygame.K_LEFT:
                auto_jugador.presionando_izquierda = True
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pausado = not pausado
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                auto_jugador.presionando_arriba = False
            if event.key == pygame.K_DOWN:
                auto_jugador.presionando_abajo = False
            if event.key == pygame.K_RIGHT:
                auto_jugador.presionando_derecha = False
            if event.key == pygame.K_LEFT:
                auto_jugador.presionando_izquierda = False
        """ if pausado:      
            juego_en_pausa()
        else: """
            # Lista de autos enemigos a eliminar
        autos_a_eliminar = []

        for i, auto_enemigo in enumerate(autos_enemigos):
            if auto_jugador.rect_jugador.colliderect(auto_enemigo.rect_enemigo):
                vidas_global -= 1  # Reduce una vida
                #vidas_restantes = vidas
                pygame.mixer.music.pause()
                sonido_explosion.play()
                # Muestra la imagen de choque
                x = auto_enemigo.rect_enemigo.centerx - imagen_explosion.get_width() // 2
                y = auto_enemigo.rect_enemigo.centery - imagen_explosion.get_height() // 2
                pantalla.blit(imagen_explosion, (x, y))
                pygame.display.flip()
                pygame.time.delay(tiempo_explosion)  # Pausa el juego para mostrar la explosión
                autos_a_eliminar.append(i)  # Agrega el auto enemigo a la lista de eliminación
                puntaje_global -= 10  # Descuenta 10 puntos por colisión
        pygame.mixer.music.unpause()        
        # Elimina autos enemigos que colisionaron
        autos_enemigos = [auto for i, auto in enumerate(autos_enemigos) if i not in autos_a_eliminar]

        
        for auto_enemigo in autos_enemigos:
            if not colision and auto_jugador.rect_jugador.colliderect(auto_enemigo.rect_enemigo):
                colision = True
        
        if vidas_global <= 0:
            mostrar_game_over(pantalla, puntaje_global)
            pygame.quit()
            sys.exit()
            
        #Verifca si sobrepasa a un auto enemigo
        for auto_enemigo in autos_enemigos:
            if not autos_adelantados.get(auto_enemigo, False) and auto_enemigo.rect_enemigo.left + auto_enemigo.rect_enemigo.width < auto_jugador.rect_jugador.left:
                puntaje_global += 20  # Suma 20 puntos por sobrepasar totalmente al auto enemigo
                autos_adelantados[auto_enemigo] = True  # Marca el auto enemigo como adelantado      
                

        

        # Actualizar el auto jugador
        auto_jugador.actualizar()

        pantalla.fill((0, 0, 0))
        pantalla.blit(imagen, (0, 0))
        
        # Dibuja el puntaje y la cantidad de vidas
        fuente = pygame.font.Font(None, 36)
        texto_puntaje = fuente.render(f"Puntaje: {puntaje_global}", True, (255, 255, 255))
        texto_vidas = fuente.render(f"Vidas: {vidas_global}", True, (255, 255, 255))
        pantalla.blit(texto_puntaje, (10, 410))
        pantalla.blit(texto_vidas, (500, 410))

        # Control de la velocidad
        if tecla_derecha_presionada and velocidad_actual < velocidad_maxima:
            velocidad_actual += velocidad_aceleracion
        if not tecla_derecha_presionada:
            velocidad_actual -= velocidad_frenado
        if velocidad_actual < 0:
            velocidad_actual = 0

        # Control de movimiento
        if tecla_arriba_presionada and auto_jugador.rect.top > 0:
            auto_jugador.mover_arriba(velocidad_actual)
        if tecla_abajo_presionada and auto_jugador.rect.bottom < imagen.get_height():  # Limita el movimiento al alto de la imagen del camino
            auto_jugador.mover_abajo(velocidad_actual)

        if tiempo_aparicion == 0 and autos_enemigos_cruzados < autos_a_aparecer:
            tiempo_aparicion = pygame.time.get_ticks()
            nueva_y = coordenadas_y[autos_enemigos_cruzados % len(coordenadas_y)]
            nuevo_auto = AutoEnemigo(1090, nueva_y, velocidad_auto)
            autos_enemigos.append(nuevo_auto)
            autos_enemigos_cruzados += 1
            if autos_enemigos_cruzados == autos_a_aparecer:
                todos_autos_cruzados = True
            
        # Restablece el temporizador cuando un auto ha cruzado cierta posición
        if tiempo_aparicion > 0 and pygame.time.get_ticks() - tiempo_aparicion > distancia_entre_autos:
            tiempo_aparicion = 0
            
        # Dibuja el auto jugador solo si está dentro de los límites de la ventana
        if 0 <= auto_jugador.rect_jugador.top <= pantalla.get_height():
            auto_jugador.dibujar()
        
        # Elimina los autos que han cruzado cierta posición (cuando están completamente fuera de la pantalla)
        autos_enemigos = [auto for auto in autos_enemigos if auto.x < pantalla.get_width()]

        # Mueve y dibuja los autos enemigos
        autos_a_eliminar = []  # Lista de autos que han llegado al borde de la ventana o han colisionado
        for i, auto_enemigo in enumerate(autos_enemigos):
            auto_enemigo.mover()
            auto_enemigo.dibujar(pantalla)

            # Comprueba si el auto ha cruzado las coordenadas [0, 300]
            if auto_enemigo.x < 0 - auto_enemigo.rect_enemigo.width:
                autos_a_eliminar.append(i) 
        
        autos_enemigos = [auto for i, auto in enumerate(autos_enemigos) if i not in autos_a_eliminar]
        # Mueve y dibuja el auto jugador
        auto_jugador.dibujar()

        if todos_autos_cruzados:
            mostrar_imagen_nivel_completado_flag = True

        if mostrar_imagen_nivel_completado_flag and len(autos_enemigos) == 0:
            pygame.mixer.music.pause()
            mostrar_imagen_nivel_completado(pantalla)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mostrar_imagen_nivel_completado_flag = False
                    nivel_1_completado = True
        pygame.display.flip()
    pygame.mixer.music.stop()
    mostrar_menu()  # Regresar al menú principal al salir del juego


"""
Inicia el segundo nivel del juego de carreras. Controla la lógica del juego, la interacción con el jugador,
y maneja eventos como colisiones y puntuaciones.

Retorna:
- None
"""
# Definición de la función para iniciar el nivel 2
def iniciar_nivel_2():
    pygame.init()
    global puntaje_global
    global vidas_global
    global nivel_2_completado
    pantalla = pygame.display.set_mode([1100, 440])
    pygame.display.set_caption("Carreras")

    imagen = pygame.image.load("Road.jpg")
    imagen = pygame.transform.scale(imagen, (400, 1100))
    imagen = pygame.transform.rotate(imagen, 90)
    pygame.mixer.music.load("fondo.mp3")
    pygame.mixer.music.play(-1)
    autos_enemigos = []  # Lista para gestionar autos enemigos
    auto_jugador = AutoJugador(19, 250, pantalla)
    auto_jugador.velocidad = 4  # Establece la velocidad del auto jugador
    imagen_explosion = pygame.image.load("choque_1_vida.png")
    imagen_explosion = pygame.transform.scale(imagen_explosion, (100, 100))
    sonido_explosion = pygame.mixer.Sound("explosion.mp3")
    sonido_explosion.set_volume(0.5)
    tiempo_explosion = 2000  # Duración de la explosión en milisegundos (2 segundos)
    # Definicion de las coordenadas 'y' para las posiciones de aparición de los autos
    coordenadas_y = [60, 250]
    autos_enemigos_cruzados = 0
    bandera_correr = True
    autos_adelantados = {}
    tiempo_aparicion = 0  # Inicializacion del temporizador para la aparición de nuevos autos
    velocidad_auto = 4  # Velocidad de los autos enemigos
    autos_a_aparecer = 10  # Cantidad de autos a aparecer
    distancia_entre_autos = 2500  # Espacio entre autos enemigos

    # Defincion de variables de estado para las teclas
    tecla_arriba_presionada = False
    tecla_abajo_presionada = False
    tecla_derecha_presionada = False
    tecla_izquierda_presionada = False
    
    velocidad_maxima = 5
    velocidad_actual = 0  
    velocidad_aceleracion = 0.1  # Cuánto aumenta la velocidad con cada cuadro
    velocidad_frenado = 0.1  # Cuánto disminuye la velocidad al soltar la tecla de acelerar

    # Definicion de una variable para controlar la visualización de la imagen "Nivel Completado"
    mostrar_imagen_nivel_completado_flag = False
    nivel_2_completado = False
    pausado = False
    colision = False
    todos_autos_cruzados = False
    while bandera_correr:
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                bandera_correr = False
        # Procesar eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                auto_jugador.presionando_arriba = True
            if event.key == pygame.K_DOWN:
                auto_jugador.presionando_abajo = True
            if event.key == pygame.K_RIGHT:
                auto_jugador.presionando_derecha = True
            if event.key == pygame.K_LEFT:
                auto_jugador.presionando_izquierda = True
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pausado = not pausado
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                auto_jugador.presionando_arriba = False
            if event.key == pygame.K_DOWN:
                auto_jugador.presionando_abajo = False
            if event.key == pygame.K_RIGHT:
                auto_jugador.presionando_derecha = False
            if event.key == pygame.K_LEFT:
                auto_jugador.presionando_izquierda = False
                
        autos_a_eliminar = []

        for i, auto_enemigo in enumerate(autos_enemigos):
            if auto_jugador.rect_jugador.colliderect(auto_enemigo.rect_enemigo):
                vidas_global -= 1  # Reduce una vida
                pygame.mixer.music.pause()
                sonido_explosion.play()
                # Muestra la imagen de choque
                x = auto_enemigo.rect_enemigo.centerx - imagen_explosion.get_width() // 2
                y = auto_enemigo.rect_enemigo.centery - imagen_explosion.get_height() // 2
                pantalla.blit(imagen_explosion, (x, y))
                pygame.display.flip()
                pygame.time.delay(tiempo_explosion)  # Pausa el juego para mostrar la explosión
                autos_a_eliminar.append(i)  # Agrega el auto enemigo a la lista de eliminación
                puntaje_global -= 10  # Descuenta 10 puntos por colisión
        pygame.mixer.music.unpause()        
        # Elimina autos enemigos que colisionaron
        autos_enemigos = [auto for i, auto in enumerate(autos_enemigos) if i not in autos_a_eliminar]

        
        for auto_enemigo in autos_enemigos:
            if not colision and auto_jugador.rect_jugador.colliderect(auto_enemigo.rect_enemigo):
                colision = True
        
            if vidas_global <= 0:
                mostrar_game_over(pantalla, puntaje_global)
                pygame.quit()
                sys.exit()
            
        #Verifca si sobrepasa a un auto enemigo
        for auto_enemigo in autos_enemigos:
            if not autos_adelantados.get(auto_enemigo, False) and auto_enemigo.rect_enemigo.left + auto_enemigo.rect_enemigo.width < auto_jugador.rect_jugador.left:
                puntaje_global += 20  # Suma 20 puntos por sobrepasar totalmente al auto enemigo
                autos_adelantados[auto_enemigo] = True  # Marca el auto enemigo como adelantado      
                


        # Actualizar el auto jugador
        auto_jugador.actualizar()

        pantalla.fill((0, 0, 0))
        pantalla.blit(imagen, (0, 0))
        
        # Dibuja el puntaje y la cantidad de vidas
        fuente = pygame.font.Font(None, 36)
        texto_puntaje = fuente.render(f"Puntaje: {puntaje_global}", True, (255, 255, 255))
        texto_vidas = fuente.render(f"Vidas: {vidas_global}", True, (255, 255, 255))
        pantalla.blit(texto_puntaje, (10, 410))
        pantalla.blit(texto_vidas, (500, 410))

        # Control de la velocidad
        if tecla_derecha_presionada and velocidad_actual < velocidad_maxima:
            velocidad_actual += velocidad_aceleracion
        if not tecla_derecha_presionada:
            velocidad_actual -= velocidad_frenado
        if velocidad_actual < 0:
            velocidad_actual = 0

        # Control de movimiento
        if tecla_arriba_presionada and auto_jugador.rect.top > 0:
            auto_jugador.mover_arriba(velocidad_actual)
        if tecla_abajo_presionada and auto_jugador.rect.bottom < imagen.get_height():  # Limita el movimiento al alto de la imagen del camino
            auto_jugador.mover_abajo(velocidad_actual)

        if tiempo_aparicion == 0 and autos_enemigos_cruzados < autos_a_aparecer:
            tiempo_aparicion = pygame.time.get_ticks()
            nueva_y = coordenadas_y[autos_enemigos_cruzados % len(coordenadas_y)]
            nuevo_auto = AutoEnemigo2(1090, nueva_y, velocidad_auto)
            autos_enemigos.append(nuevo_auto)
            autos_enemigos_cruzados += 1
            if autos_enemigos_cruzados == autos_a_aparecer:
                todos_autos_cruzados = True
            
        # Restablece el temporizador cuando un auto ha cruzado cierta posición
        if tiempo_aparicion > 0 and pygame.time.get_ticks() - tiempo_aparicion > distancia_entre_autos:
            tiempo_aparicion = 0
            
        # Dibuja el auto jugador solo si está dentro de los límites de la ventana
        if 0 <= auto_jugador.rect_jugador.top <= pantalla.get_height():
            auto_jugador.dibujar()
        
        # Elimina los autos que han cruzado cierta posición (cuando están completamente fuera de la pantalla)
        autos_enemigos = [auto for auto in autos_enemigos if auto.x < pantalla.get_width()]

        # Mueve y dibuja los autos enemigos
        autos_a_eliminar = []  # Lista de autos que han llegado al borde de la ventana o han colisionado
        for i, auto_enemigo in enumerate(autos_enemigos):
            auto_enemigo.mover()
            auto_enemigo.dibujar(pantalla)

            # Comprueba si el auto ha cruzado las coordenadas [0, 300]
            if auto_enemigo.x < 0 - auto_enemigo.rect_enemigo.width:
                autos_a_eliminar.append(i) 
        
        autos_enemigos = [auto for i, auto in enumerate(autos_enemigos) if i not in autos_a_eliminar]
        # Mueve y dibuja el auto jugador
        auto_jugador.dibujar()

        if todos_autos_cruzados:
            mostrar_imagen_nivel_completado_flag = True

        if mostrar_imagen_nivel_completado_flag and len(autos_enemigos) == 0:
            pygame.mixer.music.pause()
            mostrar_imagen_nivel_completado(pantalla)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mostrar_imagen_nivel_completado_flag = False
                    nivel_2_completado = True
                    
        pygame.display.flip()
        
"""
Inicia el tercer nivel del juego de carreras. Controla la lógica del juego, la interacción con el jugador,
y maneja eventos como colisiones y puntuaciones.

Retorna:
- None
"""       
# Definición de la función para iniciar el nivel 3
def iniciar_nivel_3():
    pygame.init()
    global puntaje_global
    global vidas_global
    pantalla = pygame.display.set_mode([1100, 440])
    pygame.display.set_caption("Carreras")

    imagen = pygame.image.load("Road.jpg")
    imagen = pygame.transform.scale(imagen, (400, 1100))
    imagen = pygame.transform.rotate(imagen, 90)
    pygame.mixer.music.load("fondo.mp3")
    pygame.mixer.music.play(-1)
    autos_enemigos = []  # Lista para gestionar autos enemigos
    auto_jugador = AutoJugador(19, 250, pantalla)
    auto_jugador.velocidad = 4  # Establece la velocidad del auto jugador
    imagen_explosion = pygame.image.load("choque_1_vida.png")
    imagen_explosion = pygame.transform.scale(imagen_explosion, (100, 100))
    sonido_explosion = pygame.mixer.Sound("explosion.mp3")
    sonido_explosion.set_volume(0.5)
    tiempo_explosion = 2000  # Duración de la explosión en milisegundos (2 segundos)
    # Definicion de las coordenadas 'y' para las posiciones de aparición de los autos
    coordenadas_y = [60, 250]
    autos_enemigos_cruzados = 0
    bandera_correr = True
    autos_adelantados = {}
    tiempo_aparicion = 0  # Inicializacion del temporizador para la aparición de nuevos autos
    velocidad_auto = 5  # Velocidad de los autos enemigos
    autos_a_aparecer = 15  # Cantidad de autos a aparecer
    distancia_entre_autos = 1500  # Espacio entre autos enemigos

    # Defincion de variables de estado para las teclas
    tecla_arriba_presionada = False
    tecla_abajo_presionada = False
    tecla_derecha_presionada = False
    tecla_izquierda_presionada = False
    
    velocidad_maxima = 5
    velocidad_actual = 0  
    velocidad_aceleracion = 0.1  # Cuánto aumenta la velocidad con cada cuadro
    velocidad_frenado = 0.1  # Cuánto disminuye la velocidad al soltar la tecla de acelerar

    # Definicion de una variable para controlar la visualización de la imagen "Nivel Completado"
    mostrar_imagen_nivel_completado_flag = False
    pausado = False
    colision = False
    todos_autos_cruzados = False
    while bandera_correr:
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                bandera_correr = False
        # Procesar eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                auto_jugador.presionando_arriba = True
            if event.key == pygame.K_DOWN:
                auto_jugador.presionando_abajo = True
            if event.key == pygame.K_RIGHT:
                auto_jugador.presionando_derecha = True
            if event.key == pygame.K_LEFT:
                auto_jugador.presionando_izquierda = True
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pausado = not pausado
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                auto_jugador.presionando_arriba = False
            if event.key == pygame.K_DOWN:
                auto_jugador.presionando_abajo = False
            if event.key == pygame.K_RIGHT:
                auto_jugador.presionando_derecha = False
            if event.key == pygame.K_LEFT:
                auto_jugador.presionando_izquierda = False
                
        autos_a_eliminar = []

        for i, auto_enemigo in enumerate(autos_enemigos):
            if auto_jugador.rect_jugador.colliderect(auto_enemigo.rect_enemigo):
                vidas_global -= 1  # Reduce una vida
                pygame.mixer.music.pause()
                sonido_explosion.play()
                # Muestra la imagen de choque
                x = auto_enemigo.rect_enemigo.centerx - imagen_explosion.get_width() // 2
                y = auto_enemigo.rect_enemigo.centery - imagen_explosion.get_height() // 2
                pantalla.blit(imagen_explosion, (x, y))
                pygame.display.flip()
                pygame.time.delay(tiempo_explosion)  # Pausa el juego para mostrar la explosión
                autos_a_eliminar.append(i)  # Agrega el auto enemigo a la lista de eliminación
                puntaje_global -= 10  # Descuenta 10 puntos por colisión
        pygame.mixer.music.unpause()        
        # Elimina autos enemigos que colisionaron
        autos_enemigos = [auto for i, auto in enumerate(autos_enemigos) if i not in autos_a_eliminar]

        
        for auto_enemigo in autos_enemigos:
            if not colision and auto_jugador.rect_jugador.colliderect(auto_enemigo.rect_enemigo):
                colision = True
        
        if vidas_global <= 0:
            mostrar_game_over(pantalla, puntaje_global)
            pygame.quit()
            sys.exit()
            
        #Verifca si sobrepasa a un auto enemigo
        for auto_enemigo in autos_enemigos:
            if not autos_adelantados.get(auto_enemigo, False) and auto_enemigo.rect_enemigo.left + auto_enemigo.rect_enemigo.width < auto_jugador.rect_jugador.left:
                puntaje_global += 20  # Suma 20 puntos por sobrepasar totalmente al auto enemigo
                autos_adelantados[auto_enemigo] = True  # Marca el auto enemigo como adelantado      
                


        # Actualizar el auto jugador
        auto_jugador.actualizar()

        pantalla.fill((0, 0, 0))
        pantalla.blit(imagen, (0, 0))
        
        # Dibuja el puntaje y la cantidad de vidas
        fuente = pygame.font.Font(None, 36)
        texto_puntaje = fuente.render(f"Puntaje: {puntaje_global}", True, (255, 255, 255))
        texto_vidas = fuente.render(f"Vidas: {vidas_global}", True, (255, 255, 255))
        pantalla.blit(texto_puntaje, (10, 410))
        pantalla.blit(texto_vidas, (500, 410))

        # Control de la velocidad
        if tecla_derecha_presionada and velocidad_actual < velocidad_maxima:
            velocidad_actual += velocidad_aceleracion
        if not tecla_derecha_presionada:
            velocidad_actual -= velocidad_frenado
        if velocidad_actual < 0:
            velocidad_actual = 0

        # Control de movimiento
        if tecla_arriba_presionada and auto_jugador.rect.top > 0:
            auto_jugador.mover_arriba(velocidad_actual)
        if tecla_abajo_presionada and auto_jugador.rect.bottom < imagen.get_height():  # Limita el movimiento al alto de la imagen del camino
            auto_jugador.mover_abajo(velocidad_actual)

        if tiempo_aparicion == 0 and autos_enemigos_cruzados < autos_a_aparecer:
            tiempo_aparicion = pygame.time.get_ticks()
            nueva_y = coordenadas_y[autos_enemigos_cruzados % len(coordenadas_y)]
            nuevo_auto = AutoEnemigo3(1090, nueva_y, velocidad_auto)
            autos_enemigos.append(nuevo_auto)
            autos_enemigos_cruzados += 1
            if autos_enemigos_cruzados == autos_a_aparecer:
                todos_autos_cruzados = True
            
        # Restablece el temporizador cuando un auto ha cruzado cierta posición
        if tiempo_aparicion > 0 and pygame.time.get_ticks() - tiempo_aparicion > distancia_entre_autos:
            tiempo_aparicion = 0
            
        # Dibuja el auto jugador solo si está dentro de los límites de la ventana
        if 0 <= auto_jugador.rect_jugador.top <= pantalla.get_height():
            auto_jugador.dibujar()
        
        # Elimina los autos que han cruzado cierta posición (cuando están completamente fuera de la pantalla)
        autos_enemigos = [auto for auto in autos_enemigos if auto.x < pantalla.get_width()]

        # Mueve y dibuja los autos enemigos
        autos_a_eliminar = []  # Lista de autos que han llegado al borde de la ventana o han colisionado
        for i, auto_enemigo in enumerate(autos_enemigos):
            auto_enemigo.mover()
            auto_enemigo.dibujar(pantalla)

            # Comprueba si el auto ha cruzado las coordenadas [0, 300]
            if auto_enemigo.x < 0 - auto_enemigo.rect_enemigo.width:
                autos_a_eliminar.append(i) 
        
        autos_enemigos = [auto for i, auto in enumerate(autos_enemigos) if i not in autos_a_eliminar]
        # Mueve y dibuja el auto jugador
        auto_jugador.dibujar()

        if todos_autos_cruzados:
            mostrar_imagen_nivel_completado_flag = True

        if mostrar_imagen_nivel_completado_flag and len(autos_enemigos) == 0:
            pygame.mixer.music.pause()
            mostrar_imagen_nivel_completado(pantalla)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mostrar_imagen_nivel_completado_flag = False
                    
        pygame.display.flip()

pygame.quit()