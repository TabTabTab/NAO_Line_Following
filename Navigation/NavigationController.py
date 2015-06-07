from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import Tkinter
import os
import math
from sys import argv
from MotionMaestro import MotionMaestro
import RegisterMaestro


#Prompt for ip and port
IP = "192.168.0.101"
PORT = 9559
turning = False

def main():


	try:
		script,IP,PORT = argv
		PORT = int(PORT)
	except:
		print "This program needs the IP and Port of the Nao robot."
		print "Runt it like this 'python NavigataionController.py ip_of_your_nao port_of_your_nao'"
		exit(0)

	# We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
	myBroker = ALBroker("myBroker","0.0.0.0",0,IP,PORT)


	#register proxys
	postureProxy=RegisterMaestro.registerPostureProxy()

	motionProxy=RegisterMaestro.registerMotionProxy()

	#create the walk object
	global motionMaestro
	motionMaestro = MotionMaestro(postureProxy,motionProxy)
#	turning = False

	motionMaestro.stiffnessOn()
	postureProxy.goToPosture("StandInit", 0.5)
	motionProxy.setWalkArmsEnabled(True, True)



	os.system('xset r off')
	root = Tkinter.Tk()
	frame = Tkinter.Frame(root, width=100, height=100)
	frame.bind("<Key>", key_down)
	frame.bind("<KeyRelease>", key_up)
	frame.pack()
	frame.focus_set()
	root.mainloop()
	os.system('xset r on')







def key_up(event):
	if event.keycode == 113 or event.keycode == 114:
		motionMaestro.stopMove()
	#	global turning
	#	turning = False



def key_down(event):
	global turning
	if event.keycode == 111:
	#	print "forward"
		motionMaestro.continueStraight()
	elif event.keycode == 113:
	#	print "turn left"
	#	turning=True
		motionMaestro.turnLeft()
	elif event.keycode == 116:
	#	print "stoping "
		motionMaestro.stopMove()
	elif event.keycode == 114:
	#	print "turn right"
	#	turning=True
		motionMaestro.turnRight() 
	else:
		print "unkown command '"+event.char+"' use the arrow keys to move the robot"

if __name__ == "__main__":
    main()


