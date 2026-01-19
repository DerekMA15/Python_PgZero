import pgzrun
import math
import random
import pygame
from menu import JogoMenu

# Configurações
WIDTH = 800
HEIGHT = 600
MAP_WIDTH = 5000  # Tamanho total da fase
TITLE = "Plataforma Pro - Nível 1"

# Inicialização
menu = JogoMenu()
player = Rect((100, 450), (30, 40))
player_color = "orange"
vel_y = 0
vel_x = 0
scroll_x = 0
moedas_coletadas = 0

# Física
GRAVITY = 0.5
ACCEL = 0.7
FRICTION = 0.85

# Plataformas (Espalhadas por 5000 pixels)
plataformas = [
    Rect((0, 550), (600, 50)),
    Rect((700, 450), (300, 20)),
    Rect((1100, 350), (400, 20)),
    Rect((1700, 450), (300, 20)),
    Rect((2100, 550), (1000, 50)),
    Rect((3200, 400), (400, 20)),
    Rect((3800, 300), (500, 20)),
    Rect((4500, 500), (500, 50))
]

# Moedas (Retângulos amarelos)
moedas = [
    Rect((1200, 310), (20, 20)),
    Rect((2500, 510), (20, 20)),
    Rect((4800, 460), (20, 20))
]

# Inimigos (Lista de dicionários para facilitar)
inimigos = [
    {"rect": Rect((800, 410), (30, 40)), "dir": 1, "limite": (700, 1000)},
    {"rect": Rect((2200, 510), (30, 40)), "dir": 1, "limite": (2100, 3100)},
    {"rect": Rect((3900, 260), (30, 40)), "dir": 1, "limite": (3800, 4300)}
]

# Iniciar Música
try:
    music.play('tema')
    music.set_volume(0.4) # Volume mais baixo para não abafar os sons
except:
    print("Erro: Arquivo music/tema.mp3 não encontrado.")


def draw():
    screen.clear()
    
    if menu.ativo:
        menu.draw(screen, WIDTH, HEIGHT)
        return

    screen.fill((10, 10, 20)) # Fundo do jogo

    # Desenhar Plataformas com Scroll
    for plat in plataformas:
        screen.draw.filled_rect(Rect((plat.x - scroll_x, plat.y), (plat.width, plat.height)), (80, 80, 100))

    # Desenhar Moedas com efeito de brilho (math)
    for m in moedas:
        brilho = abs(math.sin(pygame.time.get_ticks() * 0.01)) * 5
        m_visual = Rect((m.x - scroll_x - brilho/2, m.y - brilho/2), (m.width + brilho, m.height + brilho))
        screen.draw.filled_rect(m_visual, "yellow")

    # Desenhar Inimigos
    for ene in inimigos:
        screen.draw.filled_rect(Rect((ene["rect"].x - scroll_x, ene["rect"].y), (30, 40)), "red")

    # Desenhar Player
    screen.draw.filled_rect(Rect((player.x - scroll_x, player.y), (player.width, player.height)), player_color)

    # HUD Lateral Fixa
    screen.draw.filled_rect(Rect((WIDTH - 180, 20), (160, 60)), (0, 0, 0, 150)) # Fundo
    screen.draw.text(f"{moedas_coletadas}/3", (WIDTH - 170, 35), fontsize=40, bold=True, color="white")
    # O quadradinho amarelo da moeda ao lado do texto
    screen.draw.filled_rect(Rect((WIDTH - 60, 35), (20, 20)), "yellow")

def update():
    global vel_x, vel_y, scroll_x, moedas_coletadas, player_color

    if menu.ativo:
        menu.update(keyboard) # Passando o objeto keyboard para a classe
        return
    
    # ... resto do código do jogo ...

    # Movimentação X
    if keyboard.left: vel_x -= ACCEL
    elif keyboard.right: vel_x += ACCEL
    vel_x *= FRICTION
    player.x += vel_x

    # Scrolling Lateral (Câmera)
    if player.x > WIDTH / 2:
        # A câmera segue, mas trava no fim do mapa (5000)
        scroll_x = min(player.x - WIDTH / 2, MAP_WIDTH - WIDTH)

    # Gravidade e Movimentação Y
    vel_y += GRAVITY
    player.y += vel_y

    # Colisões
    no_chao = False
    for plat in plataformas:
        if player.colliderect(plat):
            if vel_y > 0: # Caindo
                player.bottom = plat.top
                vel_y = 0
                no_chao = True
            elif vel_y < 0: # Pulando
                player.top = plat.bottom
                vel_y = 0

    if keyboard.space and no_chao:
        vel_y = -12
        try: sounds.pulo.play()
        except: pass

    # Coleta de Moedas
    for m in moedas[:]:
        if player.colliderect(m):
            moedas.remove(m)
            moedas_coletadas += 1
            sounds.moeda.play()
            player_color = "white" 

    # Resetar cor do player suavemente
    if player_color == "white":
        player_color = "orange"

    # Movimento dos Inimigos
    for ene in inimigos:
        ene["rect"].x += 3 * ene["dir"]
        if ene["rect"].right > ene["limite"][1] or ene["rect"].left < ene["limite"][0]:
            ene["dir"] *= -1
        
        # Colisão com Inimigo (Dano/Morte)
        if player.colliderect(ene["rect"]):
            # Reset simples
            player.pos = (100, 450)
            scroll_x = 0
            # (Aqui você poderia tocar um som de dano)

    # Morte por queda
    if player.y > HEIGHT:
        player.pos = (100, 450)
        scroll_x = 0

pgzrun.go()