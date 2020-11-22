import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640 
altura = 480
x = 300 # (largura_screen / 2) - (largura_objeto / 2)  
y = 215 # (altura_screen / 2) - (altura_objeto / 2) 

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

while True:
	clock.tick(30)
	screen.fill((0,0,0))
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

	pygame.draw.rect(screen, (255,0,0), (x,y,40,50))

	
	

	pygame.display.update()

	