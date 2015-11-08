#!/usr/bin/env python
# encoding: utf-8

"""
Twitter: @server1567
"""

# Hola Mundo!

import pygame,sys
from pygame.locals import *

# Variables GLOBALES
ancho = 900
alto = 480

#####################Pantalla Inicial######################

def Inicio():
	pygame.init()
	window = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Space Invaders by Junior J.")

	fondo = pygame.image.load("imagesPygame/space.gif")
	up = pygame.image.load("imagesPygame/up.png")
	down = pygame.image.load("imagesPygame/down.png")
	left = pygame.image.load("imagesPygame/left.png")
	right = pygame.image.load("imagesPygame/right.png")

	# Área de letras y música

	pygame.mixer.music.load("Sonidos/Intro.mp3")
	pygame.mixer.music.play(3)

	SysFuente = pygame.font.SysFont("Arial",30)
	Fuente = pygame.font.SysFont("Garamond",25)
	Copyright = pygame.font.SysFont("Verdana",10)
	X = Fuente.render("Presione X para Jugar",0,(0,0,255))
	Controls = SysFuente.render("Use estos Movimientos:",0,(255,255,255))
	Gun = Fuente.render("Presione X para disparar",0,(255,255,255))
	Creditos = Copyright.render("Created by Junior.  Without right reserved.",0,(0,0,255))

	while True:
		# XCosas para la ventana
		window.blit(fondo,(0,0))

		# Eventos del teclado

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

				elif event.key == K_x:
					from Space import SpaceInvader
					SpaceInvader()


		# Renderización

		window.blit(Gun,(590,200))
		window.blit(X,(20,440))
		window.blit(Controls,(560,70))

		window.blit(left,(600,125))
		window.blit(up,(650,125))
		window.blit(right,(708,125))
		window.blit(down,(762,125))

		window.blit(Creditos,(640,450))

		pygame.display.update()

Inicio()

#####################Pantalla Inicial######################

					# Fin de código
