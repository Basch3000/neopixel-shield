# Binary clock for a 8 x 5 NeoPixel shield
# (c) 2017 Bas van der Sluis

import time
import datetime

from neopixel import *
from threading import Timer

# LED strip configuration:
LED_COUNT      = 40      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 80      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

iStartColumn     = 1                 # column where to start (from left to right)
bSpace           = True              # True = space between hours, minutes and seconds, false = no space
oColor           = Color(0, 0, 255)  # Color of each pixel format: (green, red, blue)
oBackgroundColor = Color(0, 0, 10)   # Set this to 0,0,0 if you do not want the inactive leds to light (dimly)

# ColumnSizes are used to determine the size of the column for the background color
aColumnSizes = [0, 2, 8, 4, 8, 4, 8]
if bSpace == True:
	aColumnSizes = [0, 2, 8, 0, 4, 8, 0, 4, 8]

def displayTime():
	strip.begin()

	oDate = datetime.datetime.now()
	sHours = str(oDate.hour)
	sMinutes = str(oDate.minute)
	sSeconds = str(oDate.second)

	displayNumber(iStartColumn, sHours)

	iColumnAdd = 2
	if bSpace == True:
		iColumnAdd = 3

	displayNumber((iStartColumn + iColumnAdd), sMinutes)

	iColumnAdd = 4;
	if bSpace == True:
		iColumnAdd = 6

	displayNumber((iStartColumn + iColumnAdd), sSeconds)
	strip.show()

	Timer(1, displayTime).start()

def displayNumber(iColumn, sNumber):
	if len(sNumber) == 1:
		displayColumn(iColumn, 0)
		displayColumn((iColumn + 1), int(sNumber))
	else:
		displayColumn(iColumn, int(sNumber[0:1]))
		displayColumn((iColumn + 1), int(sNumber[1:]))

def displayColumn(iColumn, iDigit):
	iPos = 32 + (iColumn - 1)

	b = 1
	while b <= 8:
		if iDigit & b:
			strip.setPixelColor(iPos, oColor)
		else:
			if b <= aColumnSizes[iColumn]:
				strip.setPixelColor(iPos, oBackgroundColor)
		iPos -= 8
		b *= 2;

# Main program logic follows:
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	displayTime()

