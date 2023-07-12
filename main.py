'''Este é um jogo simples usando a biblioteca Pygame. 
Ele contém vários recursos como a tela de jogo, a imagem de fundo, imagens de alienígenas, jogador e mísseis, e suas posições.

A primeira parte do código é usada para inicializar o Pygame e configurar a tela do jogo. 
Em seguida, as imagens são carregadas e redimensionadas para o tamanho desejado. 
A posição inicial de cada imagem é definida como uma variável global. 
O jogo é executado no loop principal, que mantém o jogo aberto até que a variável rodando se torne falsa.

Há várias funções que são usadas para gerenciar o jogo. A função "respawn" é usada para redefinir a posição inicial do alienígena quando ele sai da tela ou é atingido. 
A função "respawn_missil" é usada para redefinir a posição inicial do míssil quando ele é disparado. 
A função "colisions" é usada para detectar colisões entre os objetos e atualizar o número de pontos do jogador.

Finalmente, a entrada do jogador é capturada através da biblioteca Pygame e usada para mover o jogador e o míssil na tela. 
A imagem de cada objeto é desenhada na tela a cada iteração do loop principal.
'''




# importações
import pygame
import random

#Inciciando o pygame
pygame.init()

# Define o tamanho da tela do jogo
x = 1280
y = 720

# Cria a tela do jogo
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Título do jogo")

# Carregando imagens do jogo
bg = pygame.image.load("./imagens/bg2.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

alien_img = pygame.image.load("./imagens/alien.gif")
alien_img = pygame.transform.scale(alien_img, (50, 50))

player_img = pygame.image.load("./imagens/space.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))
player_img = pygame.transform.rotate(player_img, -90)

missil_img = pygame.image.load("./imagens/missel.png").convert_alpha()
missil_img = pygame.transform.scale(missil_img, (20, 20))
missil_img = pygame.transform.rotate(missil_img, 0)

coracao_img = pygame.image.load("./imagens/heart.png").convert_alpha()
coracao_img = pygame.transform.scale(coracao_img, (30, 30))

# Posições iniciais
alien_x = 1200
alien_y = 360

player_x = 200
player_y = 300

missil_x = 215
missil_y = 315
missil_vel_x = 0

coracao_x = 20
coracao_y = 20

# Variáveis de jogo
rodando = True
atirando = False
pontos = 0
vidas = 5

# Rects das imagens
player_rect = player_img.get_rect()
alien_rect = alien_img.get_rect()
missil_rect = missil_img.get_rect()


#Musica tema do jogo
pygame.mixer.music.load("./musicas/music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Loop principal
while rodando:
    #Matem o jogo aberto enquanto não for cliclado no QUIT (X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    # Desenha o background
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
    
    # Atualiza posições
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and player_y > 1:
        player_y -= 1
        if not atirando:
            missil_y -= 1
    if tecla[pygame.K_DOWN] and player_y < 665:
        player_y += 1
        if not atirando:
            missil_y += 1
    if tecla[pygame.K_SPACE]:
        atirando = True
        missil_vel_x = 2
        if atirando and missil_x == 215: #So toca o som se a nave estiver atirando e o missil estiver na posição inicial 215 no eixo x
            sound = pygame.mixer.Sound("./efeitos_sonoros/missile_sound.wav")
            sound.set_volume(0.1)
            sound.play()  

    #Criando imagens dos atores
    screen.blit(alien_img, (alien_x, alien_y))
    screen.blit(missil_img, (missil_x, missil_y)) # O missil tem que ser chamado antes da nave, caso contrário ele vai se sobrepor a nave
    screen.blit(player_img, (player_x, player_y))

    # Movimento do background
    x -= 1.5

    # Movimento do alien
    alien_x -= 1

    # Movimento do míssil
    missil_x += missil_vel_x

    # Atualiza posições dos rects
    player_rect.x = player_x
    player_rect.y = player_y
    missil_rect.x = missil_x
    missil_rect.y = missil_y
    alien_rect.x = alien_x
    alien_rect.y = alien_y

    #pontuação do jogo

    #TENTE FAZER, USE O CHAT GPT OU A DOCUMENTAÇÃO COMO AJUDA


    
    # Funções
    def respawn():
        x = 1350
        y = random.randint(1,640)
        return [x,y]

    def respawn_missil():
        atirando = False
        respawn_missil_x = player_x + 15
        respawn_missil_y = player_y + 15
        velocidade_missil_x = 0
        return [respawn_missil_x,respawn_missil_y, atirando, velocidade_missil_x]

    def colisions():
        global vidas
        if player_rect.colliderect(alien_rect):
            vidas -= 1
            return True
        elif missil_rect.colliderect(alien_rect):
            return True
        elif  alien_rect.x == 60:
            return True
        else:
            return False
    def saude(vidas):
        if vidas == 5:
            screen.blit(coracao_img, (coracao_x, coracao_y))
            cont = 40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            cont+=40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            cont+=40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            cont+=40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))

        if vidas == 4:
            screen.blit(coracao_img, (coracao_x, coracao_y))
            cont = 40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            cont+=40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            cont+=40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            
        if vidas == 3:
            screen.blit(coracao_img, (coracao_x, coracao_y))
            cont = 40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            cont+=40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
            
        if vidas == 2:
            screen.blit(coracao_img, (coracao_x, coracao_y))
            cont = 40
            screen.blit(coracao_img, (coracao_x+cont, coracao_y))
                
        if vidas == 1:
            screen.blit(coracao_img, (coracao_x, coracao_y))

    #Fazendo o aliem da respawn
    if alien_x == 50:
        alien_x = respawn()[0]
        alien_y = respawn()[1]
    #Fazendo o missil da respawn
    if missil_x > 1300:
        missil_x, missil_y, atirando, missil_vel_x = respawn_missil()
        print(respawn_missil())

    #se acontecer alguma colisão vai dar respwn nos atores
    if alien_x == 50 or colisions():
        alien_x = respawn()[0]
        alien_y = respawn()[1]

    saude(vidas)
    if vidas == 0:
        
        break
    #mostrar contorno da dossa imagens que agora é são objetos
    #Para ver esse feito apague as aspas tripas do codigo abaixo
    '''pygame.draw.rect(screen,(255,0,0), player_rect,4)
    pygame.draw.rect(screen,(255,0,0), missil_rect, 4)
    pygame.draw.rect(screen,(255,0,0), alien_rect, 4)'''

    #Atualiza a tela constantemente
    pygame.display.update()


