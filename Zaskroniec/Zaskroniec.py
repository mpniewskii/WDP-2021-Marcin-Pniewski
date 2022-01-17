import pygame, random
from pygame.locals import *
from pygame import mixer



pygame.init()

mixer.music.load('soundtrack_gra.mp3')
mixer.music.play()
pygame.mixer.music.play(-1)

def uruchom():
    SCREEN.blit(essa, (0, 0))
    gorasciana = pygame.draw.rect(SCREEN, (255, 0, 0), (0, 0, 890, 10))
    dolsciana = pygame.draw.rect(SCREEN, (255, 0, 0), (0, 790, 890, 10))
    lewasciana = pygame.draw.rect(SCREEN, (255, 0, 0), (0, 0, 10, 890))
    prawasciana = pygame.draw.rect(SCREEN, (255, 0, 0), (890, 0, 10, 890))
    jedzenie1 = pygame.draw.rect(SCREEN, KOLOREKJEDZ, [Xjedzeniaupdate, Yjedzeniaupdate, 20, 20])

    mixer.init()
    przegrales = False


def game_over():
    SCREEN.blit(cmentarz, [0, 0])
    napis_game_over = czcionka_game_over.render("Przegrałeś! Twoja punktacja to: " + str(punkty), 1, (0, 0, 0))
    instrukcje = czcionka_game_over.render("Naciśnij Y by wyjść!", 1, (0, 0, 0))
    SCREEN.blit(napis_game_over, (130, 10))
    SCREEN.blit(instrukcje, (130, 110))
    kordy.clear()
    mixer.music.load('game_over_soundtrack.mp3')
    mixer.music.play()
    pygame.display.update()
    klawisz_game_over = pygame.key.get_pressed()



def waz():
    for blok in kordy:
        pygame.draw.rect(SCREEN, (75, 0, 130), [blok[0], blok[1], rozmiar, rozmiar])

    if len(kordy) > dlugosc:
        del kordy[0]

def ruchy():
    global ruch
    global Xglowy
    global Yglowy
    global ruch_pion
    global ruch_boki

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



WIDTH = 900
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPSy = pygame.time.Clock()

essa = pygame.image.load('Tlo.jpg').convert_alpha()
essa = pygame.transform.scale(essa, (900, 800))

czcionka = pygame.font.SysFont("monospace", 12)
czcionka_game_over = pygame.font.SysFont("arial", 22)

cmentarz = pygame.image.load('game_over.jpg').convert_alpha()
cmentarz = pygame.transform.scale(cmentarz, (900, 800))

mleczko_power_up = pygame.image.load('mleczko_power_up.png').convert_alpha()
mleczko_power_up = pygame.transform.scale(mleczko_power_up, (30, 30))
Xmleczka = int(random.randint(30,850))
Ymleczka = int(random.randint(30,750))

zupka_power_up = pygame.image.load('zupka_power_up.png').convert_alpha()
zupka_power_up = pygame.transform.scale(zupka_power_up, (20, 20))
Xzupki = int(random.randint(30,850))
Yzupki = int(random.randint(30,750))

szansa_power_up = 0
ktory_power_up = 3

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
ruch = 'dol'
rozmiar = 20
dlugosc = 2
punkty = 0


Xjedzeniaupdate = 40
Yjedzeniaupdate = 40



przegrales = False
is_running = True

while is_running:
    if przegrales == False:
        uruchom()
        ruchy()




        if ((Xjedzeniaupdate + 20 > Xglowy and Xjedzeniaupdate - 20 < Xglowy) and (Yjedzeniaupdate + 20 > Yglowy and Yjedzeniaupdate - 20 < Yglowy)):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('jedzenie.mp3'))
            Xjedzeniaupdate = int(random.randint(30,850))
            Yjedzeniaupdate = int(random.randint(30,750))
            dlugosc += 1
            szybkosc += 0.1
            punkty += 1
            szansa_power_up = int(random.randint(0, 1))
            if szansa_power_up == 1:
                ktory_power_up = int(random.randint(0, 1))

        if ((Xmleczka + 15 > Xglowy and Xmleczka - 15 < Xglowy) and (Ymleczka + 15 > Yglowy and Ymleczka - 15 < Yglowy)):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('jedzenie.mp3'))
            Xmleczka = int(random.randint(30,850))
            Ymleczka = int(random.randint(30,750))
            szybkosc -= 0.5
            SCREEN.blit(mleczko_power_up, (Xmleczka, Ymleczka))
            szansa_power_up = int(random.randint(0, 1))
            if szansa_power_up == 1:
                ktory_power_up = int(random.randint(0, 1))

        if ((Xzupki + 20 > Xglowy and Xzupki - 20 < Xglowy) and (Yzupki + 20 > Yglowy and Yzupki - 20 < Yglowy)):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('jedzenie.mp3'))
            Xzupki = int(random.randint(30,850))
            Yzupki = int(random.randint(30,750))
            szybkosc += 0.5
            dlugosc -= 1
            del kordy[0]
            szansa_power_up = int(random.randint(0, 1))
            if szansa_power_up == 1:
                ktory_power_up = int(random.randint(0, 1))

        if szansa_power_up == 1 and ktory_power_up == 1:
            SCREEN.blit(mleczko_power_up, (Xmleczka, Ymleczka))

        if szansa_power_up == 1 and ktory_power_up == 0:
            SCREEN.blit(zupka_power_up, (Xzupki, Yzupki))

        licznik = czcionka.render("Score: " + str(punkty), 1, (0, 0, 0))
        SCREEN.blit(licznik, (400, 10))

        waz()
        for blok in kordy[:-1]:
            if blok[0] == Xglowy and blok[1] == Yglowy:
                przegrales = True
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
#Dodaje_pogram_przepisany_na_funkcje
