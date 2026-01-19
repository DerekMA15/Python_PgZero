import pgzrun
import math
import random
import pygame

# Configurações da Janela
WIDTH = 800
HEIGHT = 600
TITLE = "Plataforma - Nível 1 Expandido"

# Player
player = Rect((50, 450), (30, 40))
vel_y = 0
vel_x = 0
ACCEL = 0.6
FRICTION = 0.85
GRAVITY = 0.5
moedas_coletadas = 0

# Câmera (Scrolling)
scroll_x = 0

# Configuração do Mundo (Esticamos a fase lateralmente até 2000 pixels)
plataformas = [
    Rect((0, 550), (400, 50)),
    Rect((500, 450), (200, 20)),
    Rect((800, 350), (300, 20)),
    Rect((1200, 400), (200, 20)),
    Rect((1500, 550), (500, 50)), # Plataforma final
]

# Moedas em posições fixas (3 moedas)
moedas = [
    Rect((550, 410), (20, 20)),
    Rect((950, 310), (20, 20)),
    Rect((1600, 510), (20, 20))
]

# Inimigo Simples
inimigo = Rect((850, 310), (30, 40))
inimigo_vel = 2
inimigo_dir = 1 # 1 para direita, -1 para esquerda

# Iniciar Música
try:
    music.play('tema')
    music.set_volume(0.4) # Volume mais baixo para não abafar os sons
except:
    print("Erro: Arquivo music/tema.mp3 não encontrado.")

def draw():
    screen.clear()
    screen.fill((15, 15, 35))
    
    # Ao desenhar, subtraímos o scroll_x da posição X de cada objeto
    
    # Desenhar Plataformas
    for plat in plataformas:
        # Criamos um retângulo temporário deslocado para o desenho
        draw_rect = Rect((plat.x - scroll_x, plat.y), (plat.width, plat.height))
        screen.draw.filled_rect(draw_rect, (100, 80, 60))

    # Desenhar Moedas
    for moeda in moedas:
        # Efeito visual de flutuar usando math
        offset_y = math.sin(pygame.time.get_ticks() * 0.005) * 5
        m_rect = Rect((moeda.x - scroll_x, moeda.y + offset_y), (20, 20))
        screen.draw.filled_rect(m_rect, "yellow")

    # Inimigo
    screen.draw.filled_rect(Rect((inimigo.x - scroll_x, inimigo.y), (30, 40)), "red")

    #  Jogador
    screen.draw.filled_rect(Rect((player.x - scroll_x, player.y), (30, 40)), "orange")
    
    # Interface (HUD) - Fica fixa na tela (não usa scroll_x)
    screen.draw.text(f"Moedas: {moedas_coletadas}/3", (20, 20), fontsize=30)
    
    if moedas_coletadas == 3:
        screen.draw.text("VOCÊ VENCEU! PEGUE TODAS!", (250, 250), fontsize=50, color="green")

def update():
    global vel_y, vel_x, scroll_x, moedas_coletadas, inimigo_vel, inimigo_dir

    # Movimentação e Gravidade do Jogador
    if keyboard.left: vel_x -= ACCEL
    elif keyboard.right: vel_x += ACCEL
    vel_x *= FRICTION
    player.x += vel_x

    # Lógica da Câmera (Scrolling)
    # A câmera segue o jogador se ele passar do meio da tela
    if player.x > WIDTH / 2:
        scroll_x = player.x - WIDTH / 2

    # Colisões com Plataformas
    vel_y += GRAVITY
    player.y += vel_y
    
    no_chao = False
    for plat in plataformas:
        if player.colliderect(plat):
            if vel_y > 0:
                player.bottom = plat.top
                vel_y = 0
                no_chao = True
            elif vel_y < 0:
                player.top = plat.bottom
                vel_y = 0
        
        # Colisão lateral simples
        if player.colliderect(plat) and abs(player.x - plat.x) < 50:
             # Ajuste fino aqui se necessário
             pass

    # Pulo com Som
    if keyboard.space and no_chao:
        vel_y = -12
        try:
            sounds.pulo.play()
        except:
            pass

    # Coleta de Moedas
    for moeda in moedas[:]: 
        if player.colliderect(moeda):
            moedas.remove(moeda)
            moedas_coletadas += 1
            sounds.moeda.play() # Se tiver som de moeda

    #  Movimento do Inimigo (Patrulha na plataforma 2)
    plat_inimigo = plataformas[2] # A plataforma onde o inimigo está
    inimigo.x += inimigo_vel * inimigo_dir
    if inimigo.right > plat_inimigo.right or inimigo.left < plat_inimigo.left:
        inimigo_dir *= -1 

    # Colisão com Inimigo (Morte)
    if player.colliderect(inimigo):
        player.pos = (50, 450)
        scroll_x = 0

pgzrun.go()