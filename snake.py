# A simple Snake game for a 8 x 5 NeoPixel shield
# (c) 2017 Bas van der Sluis

import sys,tty,termios,os,signal
import time,datetime

from threading import Thread
from time import sleep
from random import randint
from neopixel import *

# LED strip configuration:
LED_COUNT      = 40      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 80      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

oSnakeColor = Color(255, 0, 0)
oCandyColor = Color(0, 255, 0)

aSnake = [19, 20]
iDirection = 1
iCandy = False
bExit = False

aRightBorder = [7, 15, 23, 31, 39]
aLeftBorder = [0, 8, 16, 24, 32]

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
	global iDirection

        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                iDirection = 4
        elif k=='\x1b[B':
                iDirection = 2
        elif k=='\x1b[C':
                iDirection = 1
        elif k=='\x1b[D':
                iDirection = 3


def gameInterval():
	moveSnake();
	displaySnakeAndCandy();
	sleep(0.7)
	gameInterval()

def placeNewCandy():
	global iCandy
	iPos = randint(0,39)
	if iPos in aSnake:
		placeNewCandy()
		return
	iCandy = iPos


def moveSnake():
	iHead = aSnake[(len(aSnake) - 1)]
	if iDirection == 1:
		if (isPosFree(iHead + 1) == False) or (iHead in aRightBorder):
			dieSnakeDIE()
			return
		aSnake.append(iHead + 1)

	elif iDirection == 2:
		iNewPos = iHead + 8
		if (iNewPos > 39) or (isPosFree(iNewPos) == False):
			dieSnakeDIE()
			return
		aSnake.append(iNewPos)

	elif iDirection == 3:
		if (isPosFree(iHead - 1) == False) or (iHead in aLeftBorder):
			dieSnakeDIE()
			return
		aSnake.append(iHead - 1)

	elif iDirection == 4:
		iNewPos = iHead - 8
		if (iNewPos < 0) or (isPosFree(iNewPos) == False):
			dieSnakeDIE()
			return
		aSnake.append(iNewPos)

	iHead = aSnake[(len(aSnake) - 1)]
	if iHead == iCandy:
		placeNewCandy()
		return

	aSnake.pop(0)

def isPosFree(iPos):
	if iPos in aSnake:
		return False
	return True


def displaySnakeAndCandy():
	strip.begin()
	for i in aSnake:
		strip.setPixelColor(i, oSnakeColor)
	strip.setPixelColor(iCandy, oCandyColor)
	strip.show()

def dieSnakeDIE():
	global bExit
	print "You lost!"
	bExit = True
	sys.exit()

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	placeNewCandy()
	myThread = Thread(target=gameInterval)
	myThread.start()
	while True:
		if bExit == True:
			break;
		get()

