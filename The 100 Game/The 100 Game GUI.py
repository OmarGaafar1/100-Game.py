import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600,))
Game_running = True

# BackGround Img
background = pygame.image.load("wooden_background_board_65898_800x600 222.jpg")

# Title and icon
pygame.display.set_caption("100 Game")
icon = pygame.image.load("number-blocks.png")
pygame.display.set_icon(icon)

# Digit One 1 !
oneImg = pygame.image.load("one (1).png")
oneX = 150
oneY = 50
oneX_change = 0


def Digit_One(x, y):
    screen.blit(oneImg, (x, y))


# Digit Two !
twoImg = pygame.image.load("two.png")
twoX = 250
twoY = 50


def Digit_Two(x, y):
    screen.blit(twoImg, (x, y))


# Digit Three !
threeImg = pygame.image.load("three.png")
threeX = 350
threeY = 50


def Digit_Three(x, y):
    screen.blit(threeImg, (x, y))


# Digit Four !
fourImg = pygame.image.load("four.png")
fourX = 450
fourY = 50


def Digit_Four(x, y):
    screen.blit(fourImg, (x, y))


# Digit Five !
fiveImg = pygame.image.load("five.png")
fiveX = 550
fiveY = 50


def Digit_Five(x, y):
    screen.blit(fiveImg, (x, y))


# Digit Six !
sixImg = pygame.image.load("six.png")
sixX = 150
sixY = 120


def Digit_Six(x, y):
    screen.blit(sixImg, (x, y))


# Digit seven !
sevenImg = pygame.image.load("seven.png")
sevenX = 250
sevenY = 120


def Digit_Seven(x, y):
    screen.blit(sevenImg, (x, y))


# Digit Eight !
eightImg = pygame.image.load("eight.png")
eightX = 350
eightY = 120


def Digit_Eight(x, y):
    screen.blit(eightImg, (x, y))


# Digit Nine !
nineImg = pygame.image.load("nine.png")
nineX = 450
nineY = 120


def Digit_Nine(x, y):
    screen.blit(nineImg, (x, y))


def instructors():
    instructors_text = pygame.font.Font('OpenSans-Bold.ttf', 20)
    text = instructors_text.render("Input numbers using the keyboard, whoever reaches 100 wins : ", True, (0,0, 0))
    screen.blit(text, (5, 250))




# Displaying the score_value
score_value = 0
score_text = pygame.font.Font('yankclipper2.ttf', 44)
scoreX = 350
scoreY = 450


def show_score(x, y):
    game = score_text.render("Current score: " + str(score_value), True, (255, 0, 0))
    screen.blit(game, (x, y))


# Displaying the player Turn
current_player = "Player_One"
turns = pygame.font.Font('yankclipper2.ttf', 44)
turnsX = 0
turnsY = 350


def player_turn(x, y):
    turn = score_text.render("Current Turn: " + str(current_player), True, (255, 0, 0))
    screen.blit(turn, (x, y))


def Winner():
    global Game_running
    background_new = pygame.image.load("Game over.jpg")
    if current_player == "Player_Two" and score_value == 100:
        winner_text = pygame.font.Font('yankclipper2.ttf', 50)
        winner = winner_text.render("Player One Wins !! ", True, (255, 0, 0))
        screen.blit(background_new, (0, 0))
        screen.blit(winner, (275, 290))
        Game_running = False
    if current_player == "Player_One" and score_value == 100:
        winner_text = pygame.font.Font('yankclipper2.ttf', 50)
        winner = winner_text.render("Player Two Wins !! ", True, (255, 0, 0))
        screen.blit(background_new, (0, 0))
        screen.blit(winner, (275, 290))
        Game_running = False
    # Checking for Draw
    if score_value > 100:
        winner_text = pygame.font.Font('yankclipper2.ttf', 50)
        winner = winner_text.render("Draw!!", True, (255, 0, 0))
        screen.blit(background_new, (0, 0))
        screen.blit(winner, (350, 290))
        Game_running = False


while True:
    screen.fill((255, 255, 255))

    mX, mY = pygame.mouse.get_pos()

    # Keyboard Events !

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # checkinng if the user close the program
            exit()
        # Keyboard inputs !
        if Game_running == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # 1 moves to 2
                    a = oneX
                    b = oneY
                    oneX = twoX
                    oneY = twoY
                    twoY = b
                    twoX = a
                    score_value = score_value + 1
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_2:

                    # 2 moves to 6
                    c = twoX
                    d = twoY
                    twoX = sixX
                    twoY = sixY
                    sixX = c
                    sixY = d

                    score_value = score_value + 2
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_3:

                    # 3 moves to 7
                    e = threeX
                    f = threeY
                    threeX = sevenX
                    threeY = sevenY
                    sevenX = e
                    sevenY = f

                    score_value = score_value + 3
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_4:

                    # 4 moves to 9
                    g = fourX
                    h = fourY

                    fourX = nineX
                    fourY = nineY

                    nineX = g
                    nineY = h

                    score_value = score_value + 4
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_5:
                    # 5 moves to 8
                    i = fiveX
                    g = fiveY
                    fiveX = eightX
                    fiveY = eightY
                    eightX = i
                    eightY = g
                    score_value = score_value + 5
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_6:
                    # six moves to nine
                    j = sixX
                    k = sixY
                    sixX = nineX
                    sixY = nineY
                    nineX = j
                    nineY = k
                    score_value = score_value + 6
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_7:
                    # 7 moves to 4
                    l = sevenX
                    m = sevenY
                    sevenX = fourX
                    sevenY = fourY
                    fourX = l
                    fourY = m
                    score_value = score_value + 7
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_8:
                    # 8 moves to 1
                    n = eightX
                    o = eightY
                    eightX = oneX
                    eightY = oneY
                    oneX = n
                    oneY = o
                    score_value = score_value + 8
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"
                if event.key == pygame.K_9:
                    # 9 moves to 5
                    p = nineX
                    q = nineY
                    nineX = fiveX
                    nineY = fiveY
                    fiveX = p
                    fiveY = q

                    score_value = score_value + 9
                    if current_player == "Player_One":
                        current_player = "Player_Two"
                    else:
                        current_player = "Player_One"

    screen.blit(background, (0, 0))
    Digit_One(oneX, oneY)
    Digit_Two(twoX, twoY)
    Digit_Three(threeX, threeY)
    Digit_Four(fourX, fourY)
    Digit_Five(fiveX, fiveY)
    Digit_Six(sixX, sixY)
    Digit_Seven(sevenX, sevenY)
    Digit_Eight(eightX, eightY)
    Digit_Nine(nineX, nineY)
    show_score(scoreX, scoreY)
    player_turn(turnsX, turnsY)
    instructors()
    Winner()

    pygame.display.update()
