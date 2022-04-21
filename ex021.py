# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM PROGRAMA EM MP3

import pygame
pygame.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
pygame.event.wait()



