import math
import pygame

class JogoMenu:
    def __init__(self):
        self.ativo = True

    def draw(self, screen, WIDTH, HEIGHT):
        screen.fill((20, 20, 40))
        screen.draw.text("Plataform", center=(WIDTH/2, HEIGHT/3), fontsize=70, color="orange")
        
        # Efeito de piscar no texto usando math.sin
        alpha = math.sin(pygame.time.get_ticks() * 0.005)
        cor = "white" if alpha > 0 else "yellow"
        
        screen.draw.text("Pressione ENTER para começar", center=(WIDTH/2, HEIGHT/2), fontsize=40, color=cor)
        screen.draw.text("Setas: Mover | Espaço: Pular", center=(WIDTH/2, HEIGHT * 0.8), fontsize=25, color="gray")

    def update(self, keyboard):
        # MUDANÇA AQUI: .enter vira .return
        if keyboard.RETURN: 
            self.ativo = False