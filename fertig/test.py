import pygame
pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie('bild0.mpg')
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()
movie.set_display(movie_screen)
movie.play()
playing = True
while playing:
    screen.blit(movie_screen,(0,0))
    pygame.display.update()
pygame.quit()
