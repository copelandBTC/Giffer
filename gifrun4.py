import pyglet
import subprocess
import time
import math
import random
import os

win = pyglet.window.Window(fullscreen = True)
interm = "static.gif"
#gif_set = ["creepy.gif", "mew.gif", "mob.gif", "glob.gif", "mewtwo.gif", "shroom.gif", "ssj3goku.gif", "wiz.gif"]

def chooseRandGif():
	return random.choice(os.listdir("/home/bc/scripts/giffer/gifs/"))

curGif = chooseRandGif()
animation = pyglet.resource.animation(curGif)

def getResolution():
	output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
	output = str(output).strip("b'")
	output = output.strip("\\n")
	resolution = output.split("x")

	resolution[0] = int(resolution[0])
	resolution[1] = int(resolution[1])

	return resolution

res = getResolution()
sprite = pyglet.sprite.Sprite(animation)

def fitSprite():
	#sprite.scale = math.sqrt(((res[0] / sprite.width)**2) + ((res[1] / sprite.height)**2)) * 0.75
	sprite._set_scale_x(res[0] / sprite._get_width())
	sprite._set_scale_y(res[1] / sprite._get_height())


def swapGif():
	global startTime
	global curGif
	global animation
	global sprite

	#intermission
	if curGif is not interm:
		curGif = interm
		animation = pyglet.resource.animation(interm)
		sprite = pyglet.sprite.Sprite(animation)
		fitSprite()
		startTime = time.time() - 14
			
	else:
		#new gif
		curGif = chooseRandGif()
		animation = pyglet.resource.animation(curGif)
		sprite = pyglet.sprite.Sprite(animation)
		fitSprite()
		startTime = time.time()

fitSprite()

@win.event
def on_draw():
	global startTime

	win.clear()
	sprite.draw()

	#Swap gif
	if time.time() > startTime + 15:
		swapGif()

"""
This needs to be here right before the beginning of the 
program so that it can capture the starting time right before execution
"""

startTime = time.time()
		
pyglet.app.run()


