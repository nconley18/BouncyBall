import pygame

# initialize the pygame object
pygame.init()

# title and window settings
pygame.display.set_caption("Bouncy Ball")
pygame.display.set_icon(pygame.image.load("IconNoBG.png"))

# create 1024x1024 window
window = pygame.display.set_mode((1024, 1024))

# bouncy ball icon
bouncyBall = pygame.image.load("ballSize1.png")
bouncyBallX = 487
bouncyBallY = 487
ballStopped = False
clickDebugFlag = False


XVelocity = 0
YVelocity = 0
timeLastUpdate = 0

# acceleration assuming 1 pixel == 0.125 meter
XAcceleration = 0
YAcceleration = 9810


# tracking when the user asks to exit the game
quitFlag = False


def ball(x, y):
    window.blit(bouncyBall, (x, y))


# basic game loop
while not quitFlag:
    # setting background of the program to light gray
    window.fill((150, 150, 150))

    # game loop that processes events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitFlag = True
        elif event.type == pygame.MOUSEBUTTONUP:
            bouncyBallX, bouncyBallY = pygame.mouse.get_pos()
            # centering sprite
            bouncyBallX -= 50
            bouncyBallY -= 50
            ballStopped = False
            YVelocity = 0
            timeLastUpdate = pygame.time.get_ticks()
            clickDebugFlag = True
        else:
            continue

    ball(bouncyBallX, bouncyBallY)
    pygame.display.update()

    if not ballStopped:
        # update acceleration, velocity, and coordinates
        # velocity = acceleration * milliseconds passed in second format
        YVelocity += YAcceleration * ((timeLastUpdate - pygame.time.get_ticks()) / 1000)
        bouncyBallY += YVelocity * ((timeLastUpdate - pygame.time.get_ticks()) / 1000)
        if clickDebugFlag:
            print(f"Velocity after click is: {YVelocity}")
            print(f"Acceleration after click is: {YAcceleration}")
            print(f"timeLastUpdate is {timeLastUpdate} and gametime is {pygame.time.get_ticks()}")
            clickDebugFlag = False
        timeLastUpdate = pygame.time.get_ticks()
    else:
        continue

    # if ball has hit the bottom of the frame... (1024 pixels - sprite is 100 pixels tall)
    if bouncyBallY >= 924 and not ballStopped:
        if abs(YVelocity) < 500:
            # this is to make sure we don't trigger the bounce logic over and over again at low velocity
            ballStopped = True
            bouncyBallY = 923
            YVelocity = 0
        else:
            bouncyBallY = 923

            timeLastUpdate = pygame.time.get_ticks()
            YVelocity = YVelocity * -0.75