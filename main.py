import pgzrun
import math
#import random

# Configurações da Janela
WIDTH = 800
HEIGHT = 600
TITLE = "Teste de Plataforma"

# Variáveis do Jogador 
player_x = 400
player_y = 300

# Definições do player
player = Rect((100, 450), (40, 40))# Rect((x, y), (largura, altura))
vel_y = 0# Velocidade vertical (gravidade)
vel_x = 0
player_color = "red"

ACCEL = 0.8    # Aceleração (math ajuda na suavidade)
FRICTION = 0.9 # Atrito para o personagem não parar do nada
GRAVITY = 0.5
JUMP_FORCE = -15

vel_y = 0  
no_chao = False

# Lista de Obstáculos (Chão e Paredes)
plataformas = [
    Rect((0, 550), (800, 50)),   # Chão principal
    Rect((300, 400), (200, 20)), # Plataforma flutuante
    Rect((100, 300), (150, 20)), # Outra plataforma
    Rect((550, 250), (100, 20)), # Obstáculo pequeno
   # Rect((700, 0), (20, 550)),    # Uma parede na direita
    Rect((0, 0), (20, 550))    # Uma parede na esquerda
]

# Configuração do Chão
chao = Rect((0, 550), (800, 50))

#Detahes da tela
def draw():
    screen.clear()
    screen.fill((135, 206, 235)) # Céu azul
    
    # Desenha o jogador
    screen.draw.filled_rect(player, "red")
    
    for plat in plataformas:
        screen.draw.filled_rect(plat, "gray")
    

def update():
    global vel_y, vel_x

    # --- MOVIMENTAÇÃO HORIZONTAL ---
    if keyboard.left:
        vel_x -= ACCEL
    elif keyboard.right:
        vel_x += ACCEL
    
    vel_x *= FRICTION # Aplica o atrito
    player.x += vel_x

    # Checar colisão horizontal (Paredes)
    for plat in plataformas:

        if player.colliderect(plat):
            if vel_x > 0: # Indo para direita
                player.right = plat.left
                vel_x = 0
            elif vel_x < 0: # Indo para esquerda
                player.left = plat.right
                vel_x = 0

    # MOVIMENTAÇÃO VERTICAL (GRAVIDADE)  
    vel_y += GRAVITY
    player.y += vel_y
    
    # Checar colisão vertical (Chão e Teto)
    no_chao = False
    for plat in plataformas:
        if player.colliderect(plat):
            if vel_y > 0: # Caindo
                player.bottom = plat.top
                vel_y = 0
                no_chao = True
            elif vel_y < 0: # Batendo a cabeça
                player.top = plat.bottom
                vel_y = 0

    # Pulo
    if keyboard.space and no_chao:
        vel_y = JUMP_FORCE

pgzrun.go()