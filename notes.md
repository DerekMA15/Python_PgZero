1. Estrutura de Pastas (Obrigatória)

O Pygame Zero é rigoroso com a organização. Ele procura automaticamente por arquivos em pastas específicas. Se você não criar essa estrutura, o código não encontrará suas imagens ou sons.

Crie uma pasta para o seu projeto (ex: meu_jogo_plataforma) e, dentro dela, crie as seguintes pastas:

    images/: Onde ficarão seus personagens, blocos e fundo (formatos .png ou .jpg).

    sounds/: Para efeitos sonoros curtos (pulo, dano, coletar item) em formato .wav ou .ogg.

    music/: Para a trilha sonora de fundo (formato .mp3 ou .ogg).

    meu_jogo.py: O arquivo principal onde escreveremos o código.

2. Preparando os Assets (Arquivos)

Para que o jogo funcione, você precisará de alguns nomes de arquivos padrão. Sugiro que você já salve alguns arquivos com estes nomes:
Pasta	Nome Sugerido	Descrição
images	player.png	O herói do jogo.
images	ground.png	O bloco do chão/plataforma.
sounds	jump.wav	Som ao pular.
music	theme.mp3	Música que ficará tocando em loop.