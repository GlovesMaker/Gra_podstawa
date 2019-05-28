import sys
import pygame
from settings import Settings
from button import Button
import game_functions as gf


def run_game():
    #inicjalizacja programu i utworzenie obiektu ekranu
    pygame.init()
    pygame.display.set_caption("Daniel i Iza Triangulacja Delaunay'a")

    #egzemplarz klasy ustawienia
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button = Button(ai_settings, screen, "gra")

    #self.game_active = False
    #Rozpoczecie petli serca programu
    while True:
        
        #Oczekiwania na naci�niecie klawisza lub przycisku myszy
        gf.check_events(ai_settings, screen, play_button)
        gf.update_screen(ai_settings, screen, play_button)

        #print("gramy")

#wywolanie funkcji run_game()
run_game()

