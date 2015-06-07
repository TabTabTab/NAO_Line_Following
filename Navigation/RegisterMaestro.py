from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule


#all functions below requires a broker to be registered


def registerPostureProxy():
	postureProxy=False
	#connect to posture
	try:
		postureProxy = ALProxy("ALRobotPosture")
		return postureProxy
	except Exception, e:
		print "Could not create proxy to ALRobotPosture"
    	print "Error was: ", e
    	postureProxy=False
    	return postureProxy

def registerMotionProxy():
	motionProxy=False
	#connect to posture
	try:
		motionProxy = ALProxy("ALMotion")
		return motionProxy
	except Exception, e:
		print "Could not create proxy to ALMotion"
    	print "Error was: ", e
    	motionProxy=False
    	return motionProxy

def registerMemoryProxy():
	memoryProxy=False
	#connect to posture
	try:
		memoryProxy = ALProxy("ALMemory")
		return memoryProxy
	except Exception, e:
		print "Could not create proxy to ALMemory"
    	print "Error was: ", e
    	memoryProxy=False
    	return memoryProxy


def registerSonarProxy():
	sonarProxy=False
	#connect to posture
	try:
		sonarProxy = ALProxy("ALSonar")
		return sonarProxy
	except Exception, e:
		print "Could not create proxy to ALSonar"
    	print "Error was: ", e
    	sonarProxy=False
    	return sonarProxy