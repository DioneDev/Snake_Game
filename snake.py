import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Add musica ao jogo.
pygame.mixer.music.set_volume(0.2) 
musica = pygame.mixer.music.load('./music/BoxCat_Games.wav')
pygame.mixer.music.play(-1) # Parametro -1 fará com que a musica repita

som_colisao = pygame.mixer.Sound('./music/smw_coin.wav')

width = 600 
height = 600

speed = 15
x_control = speed
y_control = 0

x_snake = int(width/2) # (largura_screen / 2) - (largura_objeto / 2)  
y_snake = int(height/2) # (altura_screen / 2) - (altura_objeto / 2) 

# randint serve para sortear valores entre os intervalos pré-definidos.
# variavel para o objeto receber diferente posições
x_apple = randint(20,580)
y_apple = randint(20,580)
score = 0 # Placar 

fonte = pygame.font.SysFont('arial', 25, True) # Fonte,Tamanho texto, Negrito true e false, Italico true e false

screen = pygame.display.set_mode((width, height)) # Criar a tela de jogo.
pygame.display.set_caption('Snake Game') # Mudar o nome na tela de jogo (opcional)
clock = pygame.time.Clock()
list_snake = []
initial_length = 3
game_over = False

def body_snake(list_snake):
	for XeY in list_snake:
		pygame.draw.rect(screen, (0,255,0), (XeY[0], XeY[1], 10,10))

def restart_game():
	global score, initial_length, x_snake, y_snake, list_snake, list_head, x_apple, y_apple, game_over
	score = 0
	initial_length = 3
	x_snake = int(width/2)
	y_snake = int(height/2)
	list_snake = []
	list_head = []
	x_apple = randint(20,580)
	y_apple = randint(20,580)
	game_over = False

while True:
	clock.tick(speed)
	screen.fill((0,0,0)) # Cor de fundo da tela
	mensage = f'Score: {score}'
	scoreboard = fonte.render(mensage, True, (255,255,255))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		
		# Evento de teclado / movimento do objeto

		if event.type == KEYDOWN:

			if event.key == K_a:
				if x_control == speed:
					pass
				else:
					x_control = -speed
					y_control = 0

			if event.key == K_d:
				if x_control == -speed:
					pass
				else:
					x_control = speed
					y_control = 0

			if event.key == K_w:
				if y_control == speed:
					pass
				else:
					y_control = -speed # Eixo Y: Valor negativo para o objeto subir e valor positivo para descer.
					x_control = 0	

			if event.key == K_s:
				if y_control == -speed:
					pass
				else:
					y_control = speed # Eixo Y: Valor negativo para o objeto subir e valor positivo para descer.
					x_control = 0	

	x_snake = x_snake + x_control
	y_snake = y_snake + y_control	

	snake = pygame.draw.rect(screen, (0,255,0), (x_snake,y_snake, 10,10))
	apple = pygame.draw.rect(screen, (255,0,0), (x_apple,y_apple, 10,10))

	if snake.colliderect(apple):
		x_apple = randint(20,580)
		y_apple = randint(20,580)
		score = score + 1
		som_colisao.play()
		initial_length = initial_length +1

	list_head = [] # Armazena os valores de x e y da cabeça da cobra
	list_head.append(x_snake)
	list_head.append(y_snake)
	 
	list_snake.append(list_head)

	# Condição para finalizar o jogo.
	if list_snake.count(list_head) >1:
		fonte2 = pygame.font.SysFont('arial', 17, True)
		mensage = 'Game over !! HAhaHAha Pressione a tecla R para jogar novamente.'
		texto_formatado = fonte2.render(mensage, True, (0,0,0))
		ret_texto = texto_formatado.get_rect()

		game_over = True
		while game_over:
			screen.fill((255,255,255))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					exit()
				if event.type == KEYDOWN:	
					if event.key == K_r:
						restart_game()

			ret_texto.center = (width//2, height//2)			
			screen.blit(texto_formatado, ret_texto)
			pygame.display.update()

	# Condição para a cobra passar a parede e voltar novamente.
	if x_snake > width:
		x_snake = 0
	if x_snake < 0:
		x_snake = width
	if y_snake < 0:
		y_snake = height
	if y_snake > height:
		y_snake = 0

	if len(list_snake) > initial_length:
		del list_snake[0]

	body_snake(list_snake)
	
	screen.blit(scoreboard,(470,20))

	pygame.display.update()
