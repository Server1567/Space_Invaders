#!/usr/bin/env python
# encoding: utf-8

import pygame,sys
from pygame.locals import *
from Clases import Nave
from Clases import Invasor as Enemigo
from Clases import Proyectil

# Variables GLOBALES
ancho = 900
alto = 480
listaEnemigo = []


def dentenerTodo():
	for enemigo in listaEnemigo:
		for disparo in enemigo.listaDisparo:
			enemigo.listaDisparo.remove(disparo)

		enemigo.conquista = True

def detenerTodo2():
	for jugador in listaDisparo:
		for disparar in jugador.listaDisparo:
			jugador.listaDisparo.remove(disparar)

		enemigo.conquista = False

def cargarEnemigos():
	posx = 100
	for x in range(1, 5):
		enemigo = Enemigo(posx,100,40, "imagesPygame/marcianoA.jpg", "imagesPygame/MarcianoB.jpg",)
		listaEnemigo.append(enemigo)
		posx = posx + 200

	posx = 100
	for x in range(1,5):
		enemigo = Enemigo(posx,0,40, "imagesPygame/Marciano3A.jpg", "imagesPygame/Marciano3B.jpg",)
		listaEnemigo.append(enemigo)
		posx = posx + 200


def SpaceInvader():
	pygame.init()
	window = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Space Invaders by Junior J.")
	fondo = pygame.image.load("imagesPygame/Fondo.jpg")

	pygame.mixer.music.load("Sonidos/Intro.mp3")
	pygame.mixer.music.play(3)

	miFuenteSistema = pygame.font.SysFont("Arial",30)
	Fuente = pygame.font.SysFont("Verdana",50)
	Texto = miFuenteSistema.render("Fin del Juego",0,(120,100,40))
	indicio = miFuenteSistema.render("Presiona R para Reiniciar la partida",0,(255,0,0))
	indicio2 = miFuenteSistema.render("Presiona Esc para Salir",0,(255,0,0))
	WINNER = Fuente.render("GANASTE EL JUEGO",0,(0,255,0))

	jugador = Nave.naveEspacial(ancho,alto)
	cargarEnemigos()

	enJuego = True

	reloj = pygame.time.Clock()

	while True:

		# Del reloj
		reloj.tick(60)

		tiempo = pygame.time.get_ticks()/1000

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if enJuego == True:
				if event.type == pygame.KEYDOWN:
					if event.key == K_LEFT:
						jugador.movimientoIzquierda()

					elif event.key == K_RIGHT:
						jugador.movimientoDerecha()
						
					elif event.key == K_x:
						x,y = jugador.rect.center
						jugador.disparar(x,y)

					elif event.key == K_ESCAPE:
						import main
						return main


		window.blit(fondo, (0,0))

		jugador.dibujar(window)

		if len(jugador.listaDisparo) > 0:
			for x in jugador.listaDisparo:
				x.dibujar(window)
				x.trayectoria()

				if x.rect.top < -10:
					jugador.listaDisparo.remove(x)
				else:
					for enemigo in listaEnemigo:
						if x.rect.colliderect(enemigo.rect):
							listaEnemigo.remove(enemigo)


		if len(listaEnemigo) > 0:
			for enemigo in listaEnemigo:
				enemigo.comportamiento(tiempo)
				enemigo.dibujar(window)

				if enemigo.rect.colliderect(jugador.rect):
					jugador.destruccion()
					enJuego = False
					dentenerTodo()


				if len(enemigo.listaDisparo) > 0:
					for x in enemigo.listaDisparo:
						x.dibujar(window)
						x.trayectoria()
						
						if x.rect.colliderect(jugador.rect):
							jugador.destruccion()
							enJuego = False
							dentenerTodo()

							
						if x.rect.top > 900:
							pass

							
						else:
							for disparo in jugador.listaDisparo:
								if x.rect.colliderect(disparo.rect):
									jugador.listaDisparo.remove(disparo)
		
		else:
			enJuego == True
			window.blit(WINNER,(150,75))
			pygame.mixer.music.stop()							
		


		if enJuego == False:
			pygame.mixer.music.stop()
			window.blit(Texto,(300,300))
			window.blit(indicio,(50,50))
			window.blit(indicio2,(50,85))
			if event.type == KEYDOWN:
				if event.key == K_r:
					pygame.quit()
					SpaceInvader()

				elif event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

		pygame.display.update()

SpaceInvader()


"""

Si te gustó el juego, te lo regalo, ya que es FreeSoft.
Lo he creado sólo para ganar experiencia en los videojuegos en Python.
Si estas en un proyecto en Python puedo ayudarte, sólo agregame en Fb:
https://www.facebook.com/junior.jimenezabreu

Ahí estoy para cualquier duda.
Con gusto Mr.Server1567 :/

"""


