import asyncio
import pygame
from pygame.locals import *






async def main():
    pygame.init()
    pygame.mixer.init()



    pygame.mixer.music.load("spamton_neo_mix_ex_wip.ogg")
    # pygame.mixer.music.load("battle.ogg")
    pygame.mixer.music.play(-1)

    # pygame.mixer.music.load("sys_title/M_sys_title_intro.mp3.ogg")
    # pygame.mixer.music.play()
    # pygame.mixer.music.queue(filename = "sys_title/M_sys_title_loop.mp3.ogg", loops = -1)

    
    
    
    

    bg_size = width, height = 300, 200
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Music - drls2's Demo")

    paused = False

    '''
    pause_image = pygame.image.load("pause.png").convert_alpha()
    unpause_image = pygame.image.load("unpause.png").convert_alpha()
    pause_rect = pause_image.get_rect()
    pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2
    '''

    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = (width - paused_rect.width) // 2, (height - paused_rect.height) // 2

    paused_image = pause_nor_image


    lDown=False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                # sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    paused = not paused

    #or (event.type == KEYDOWN and event.key == K_SPACE)
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and paused_rect.collidepoint(event.pos):
                lDown=True

            if lDown and event.type == MOUSEBUTTONUP and event.button == 1:
                if paused_rect.collidepoint(event.pos):
                    paused = not paused
                lDown=False
                    

            if paused:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()

            #elif event.type == MOUSEMOTION:
            if paused_rect.collidepoint(pygame.mouse.get_pos()):
                if paused:
                    paused_image = resume_pressed_image
                else:
                    paused_image = pause_pressed_image

            else:
                if paused:
                    paused_image = resume_nor_image
                else:
                    paused_image = pause_nor_image

            
            
                    

        screen.fill((0, 0, 0))


        screen.blit(paused_image, paused_rect)
            
            
        


        pygame.display.flip()



        await asyncio.sleep(0)  # You must include this statement in your main loop. Keep the argument at 0.     



asyncio.run(main())
