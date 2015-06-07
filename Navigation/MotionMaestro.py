from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import time

class MotionMaestro:

	def __init__(self,postureProxy,motionProxy):
		self.postureProxy=postureProxy
		self.motionProxy=motionProxy		

	def standUp(self):
		print "Standing Up"
		self.postureProxy.goToPosture("Stand", 1.0)

	def sitDown(self):
		print "Sitting Down"
		self.postureProxy.goToPosture("Sit", 1.0)
	#anvands ej	
	def startWalking(self):
		self.move(0.5,0.0)

	def continueStraight(self):
		self.stopMove()
		X=1.0
		Y=0
		Theta = 0.0
		Frequency =0.0 # low speed
		self.motionProxy.moveToward(X,Y,Theta)

	def turnLeft(self):
		self.turn(1)
	def turnRight(self):
		self.turn(-1)


	def turn(self,theta):
		self.stopMove()
		x=0.0
		y=0.0
		self.motionProxy.moveToward(x, y, theta)


	def moveLeft(self):
		self.move(0.0,0.5)

	def moveRight(self):
		self.move(0.0,-0.5)

	#anvands ej, set upp sker i navigation controller atm (borde kanske var en egen metod) sen continueStraight
	def move(self,X,Y):
		self.stopMove()
		self.stiffnessOn()
		self.postureProxy.goToPosture("StandInit", 0.5)
		self.motionProxy.setWalkArmsEnabled(True, True)
		Theta = 0.0
		Frequency =0.0 # low speed
		self.motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
	
	def stopMove(self):
		self.motionProxy.stopMove()


	def stiffnessOn(self):
		pNames = "Body"
		pStiffnessLists = 1.0
		pTimeLists = 1.0
		self.motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

