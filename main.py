import pygame

# initialize the pygame object
pygame.init()

# title and window settings
pygame.display.set_caption("Bouncy Ball")
pygame.display.set_icon(pygame.image.load("IconNoBG.png"))

# create 1024x1024 window
window = pygame.display.set_mode((1024, 1024))

# bouncy ball icon and "floor" coordinate arrays
iconArray = ["ballSize1.png", "ballSize2.png", "ballSize3.png"]
floorArray = [923, 873, 823]
bouncyBall = pygame.image.load(iconArray[0])
floorCoordinate = floorArray[0]

# bouncy ball default variables
bouncyBallX = 487
bouncyBallY = 487
bounceFactor = -0.75


# acceleration and velocity. Acceleration is amplified by a factor of 1000
XAcceleration = 0
YAcceleration = 9810
XVelocity = 0
YVelocity = 0

# tracking variables
ballStopped = False
clickDebugFlag = False
timeLastUpdate = 0


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
        elif event.type == pygame.KEYDOWN:
            # if key is pressed to change ball type, change sprite and floor coordinate
            # and reset and center ball position as to handle edge case of size changing
            # when the ball is already on the floor.
            if event.key == pygame.K_1:
                bouncyBall = pygame.image.load(iconArray[0])
                floorCoordinate = floorArray[0]
                bouncyBallX = 487
                bouncyBallY = 487
            elif event.key == pygame.K_2:
                bouncyBall = pygame.image.load(iconArray[1])
                floorCoordinate = floorArray[1]
                bouncyBallX = 462
                bouncyBallY = 487
            elif event.key == pygame.K_3:
                bouncyBall = pygame.image.load(iconArray[2])
                floorCoordinate = floorArray[2]
                bouncyBallX = 437
                bouncyBallY = 487
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
    if bouncyBallY >= floorCoordinate + 1 and not ballStopped:
        if abs(YVelocity) < 500:
            # this is to make sure we don't trigger the bounce logic over and over again at low velocity
            ballStopped = True
            bouncyBallY = floorCoordinate
            YVelocity = 0
        else:
            bouncyBallY = floorCoordinate

            timeLastUpdate = pygame.time.get_ticks()
            YVelocity = YVelocity * bounceFactor