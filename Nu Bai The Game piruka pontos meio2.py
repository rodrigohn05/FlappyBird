import time
import pygame
import random

pygame.mixer.pre_init(44100,-16,2,520)

pygame.mixer.init()


pygame.init()


######
display_width=400
display_height=600

black= (0,0,0)
white= (255,255,255)
red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)
purple= (128, 0, 128)



gDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Nu Bai')
clock=pygame.time.Clock()

#Sound
sound=pygame.mixer.Sound('Mario.wav')
#socioImg= pygame.image.load('PixelArtTutorial.png')
#socioImg= pygame.transform.scale(socioImg, (100,100))


#colisao = pygame.rect.colliderect(A,B)

num=random.randrange(0,9)
carImg=pygame.image.load('Nubai.png')

def cena_dodge(count):
    font2 = pygame.font.SysFont(None,75)
    texto2 = font2.render (str(count),True, white)
    gDisplay.blit(texto2,(display_width *0.474, 80))
    
def cenas (cenaX,cenaY,cenaW,cenaH,cor):
    pygame.draw.rect(gDisplay, cor, [cenaX,cenaY,cenaW,cenaH])

def cenas2 (cena2X,cena2Y,cena2W,cena2H,cor):
    pygame.draw.rect(gDisplay, cor, [cena2X,cena2Y,cena2W,cena2H])
    
def socio (x,y,socioW,socioH):
    gDisplay.blit(carImg, (x, y))
    

def text_objects(texto, font):
    textS = font.render(texto ,True, red)
    return textS, textS.get_rect()
    
def fora():
    message_display('GAME OVER')


       


def message_display(texto):
    font = pygame.font.SysFont('arial',65)
    textS, textR = text_objects(texto,font)
    textR.center = ((display_width/2),(display_height/2))
    gDisplay.blit(textS, textR)
    
    pygame.display.update()
    
    time.sleep(2)
    game_loop()


def game_loop():
    
    
    x=(display_width *0.45)
    y=(300)
    
    x_change = 0
    y_change = 4
    gravid=0.3
    
    
    socio_width=45
    socio_height=45
    
###########################################################    
    cena_startX= 450
    cena_startY= -50
    cena_speed= -3
    cena_width=35
    cena_height= random.randrange(100,400)
    
    cena2_startX= 450
    cena2_startY= 1.4*(cena_height)
    cena2_speed= -3
    cena2_width=35
    cena2_height= 900
###############################################################

    
    dodged = 0
    
    sair = False
    
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
              #  if event.key == pygame.K_LEFT:
                #    x_change += -5
               # elif event.key == pygame.K_RIGHT:
                #    x_change += 5
                if event.key == pygame.K_UP:
                    y_change += -10
                #elif event.key == pygame.K_DOWN:
                 #   y_change += 10

            if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT:
                 #   x_change += 5
                #elif event.key == pygame.K_RIGHT:
                  #  x_change +=-5

                if event.key == pygame.K_UP:
                    y_change += 5
                #elif event.key == pygame.K_DOWN:
                 #   y_change += -10
        
        
        x += x_change
        y += y_change
        y_change +=gravid
        
        gDisplay.fill(black)
        
        #cenas (cenaX,cenaY,cenaW,cenaH,cor):
        
        cenas(cena_startX, cena_startY,cena_width, cena_height, purple)
        cena_startX+=cena_speed
        cenas2(cena2_startX, cena2_startY,cena2_width, cena2_height, purple)
        cena2_startX+=cena2_speed
        socio(x, y, socio_width, socio_height)
        #colisao(socio, cenas,cenas2)
        cena_dodge(dodged)
        
        if x>display_width-socio_width or x<0:
            fora()
        elif y> display_height-socio_height or y<0:
            fora()
        if cena_startX+cena_width<0:
            cena_height= random.randrange(100,400)
            cena2_height= 900
            cena_startX = 450
            cena2_startX=450
            cena_startY = -50
            cena2_startY = 1.4*(cena_height)

           # if cena2_startY<=(cena_startY+cena_height):
            #    cena2_startY=random.randrange((cena_height+60),(display_height-100))
                
        #if colisao==True:
       #     fora()

        
        if x+socio_width>cena_startX and y<cena_height-50 and x<cena_startX+cena_width or x+socio_width>cena2_startX and y+socio_height>cena2_startY and x<cena2_startX+cena2_width:
            fora()
        if x==cena_startX:
            sound.play()
            dodged+=1
            
        
        
        pygame.display.update()
        clock.tick(60)
        
        
game_loop()        
pygame.quit()
quit()


