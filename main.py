import pygame
from guy import Guy
from zumbi import zumbi
from shot import Shot
from time import sleep




import random

pygame.init()
#Inicializando o pygame e criando a janela

display = pygame.display.set_mode([840, 480])

pygame.display.set_caption("Meu Jogo")



# tela de inicio
janela = pygame.display.set_mode((840, 480))
pygame.display.set_caption("Meu Jogo")


inicio = pygame.image.load("data/inicio3.jpeg")
pygame.mixer.music.load('data/battleThemeA.mp3')
pygame.mixer.music.play()
janela.blit(inicio, (0, 0))
pygame.display.update()

janela_aberta = True

pygame.mixer.music.load('data/battleThemeA.mp3')
pygame.mixer.music.play(-1)

while janela_aberta:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                 janela_aberta = False



#Groups
objectGroup = pygame.sprite.Group()
zumbiGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

#Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/fundo2.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()


guy = Guy(objectGroup)
guy2 = zumbi(objectGroup)
#guy2.rect.center = [200, 400]
guy3 = zumbi(objectGroup)


#music
pygame.mixer.music.load("data/music.ogg")
pygame.mixer.music.play(-1)

#sounds
shoot = pygame.mixer.Sound("data/laser1.wav")
beep = pygame.mixer.Sound("data/beep.wav")
over = pygame.mixer.Sound("data/round_end.wav")




gameLoop = True
gameover = False
timer = 20
clock = pygame.time.Clock()
if __name__ == "__main__":

    while gameLoop:
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shoot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = guy.rect.center

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    beep.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    beep.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    beep.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    beep.play()


        #Update Logic:
        if not gameover:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newzumbi = zumbi(objectGroup, zumbiGroup)

            collisions = pygame.sprite.spritecollide(guy, zumbiGroup, False, pygame.sprite.collide_mask)

            if collisions:
                over.play()
                #print("Game Over")
                gameover = True
                pygame.mixer.music.stop()
                gameover = pygame.image.load("data/gover.jpeg")
                janela.blit(gameover, (0, 0))
                pygame.display.update()
                sleep(5)
                over.play()
                break


            hits = pygame.sprite.groupcollide(shotGroup, zumbiGroup, True, True, pygame.sprite.collide_mask)




        # Draw:
        display.fill([46, 46, 46])



        objectGroup.draw(display)


        pygame.display.update()


