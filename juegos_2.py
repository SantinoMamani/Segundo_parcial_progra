import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO, ALTO = 800, 600

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Clase para representar el automóvil del jugador
class AutoJugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 20
        self.velocidad = 5

    def mover_izquierda(self):
        self.rect.x -= self.velocidad

    def mover_derecha(self):
        self.rect.x += self.velocidad

# Clase para representar los autos enemigos
class AutoEnemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - 50)
        self.rect.y = random.randint(-ALTO, -80)
        self.velocidad = random.randint(1, 5)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.y > ALTO:
            self.rect.y = random.randint(-ALTO, -80)
            self.rect.x = random.randint(0, ANCHO - 50)

# Inicialización de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Autos en la Autopista")

# Crear objetos
jugador = AutoJugador()
autos_enemigos = pygame.sprite.Group()

for _ in range(100):  # Crear 5 autos enemigos
    auto_enemigo = AutoEnemigo()
    autos_enemigos.add(auto_enemigo)

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Función para mostrar la puntuación en la pantalla
fuente = pygame.font.Font(None, 36)
def mostrar_puntuacion(puntuacion):
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (0,0,0))
    pantalla.blit(texto, (10, 10))

# Función para manejar colisiones
def colisiones():
    colisiones = pygame.sprite.spritecollide(jugador, autos_enemigos, True)
    return colisiones       

# Bucle principal del juego
puntuacion = 0
en_ejecucion = True
while en_ejecucion:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_ejecucion = False

    # Mover el automóvil del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.mover_izquierda()
    if teclas[pygame.K_RIGHT]:
        jugador.mover_derecha()

    # Actualizar los autos enemigos
    autos_enemigos.update()

    # Comprobar colisiones
    colisiones_actuales = colisiones()
    puntuacion += len(colisiones_actuales)
    # Mostrar la puntuación
    mostrar_puntuacion(puntuacion)


    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar objetos
    pantalla.blit(jugador.image, jugador.rect)
    autos_enemigos.draw(pantalla)

    # Mostrar la puntuación
    mostrar_puntuacion(puntuacion)

    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(60)

# Finalizar Pygame
pygame.quit()
