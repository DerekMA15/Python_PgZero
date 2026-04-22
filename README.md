# Plataforma Pro - Python & Pygame Zero

Este repositório contém um motor de jogo de plataforma 2D desenvolvido em Python utilizando a biblioteca **Pygame Zero**. O projeto foca na implementação de mecânicas clássicas de jogos de plataforma, como física de gravidade, sistema de câmera e gerenciamento de estados.

## Funcionalidades

- **Sistema de Câmera (Scrolling):** O mundo possui 5000px de largura, com a câmera seguindo o jogador dinamicamente.
- **Física de Movimentação:** Sistema de aceleração, gravidade e fricção para um controle fluido do personagem.
- **IA de Patrulha:** Inimigos com lógica de movimentação autônoma dentro de limites territoriais.
- **Coletáveis Animados:** Moedas com efeito de brilho e oscilação processados via funções matemáticas (`math.sin`).
- **Gerenciamento de Estados:** Separação entre Menu e Jogo através da integração com a classe `JogoMenu`.

## Análise Técnica (Trechos Principais)

Seguindo o princípio de documentação técnica, abaixo estão os destaques da lógica implementada no `main.py`:

### **1. O Cálculo do Scroll**
Para criar o efeito de mundo aberto, a posição de desenho dos objetos é relativa ao `scroll_x`, calculado com base na posição do jogador:
```python
if player.x > WIDTH / 2:
    scroll_x = min(player.x - WIDTH / 2, MAP_WIDTH - WIDTH) 
```
- **O que faz:** Quando o jogador passa do meio da tela, o scroll_x começa a aumentar, subtraindo esse valor da posição de desenho de todos os outros objetos, criando a ilusão de movimento de câmera.

### **2. Tratamento de Colisão Dinâmica**

A colisão não apenas impede a passagem, mas ajusta a posição do ator para evitar que ele "vibre" dentro da plataforma:
Python
```python
if player.colliderect(plat):
    if vel_y > 0: # Caindo
        player.bottom = plat.top
        vel_y = 0
```
- **O que faz:** Identifica se o impacto foi durante a queda para resetar a velocidade vertical e fixar o pé do personagem exatamente no topo da plataforma.

### **3. Efeitos Matemáticos no draw()**

Para o brilho das moedas, foi utilizada a biblioteca math:
```python
brilho = abs(math.sin(pygame.time.get_ticks() * 0.01)) * 5
```
- **O que faz:** Cria uma oscilação suave no tamanho do retângulo da moeda com base no tempo de execução, sem a necessidade de múltiplos assets de imagem.

## Como Instalar e Rodar

### 1.Pré-requisitos: 
- Python 3.x instalado.

### 2.Instalação:
```bash
    pip install pgzero
```
### 3.Execução:
```bash
    pgzrun main.py
```

## Estrutura do Repositório

- main.py: Core loop, física e renderização.

- menu.py: Gerenciamento do estado de menu.

- /sounds & /music: Assets de áudio (requeridos para execução completa).
