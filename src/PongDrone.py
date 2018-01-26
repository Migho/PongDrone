import time             # For thread sleeping
import ps_drone         # Library for drone control
import cv2              # Computer vision library
import numpy as np      # Contains useful math methods

# Drone startup
drone = ps_drone.Drone()
drone.startup()
drone.reset()

# Some mandatory drone config.
while (drone.getBattery()[0] == -1): time.sleep(0.1)
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])
drone.useDemoMode(True)
drone.setConfigAllID()
drone.sdVideo()
drone.frontCam()
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount: time.sleep(0.0001)
drone.startVideo()
drone.showVideo()
drone.groundCam()

# We don't want the drone to fly to the ceiling
drone.setConfig("control:altitude max", 2000)

# In case we wan't to save the video...
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fileName = "output" + str(time.time()) + '.mp4'
out = cv2.VideoWriter(fileName, fourcc, 15.0, (640,360))
# UI stuff
font = cv2.FONT_HERSHEY_SIMPLEX

# Target area size. Center of the screen is (0,0)
targetXaxisFix = 0
targetYaxisFix = -20
targetXaxisSize = 50
targetYaxisSize = 50

# Speed limits and other settings
movementSpeed = 0.08
stabilizeTime = 1
requiredAcquireTime = 1
MaxCyclesToSkip = 3

# Other variables (do not change)
targetAcquired = False
cyclesSkipped = 0
IMC = drone.VideoImageCount

drone.takeoff()

### WAIT AND MANUAL CONTROL ###
def wait(seconds):
    manualControl = False
    mstarget = int(round((time.time() + seconds) * 1000))
    IMC = drone.VideoImageCount
    while mstarget > int(round(time.time() * 1000)) or manualControl:
        pressedKey = drone.getKey()
        if manualControl:
            # Manual control settings
            if pressedKey is '8': drone.moveForward(0.2)
            elif pressedKey is '2': drone.moveBackward(0.2)
            elif pressedKey is '4': drone.moveLeft(0.2)
            elif pressedKey is '6': drone.moveRight(0.2)
            elif pressedKey is '7': drone.turnLeft(0.2)
            elif pressedKey is '9': drone.turnRight(0.2)
            elif pressedKey is '+': drone.moveUp(0.2)
            elif pressedKey is '-': drone.moveDown(0.2)
            elif pressedKey is '5': drone.stop()
            elif pressedKey is '/':
                print "MANUAL CONTROL OFF"
                manualControl = False
            #else:
                #drone.moveForward(0)
        elif pressedKey is 'm':
            print "MANUAL CONTROL ON"
            manualControl = True
        # Stop if q is pressed
        if pressedKey is 'q':
            drone.stop()
            return True
    return False

### PROGRAM AND BRAINS ###
while True:
    # Don't load same frames twice
    while drone.VideoImageCount == IMC: time.sleep(0.01)
    IMC = drone.VideoImageCount
    frame = drone.VideoImage

    # Circle detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,5)
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,minDist=100,param1=48,param2=42,minRadius=20,maxRadius=200)

    # The magic!
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        targetCircleDistance = 999
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (255, 0, 255), 2)  # circle drawing
            if np.sqrt(x*x+y*y) < targetCircleDistance:     # Spotting the most center circle
                targetCircleDistance = np.sqrt(x*x+y*y)
                targetCircle = x, y
        
        # Moving according to the circles. Screen size is 640 x 360
        leftRight = round((targetCircle[0]-320)/320.0/4, 3)
        backwardForward = -round((targetCircle[1]-180)/180.0/4, 3)
        
        # Calculate where to move, if we need to
        if targetCircle[0]-320-targetXaxisFix > targetXaxisSize/2:
            leftRight = movementSpeed
        elif targetCircle[0]-320-targetXaxisFix < -targetXaxisSize/2:
            leftRight = -movementSpeed
        else: leftRight = 0
        if targetCircle[1]-180-targetYaxisFix > targetYaxisSize/2:
            backwardForward = movementSpeed
        elif targetCircle[1]-180-targetYaxisFix < -targetYaxisSize/2:
            backwardForward = -movementSpeed
        else: backwardForward = 0
        
        # Move or not?
        if backwardForward is 0 and leftRight is 0:
            if targetAcquired:
                if time.time() > targetAcquiredTime+requiredAcquireTime:
                    print "DO THE FLIP!!"
                    drone.anim(17, 0.5)
                    wait(9999)
            else:
                targetAcquiredTime = time.time()
                targetAcquired = True
        # Sometimes we miss the original circle and find a new one somewhere else. In these cases we don't want to move.
        elif targetAcquired and cyclesSkipped <= MaxCyclesToSkip:
            backwardForward = 0
            leftRight = 0
            cyclesSkipped = cyclesSkipped + 1
        else:
            targetAcquired = False
            cyclesSkipped = 0

        ## MOVE PAINTING ##
        # Paint the movements
        text = "RIGHT " + str(leftRight) + "%"
        cv2.putText(frame, text, (0, 30), font, 1, (255,255,255), 2, cv2.LINE_AA)
        text = "FORW. " + str(backwardForward) + "%"
        cv2.putText(frame, text, (320, 30), font, 1, (255,255,255), 2, cv2.LINE_AA)
        # Paint the target area
        cv2.rectangle(frame,(320+targetXaxisFix-targetXaxisSize/2,180+targetYaxisFix-targetYaxisSize/2),(320+targetXaxisFix+targetXaxisSize/2,180+targetYaxisFix+targetYaxisSize/2),(0,255,0),3)
        # Show the frame
        cv2.imshow("Computer", frame)
        out.write(frame)
        cv2.waitKey(1)

        # Movement and the time to move and stabilize. Theoretical maximium value we can get from the values is 180.
        drone.move(leftRight, backwardForward, 0, 0)
        if wait(min(abs(targetCircle[1]-180-targetYaxisFix), abs(targetCircle[1]-180-targetYaxisFix))/200):
            break
        drone.stop()
        if wait(stabilizeTime):
            break
        
    if wait(0.05):
        break
    drone.stop()

drone.shutdown()
cv2.destroyAllWindows()