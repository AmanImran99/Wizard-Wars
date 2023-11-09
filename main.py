import pygame
import pygame.locals
import sys
import time
pygame.init()

FPS = 30
clock = pygame.time.Clock()

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
DarkGrey = (50, 50, 50)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Screen
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
screen.fill(DarkGrey)
pygame.display.set_caption("GAME")


# Loading images
BlueWizard = pygame.image.load("Blue Wizard.png")
BlueWizardPre = pygame.image.load("Blue Wizard Pre-Attack.png")
BlueWizardAttack = pygame.image.load("Blue Wizard (Attack).png")
BlueWizardDead = pygame.image.load("Burnt.png")

RedWizard = pygame.image.load("Red Wizard.png")
RedWizardPre = pygame.image.load("Red Wizard Pre-Attack.png")
RedWizardAttack = pygame.image.load("Red Wizard (Attack).png")
RedWizardDead = pygame.image.load("Frozen.png")

Building = pygame.image.load("Building.png")
ice = pygame.image.load("Ice.png")
fire = pygame.image.load("Fire.png")

blueState = "neutral"
redState = "neutral"

timer = 0
startAttackB = 0
StartAttackR = 0

BlueAttack = False
RedAttack = False

icex = 100
icey = 240
firex = 100
firey = 400

def fight(key, blueState, redState, timer, startAttackB, startAttackR):
    screen.fill(grey)
    screen.blit(Building, (20, 320))
    screen.blit(Building, (450, 320))




    if redState == "neutral":
        screen.blit(RedWizard, (400, 214))

    # Red Attack
    if redState == "neutral":
        if key == "left":
            startAttackR = timer
            redState = "pre-attack"

    elif redState == "pre-attack":
        screen.blit(RedWizardPre, (400, 214))
        if (timer - startAttackR) >= 250:
            redState = "attack"

    elif redState == "attack":
        screen.blit(RedWizardAttack, (50, 214))
        if (timer - startAttackR) >= 500:
            redState = "neutral"


#------------------------------------------------------------------------------

    if blueState == "neutral":
        screen.blit(BlueWizard, (50, 214))

    # Blue Attack
    if blueState == "neutral":
        if key == "d":
            startAttackB = timer
            blueState = "pre-attack"

    elif blueState == "pre-attack":
        screen.blit(BlueWizardPre, (50, 214))
        if (timer - startAttackB) >= 250:
            blueState = "attack"

    elif blueState == "attack":
        screen.blit(BlueWizardAttack, (50, 214))
        if (timer - startAttackB) >= 500:
            blueState = "neutral"

    if redState == "dead":
        screen.blit(RedWizardDead, (400, 214))





    return blueState, redState, timer, startAttackB, StartAttackR



# Main Loop
running = True
while True:
    key = "none"
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                key = "d"
            elif event.key == pygame.K_a:
                key = "a"
            elif event.key == pygame.K_LEFT:
                key = "left"
    blueState, redState, timer, startAttackB, startAttackR = fight(key, blueState, redState, timer, startAttackB, StartAttackR)






    if blueState == "attack":
        BlueAttack = True
    if BlueAttack == True:
        icex += 4
        screen.blit(ice, (icex, icey))

        if icex >= 420:
            BlueAttack = False
            icex = 100
            redState = "dead"

    if redState == "attack":
        RedAttack = True
    if RedAttack == True:
        firex -= 4
        screen.blit(fire, (firex, firey))

        if firex >= 420:
            BlueAttack = False
            firex = 100
            blueState = "dead"





    # Testing Values
    print(blueState, redState)

    timer = pygame.time.get_ticks()
    pygame.display.update()
    clock.tick(FPS)


