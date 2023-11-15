import pygame
import random

class AutoEnemigo:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagenes_autos = ["auto_amarillo.png", "auto_azul.png", "auto_naranja.png", "auto_negro.png", "auto_rojo.png", "auto_verde.png", "auto_violeta.png"]
        self.imagen = pygame.image.load(random.choice(self.imagenes_autos))
        self.imagen = pygame.transform.rotate(self.imagen, 90)
        self.rect_enemigo = self.imagen.get_rect()
        self.rect_enemigo.topleft = (x, y)
        self.tiempo_movimiento = 0  # Inicializa el temporizador
    
    def mover(self):
        # Controla el movimiento usando un temporizador
        if pygame.time.get_ticks() - self.tiempo_movimiento > 20:  # Ajusta el valor para la velocidad deseada
            self.x -= self.velocidad
            self.tiempo_movimiento = pygame.time.get_ticks()  # Restablece el temporizador
            self.rect_enemigo.x = self.x  # Actualiza la posición del rectángulo
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect_enemigo.topleft)

class Movimiento:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad

    def mover_arriba(self):
        self.y -= self.velocidad

    def mover_abajo(self):
        self.y += self.velocidad

    def acelerar(self):
        self.velocidad += 1

    def reducir_velocidad(self):
        self.velocidad -= 1

class AutoEnemigo2:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagenes_autos = ["auto_amarillo.png", "auto_azul.png", "auto_naranja.png", "auto_negro.png", "auto_rojo.png", "auto_verde.png", "auto_violeta.png", "agujero.png", "roca.png",]
        self.imagen = pygame.image.load(random.choice(self.imagenes_autos))
        self.imagen = pygame.transform.rotate(self.imagen, 90)
        self.rect_enemigo = self.imagen.get_rect()
        self.rect_enemigo.topleft = (x, y)
        self.tiempo_movimiento = 0  # Inicializa el temporizador
    
    def mover(self):
        # Controla el movimiento usando un temporizador
        if pygame.time.get_ticks() - self.tiempo_movimiento > 15:
            self.x -= self.velocidad
            self.tiempo_movimiento = pygame.time.get_ticks()  # Restablece el temporizador
            self.rect_enemigo.x = self.x  # Actualiza la posición del rectángulo
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect_enemigo.topleft)
    def update(self):
        self.rect.x -= 5  # Mueve el auto hacia la izquierda

class AutoEnemigo3:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagenes_autos = ["auto_amarillo.png", "auto_azul.png", "auto_naranja.png", "auto_negro.png", "auto_rojo.png", "auto_verde.png", "auto_violeta.png", "agujero.png", "roca.png", "cactus.png"]
        self.imagen = pygame.image.load(random.choice(self.imagenes_autos))
        self.imagen = pygame.transform.rotate(self.imagen, 90)
        self.rect_enemigo = self.imagen.get_rect()
        self.rect_enemigo.topleft = (x, y)
        self.tiempo_movimiento = 0  # Inicializa el temporizador
    
    def mover(self):
        # Controla el movimiento usando un temporizador
        if pygame.time.get_ticks() - self.tiempo_movimiento > 10:
            self.x -= self.velocidad
            self.tiempo_movimiento = pygame.time.get_ticks()  # Restablece el temporizador
            self.rect_enemigo.x = self.x  # Actualiza la posición del rectángulo
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect_enemigo.topleft)
    def update(self):
        self.rect.x -= 5  # Mueve el auto hacia la izquierda


class AutoJugador(pygame.sprite.Sprite):
    def __init__(self, x, y, pantalla):
        super().__init__()
        self.x = x
        self.y = y
        self.velocidad = 0
        self.velocidad_maxima = 5  # Agrega la velocidad máxima
        self.presionando_arriba = False
        self.presionando_abajo = False
        self.presionando_derecha = False
        self.presionando_izquierda = False
        self.image = pygame.image.load("auto_principal.png")
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect_jugador = self.image.get_rect()
        self.rect_jugador.topleft = (self.x, self.y)
        self.pantalla = pantalla  # Establecer la pantalla como una propiedad
        
    def dibujar(self):
        self.pantalla.blit(self.image, self.rect_jugador.topleft)  # Dibuja solo la imagen del auto

    def mover_arriba(self):
        self.rect_jugador.y -= self.velocidad * 0.15  # Modifica el valor (0.1) según tus preferencias
        if self.rect_jugador.y < 0:
            self.rect_jugador.y = 0  # Limitar la posición superior
            self.rectangulo = self.rect_jugador

    def mover_abajo(self):
        self.rect_jugador.y += self.velocidad * 0.15
        # Limita la posición inferior al límite de la imagen "road.png"
        if self.rect_jugador.bottom > 400:
            self.rect_jugador.bottom = 400

        self.rectangulo = self.rect_jugador

    def mover_izquierda(self, velocidad):
        self.rect_jugador.x -= velocidad
        self.rectangulo = self.rect_jugador

    def mover_derecha(self, velocidad):
        self.rect_jugador.x += velocidad
        self.rectangulo = self.rect_jugador

    def acelerar(self):
        if self.velocidad < self.velocidad_maxima:
            self.velocidad += 5.5  # Incremento más suave para una aceleración gradual

    def reducir_velocidad(self):
        if self.velocidad > 0:
            self.velocidad -= 0.2  # Reducción gradual de la velocidad

    def actualizar(self):
        if self.presionando_derecha:
            self.acelerar()
        elif self.presionando_izquierda:
            self.reducir_velocidad()
        if self.presionando_arriba:
            self.mover_arriba()
        if self.presionando_abajo:
            self.mover_abajo()
            
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5






