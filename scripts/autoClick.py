# Autoclicker.py 
# --------------
# Need to manually convert NSPoint integers into a seperate array of (x, y) coordinates
# Need to manually define the actions list


import sys
import os
import time
from Quartz.CoreGraphics import *
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import CGEventCreate
from Quartz.CoreGraphics import CGEventGetLocation

#Action Script for Deleting SNS Topics
# <NSPoint x=212.4453125 y=386.37109375>
# <NSPoint x=433.63671875 y=231.41796875>
# <NSPoint x=397.84765625 y=285.25390625>
# <NSPoint x=662.17578125 y=435.25390625>


#Find coordinates of Mouse Clicks
actions=[(212,386), (433,231), (397, 285), (662, 435)]

#Type of event
def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)

#Move the mouse
def mousemove(posx,posy):
    mouseEvent(kCGEventMouseMoved, posx,posy)

#Click
def mouseclick(posx,posy):
    mouseEvent(kCGEventLeftMouseDown, posx,posy)
    mouseEvent(kCGEventLeftMouseUp, posx,posy)

#We need to set the mouse locations for script
def getMouseLocation():
	ourEvent = CGEventCreate(None)
	currentPos = CGEventGetLocation(ourEvent)
	print(currentPos)
	return currentPos

def helloWorld():
	print("Ok listening")

def listenForPos():
	#When enter is pressed, get MouseLocation
	raw_input('Move mouse to location, hit any key to get location')
	helloWorld()
	print("Ok listening")
	EventPoint = getMouseLocation()
	#How doy ou convert NSPoint to ints?????

	return EventPoint

def setActionScript(repeat):
	actionCoor = [] #Coordinates for mouse
	for x in range(0, repeat):
		actionCoor.append(listenForPos())
	return actionCoor



def main():
	ourEvent = CGEventCreate(None) #Save current mouse location
	currentPos = CGEventGetLocation(ourEvent)
	print("clicking")

	#Manually setting the clicks
	mouseclick(actions[0][0],actions[0][1])
	time.sleep(.25)
	mouseclick(actions[1][0],actions[1][1])	
	time.sleep(.125)
	mouseclick(actions[2][0],actions[2][1])	
	time.sleep(.125)
	mouseclick(actions[3][0],actions[3][1])	
	time.sleep(.20)



	mousemove(int(currentPos.x), int(currentPos.y))
	if __name__ == '__main__':
		main()





def timeElapse():
	start = time.time()
	print "hello"
	end = time.time()
	print end - start


