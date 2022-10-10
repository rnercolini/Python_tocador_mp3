# Tocando um arquivo mp3 usando pygame.
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('wratinho.mp3')
pygame.mixer_music.play()
pygame.event.wait()
