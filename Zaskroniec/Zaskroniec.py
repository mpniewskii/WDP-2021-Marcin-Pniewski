import pygame, random
from pygame.locals import *
from pygame import mixer



pygame.init()

mixer.music.load('soundtrack_gra.mp3')
mixer.music.play()

def game_over():
    SCREEN.blit(cmentarz, [0, 0])
    napis_game_over = czcionka_game_over.render("Przegrales! Twoja punktacja to: " + str(punkty), 1, (0, 0, 0))
    instrukcje = czcionka_game_over.render("Naciśnij X by zagrać ponownie lub Y by wyjść!", 1, (0, 0, 0))
    SCREEN.blit(napis_game_over, (130, 10))
    SCREEN.blit(instrukcje, (130, 110))
    kordy.clear()
    mixer.music.load('game_over_soundtrack.mp3')
    mixer.music.play()
    pygame.display.update()




WIDTH = 900
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPSy = pygame.time.Clock()
czcionka = pygame.font.SysFont("monospace", 12)
czcionka_game_over = pygame.font.SysFont("arial", 22)
cmentarz = pygame.image.load('game_over.jpg').convert_alpha()
cmentarz = pygame.transform.scale(cmentarz, (900, 800))




pygame.display.set_caption('Zaskroniec')
TLO = (50, 205, 50)
owocek = pygame.Rect(310, 30, 15, 15)
KOLOREK = (250, 250, 250)
KOLOREKJEDZ = (31, 222, 150)
szybkosc = 10

Xglowy = 70
Yglowy = 10
kordy = []
ruch_boki = 0
ruch_pion = 0
rozmiar = 20
dlugosc = 2
punkty = 0
ruch = 'dol'


Xjedzeniaupdate = 40
Yjedzeniaupdate = 40



przegrales = False
is_running = True
while is_running:
    if przegrales == False:
        SCREEN.fill(TLO)
        gorasciana = pygame.draw.rect(SCREEN, (255, 0, 0), (0, 0, 890, 10))
        dolsciana = pygame.draw.rect(SCREEN, (255, 0, 0), (0, 790, 890, 10))
        lewasciana = pygame.draw.rect(SCREEN, (255, 0, 0), (0, 0, 10, 890))
        prawasciana = pygame.draw.rect(SCREEN, (255, 0, 0), (890, 0, 10, 890))
        jedzenie1 = pygame.draw.rect(SCREEN, KOLOREKJEDZ, [Xjedzeniaupdate, Yjedzeniaupdate, 20, 20])
        mixer.init()





        klawisz = pygame.key.get_pressed()

        if klawisz[pygame.K_LEFT] and ruch != 'prawo':
            ruch = 'lewo'
            ruch_boki = -rozmiar
            ruch_pion = 0
        if klawisz[pygame.K_RIGHT] and ruch != 'lewo':
            ruch = 'prawo'
            ruch_boki = rozmiar
            ruch_pion = 0
        if klawisz[pygame.K_UP] and ruch != 'dol':
            ruch = 'gora'
            ruch_pion = -rozmiar
            ruch_boki = 0
        if ruch == 'dol' or klawisz[pygame.K_DOWN] and ruch != 'gora':
            ruch = 'dol'
            ruch_pion = rozmiar
            ruch_boki = 0

        if przegrales == False:
            Xglowy += ruch_boki
            Yglowy += ruch_pion
            kordy.append([Xglowy, Yglowy])




        if ((Xjedzeniaupdate + 20 > Xglowy and Xjedzeniaupdate - 20  < Xglowy) and (Yjedzeniaupdate + 20 > Yglowy and Yjedzeniaupdate - 20 < Yglowy)):
            Xjedzeniaupdate = int(random.randint(30,850))
            Yjedzeniaupdate = int(random.randint(30,750))
            dlugosc += 1
            szybkosc += 0.1
            punkty += 1


        jedzenie1 = pygame.draw.rect(SCREEN, KOLOREKJEDZ, [Xjedzeniaupdate, Yjedzeniaupdate, 20, 20])
        licznik = czcionka.render("Score: " + str(punkty), 1, (0, 0, 0))
        SCREEN.blit(licznik, (400, 10))

        for blok in kordy[:-1]:
            if blok[0] == Xglowy and blok[1] == Yglowy:
                przegrales = True



        for blok in kordy:
            pygame.draw.rect(SCREEN, (10, 10, 10), [blok[0], blok[1], rozmiar, rozmiar])


        if len(kordy)>dlugosc:
            del kordy[0]
        if Yglowy > 770 or Yglowy < 10 or Xglowy > 870 or Xglowy < 10:
            przegrales = True
        if przegrales == True:
            game_over()




        pygame.display.update()
        FPSy.tick(szybkosc)




    klawisz_game_over = pygame.key.get_pressed()
    if klawisz_game_over[pygame.K_y]:
        is_running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False


pygame.quit()

#Pracowalem_na_zajeciach_10.01_zdalnie_z_powodu_slabego_samopoczucia
