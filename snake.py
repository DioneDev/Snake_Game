import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640 
altura = 480
x = 300 # (largura_screen / 2) - (largura_objeto / 2)  
y = 215 # (altura_screen / 2) - (altura_objeto / 2) 

# randint serve para sortiar valores entre os intervalos pré-definidos.
# variavel para o objeto receber diferente posições
x_azul = randint(40,600)
y_azul = randint(50,430)

pontos = 0 # Placar 

fonte = pygame.font.SysFont('arial', 25, True) # Fonte,Tamanho texto, Negrito true e false, Italico true e false

screen = pygame.display.set_mode((largura, altura)) # Criar a tela de jogo.
pygame.display.set_caption('Snake Game') # Mudar o nome na tela de jogo (opcional)
clock = pygame.time.Clock()

while True:
	clock.tick(30)
	screen.fill((0,0,0))
	mensage = f'Pontos: {pontos}'
	texto_formatado = fonte.render(mensage, True, (255,255,255))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

		'''
		# Ver no ReadMe: Logica do plano cartesiano no pygame.  
		# Evento de teclado / movimento do objeto

		if event.type == KEYDOWN:

			if event.key == K_a:
				x = x - 20
			if event.key == K_d:
				x = x + 20
			if event.key == K_w:
				y = y - 20	# Eixo Y: Valor negativo para o objeto subir e valor positivo para descer.
			if event.key == K_s:
				y = y + 20	
		'''

	# Ver no ReadMe: Logica do plano cartesiano no pygame.  
	# Evento de teclado / movimento do objeto

	if pygame.key.get_pressed()[K_a]:
		x = x - 20
	if pygame.key.get_pressed()[K_d]:
		x = x + 20
	if pygame.key.get_pressed()[K_w]:
		y = y - 20
	if pygame.key.get_pressed()[K_s]:
		y = y + 20	

	ret_vermelho = pygame.draw.rect(screen, (255,0,0), (x,y,40,50))
	ret_azul = pygame.draw.rect(screen, (0,0,255), (x_azul,y_azul, 40,50))

	# Toda vez que a variavel ret_vermelho passar pela variavel ret_azul, as variaveis x_azul e y_azul irao assumir nova posição.
	if ret_vermelho.colliderect(ret_azul):
		x_azul = randint(40,600)
		y_azul = randint(50,430)
		pontos = pontos + 1

	
	screen.blit(texto_formatado,(450,40))

	pygame.display.update()

	