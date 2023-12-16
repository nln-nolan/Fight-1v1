# ╔═══════════════HI═════════════════╗
# ║    Hi user, welcome to my game   ║
# ╠═════════════CREATOR══════════════╣
# ║    Original code by nln.nolan    ║
# ╠══════════════DATE════════════════╣
# ║      Created on 15/12/2023       ║
# ╚══════════════════════════════════╝

# Import
from kandinsky import *
from ion import *
from time import *

# -- Color --
_colorBlack = (0,0,0)
_colorWhite = (255,255,255)

_colorPlayer = (100,100,100)
_colorMissile = (180,10,0)
_colorLife = (225,0,0)
_colorLifeBarBackground = (100,100,100)

_colorWinnerBackground = (100,100,100)

def Play():
  # -- Var --
  # Player Left
  # Position
  xPlayerLeft = 10
  yPlayerLeft = 100

  # Player Right
  # Position
  xPlayerRight = 300
  yPlayerRight = 100

  # Size Players Hauteur
  HSizePlayer = 20
  # Size Players Largeur
  LSizePlayer = 10

  # Size Missile Hauteur
  HSizeMissile = 10
  # Size Missile Largeur
  LSizeMissile = 10

  # Life
  global lifePlayerLeft
  global lifePlayerRight
  lifePlayerLeft = 3
  lifePlayerRight = 3

  speed = 1

  winner = 0

  # Background
  fill_rect(0,0,500,500,_colorWhite)

  # Life
  fill_rect(0,0,400,18,_colorLifeBarBackground)
  fill_rect(0,18,400,2,_colorBlack)

  fill_rect(10,4,15,11,_colorLife)
  fill_rect(30,4,15,11,_colorLife)
  fill_rect(50,4,15,11,_colorLife)

  fill_rect(295,4,15,11,_colorLife)
  fill_rect(275,4,15,11,_colorLife)
  fill_rect(255,4,15,11,_colorLife)

  draw_string("Life",140,0,(255,255,255),(100,100,100))

  while winner == 0:
    # Erase Player Left
    fill_rect(xPlayerLeft,yPlayerLeft+HSizePlayer,LSizePlayer,2,_colorWhite)
    fill_rect(xPlayerLeft,yPlayerLeft-2,LSizePlayer,2,_colorWhite)
    # Draw Players Left
    fill_rect(xPlayerLeft,yPlayerLeft,LSizePlayer,HSizePlayer,_colorPlayer)

    # Erase Player Right
    fill_rect(xPlayerRight,yPlayerRight+HSizePlayer,LSizePlayer,2,_colorWhite)
    fill_rect(xPlayerRight,yPlayerRight-2,LSizePlayer,2,_colorWhite)
    # Draw Players Right
    fill_rect(xPlayerRight,yPlayerRight,LSizePlayer,HSizePlayer,_colorPlayer)

    # Missile Left
    # Position
    xMissilePlayerLeft = xPlayerLeft
    yMissilePlayerLeft = yPlayerLeft+5

    # Missile Right
    # Position
    xMissilePlayerRight = xPlayerRight
    yMissilePlayerRight = yPlayerRight+5

    # Border Player Left
    if yPlayerLeft == 21:
      yPlayerLeft += 1
      fill_rect(0,18,400,2,(0,0,0))
    if yPlayerLeft == 202:
      yPlayerLeft -= 1
    # Border Player Right
    if yPlayerRight == 21:
      yPlayerRight += 1
      fill_rect(0,18,400,2,(0,0,0))
    if yPlayerRight == 202:
      yPlayerRight -= 1

    # Movement Player Left
    if keydown(KEY_SEVEN):
      yPlayerLeft -= speed
    if keydown(KEY_ONE):
      yPlayerLeft += speed

    # Movement Player Right
    if keydown(KEY_RIGHTPARENTHESIS):
      yPlayerRight -= speed
    if keydown(KEY_MINUS):
      yPlayerRight += speed

    if keydown(KEY_MULTIPLICATION):
      missileLoop = 0
      while missileLoop < 97:
        fill_rect(xMissilePlayerRight,yMissilePlayerRight,LSizeMissile,HSizeMissile,_colorMissile)
        fill_rect(xMissilePlayerRight+15,yMissilePlayerRight,LSizeMissile,HSizeMissile,_colorWhite)

        xMissilePlayerRight -= 3

        # Erase Player Left
        fill_rect(xPlayerLeft,yPlayerLeft+HSizePlayer,LSizePlayer,2,_colorWhite)
        fill_rect(xPlayerLeft,yPlayerLeft-2,LSizePlayer,2,_colorWhite)
        # Draw Players Left
        fill_rect(xPlayerLeft,yPlayerLeft,LSizePlayer,HSizePlayer,_colorPlayer)

        # Erase Player Right
        fill_rect(xPlayerRight,yPlayerRight+HSizePlayer,LSizePlayer,2,_colorWhite)
        fill_rect(xPlayerRight,yPlayerRight-2,LSizePlayer,2,_colorWhite)
        # Draw Players Right
        fill_rect(xPlayerRight,yPlayerRight,LSizePlayer,HSizePlayer,_colorPlayer)

        # Border Player Left
        if yPlayerLeft == 21:
          yPlayerLeft += 1
          fill_rect(0,18,400,2,(0,0,0))
        if yPlayerLeft == 202:
          yPlayerLeft -= 1
        # Border Player Right
        if yPlayerRight == 21:
          yPlayerRight += 1
          fill_rect(0,18,400,2,(0,0,0))
        if yPlayerRight == 202:
          yPlayerRight -= 1

        # Movement Player Left
        if keydown(KEY_SEVEN):
          yPlayerLeft -= speed
        if keydown(KEY_ONE):
          yPlayerLeft += speed

        # Movement Player Right
        if keydown(KEY_RIGHTPARENTHESIS):
          yPlayerRight -= speed
        if keydown(KEY_MINUS):
          yPlayerRight += speed

        missileLoop += 1

      fill_rect(xMissilePlayerRight,yMissilePlayerRight,20,LSizeMissile,_colorWhite)

      if (
        xMissilePlayerRight <= xPlayerLeft + LSizePlayer
        and xMissilePlayerRight + LSizeMissile >= xPlayerLeft
        and yMissilePlayerRight <= yPlayerLeft + HSizePlayer
        and yMissilePlayerRight + HSizeMissile >= yPlayerLeft
      ):
        lifePlayerRight -= 1

    if keydown(KEY_FIVE):
      missileLoop = 0
      while missileLoop < 97:
        fill_rect(xMissilePlayerLeft,yMissilePlayerLeft,LSizeMissile,HSizeMissile,_colorMissile)
        fill_rect(xMissilePlayerLeft-15,yMissilePlayerLeft,LSizeMissile,HSizeMissile,_colorWhite)

        xMissilePlayerLeft += 3

        # Erase Player Left
        fill_rect(xPlayerLeft,yPlayerLeft+HSizePlayer,LSizePlayer,2,_colorWhite)
        fill_rect(xPlayerLeft,yPlayerLeft-2,LSizePlayer,2,_colorWhite)
        # Draw Players Left
        fill_rect(xPlayerLeft,yPlayerLeft,LSizePlayer,HSizePlayer,_colorPlayer)

        # Erase Player Right
        fill_rect(xPlayerRight,yPlayerRight+HSizePlayer,LSizePlayer,2,_colorWhite)
        fill_rect(xPlayerRight,yPlayerRight-2,LSizePlayer,2,_colorWhite)
        # Draw Players Right
        fill_rect(xPlayerRight,yPlayerRight,LSizePlayer,HSizePlayer,_colorPlayer)

        # Border Player Left
        if yPlayerLeft == 21:
          yPlayerLeft += 1
          fill_rect(0,18,400,2,(0,0,0))
        if yPlayerLeft == 202:
          yPlayerLeft -= 1
        # Border Player Right
        if yPlayerRight == 21:
          yPlayerRight += 1
          fill_rect(0,18,400,2,(0,0,0))
        if yPlayerRight == 202:
          yPlayerRight -= 1

        # Movement Player Left
        if keydown(KEY_SEVEN):
          yPlayerLeft -= speed
        if keydown(KEY_ONE):
          yPlayerLeft += speed

        # Movement Player Right
        if keydown(KEY_RIGHTPARENTHESIS):
          yPlayerRight -= speed
        if keydown(KEY_MINUS):
          yPlayerRight += speed


        missileLoop += 1
      
      xMissilePlayerLeft -= 10
      fill_rect(xMissilePlayerLeft,yMissilePlayerLeft,20,LSizeMissile,_colorWhite)

      if (
        xMissilePlayerLeft + LSizeMissile >= xPlayerRight
        and xMissilePlayerLeft <= xPlayerRight + LSizePlayer
        and yMissilePlayerLeft + HSizeMissile >= yPlayerRight
        and yMissilePlayerLeft <= yPlayerRight + HSizePlayer
      ):
        lifePlayerLeft -= 1

    # Life Player Left
    if lifePlayerLeft == 3:
      fill_rect(295,4,15,11,_colorLife)
      fill_rect(275,4,15,11,_colorLife)
      fill_rect(255,4,15,11,_colorLife)
    if lifePlayerLeft == 2:      
      fill_rect(295,4,15,11,_colorLife)
      fill_rect(275,4,15,11,_colorLife)
      fill_rect(255,4,15,11,_colorLifeBarBackground)
    if lifePlayerLeft == 1:      
      fill_rect(295,4,15,11,_colorLife)
      fill_rect(275,4,15,11,_colorLifeBarBackground)
      fill_rect(255,4,15,11,_colorLifeBarBackground)
    if lifePlayerLeft == 0:
      winner = 1
      Winner()

    # Life Player Right
    if lifePlayerLeft > 0:
      if lifePlayerRight == 3:
        fill_rect(10,4,15,11,_colorLife)
        fill_rect(30,4,15,11,_colorLife)
        fill_rect(50,4,15,11,_colorLife)
      if lifePlayerRight == 2:      
        fill_rect(10,4,15,11,_colorLife)
        fill_rect(30,4,15,11,_colorLife)
        fill_rect(50,4,15,11,_colorLifeBarBackground)
      if lifePlayerRight == 1:      
        fill_rect(10,4,15,11,_colorLife)
        fill_rect(30,4,15,11,_colorLifeBarBackground)
        fill_rect(50,4,15,11,_colorLifeBarBackground)
      if lifePlayerRight == 0:
        winner = 1
        Winner()

def Winner():
  fill_rect(0,0,500,500,_colorWinnerBackground)

  if lifePlayerLeft == 0:
    draw_string("Player Left Win",80,60,_colorWhite,_colorWinnerBackground)
  elif lifePlayerRight == 0:
    draw_string("Player Right Win",80,60,_colorWhite,_colorWinnerBackground)
  else:
    draw_string("Error",135,100,_colorWhite,_colorWinnerBackground)


  draw_string("Press OK for restart",60,110,_colorWhite,_colorWinnerBackground)

  draw_string("By nln.nolan",100,200,_colorWhite,_colorWinnerBackground)

  pressOK = 1

  while pressOK == 1:
    if keydown(KEY_OK):
      pressOK = 0
      Play()

Play()