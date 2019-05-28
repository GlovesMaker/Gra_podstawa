import sys
import pygame    
def check_events(ai_settings, screen, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_a:
                sys.exit(0)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, mouse_x, mouse_y)
            

def check_play_button(play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        print("masz mnie")
        a = raw_input("wpisz cos: ")
        print("jeste super, wpisales: "+str(a)+" to takie niespotykane")
        
        
def update_screen(ai_settings, screen, play_button):
    
    screen.fill(ai_settings.bg_color)      
    play_button.draw_button()
    pygame.display.flip()

    #if not stats.game_active:
        #play_button.draw_button()