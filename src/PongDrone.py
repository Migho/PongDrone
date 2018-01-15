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
drone.setConfig("control:altitude max", 1000)

# In case we wan't to save the video...
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 15.0, (640,360))

font = cv2.FONT_HERSHEY_SIMPLEX

drone.takeoff()

### WAIT AND MANUAL CONTROL ###
def wait(seconds):
    manualControl = False
    mstarget = int(round((time.time() + seconds) * 1000))
    IMC = drone.VideoImageCount
    while mstarget > int(round(time.time() * 1000)) or manualControl:
        # Don't load same frames twice
        while drone.VideoImageCount == IMC: time.sleep(0.01)
        IMC = drone.VideoImageCount
        frame = drone.VideoImage
        cv2.imshow("Frame", frame)
        out.write(frame)

        pressedKey = drone.getKey()
        if pressedKey is 'p':
            print "DO THE FLIP!!"
            drone.anim(17, 0.5)
        elif manualControl:
            # Manual control settings
            if pressedKey is 'e': drone.moveForward(0.3)
            elif pressedKey is 'd': drone.moveBackward(0.3)
            elif pressedKey is 's': drone.moveLeft(0.3)
            elif pressedKey is 'f': drone.moveRight(0.3)
            elif pressedKey is 'w': drone.turnLeft(0.3)
            elif pressedKey is 'r': drone.turnRight(0.3)
            elif pressedKey is 't': drone.moveUp(0.3)
            elif pressedKey is 'g': drone.moveDown(0.3)
            elif pressedKey is 'n':
                print "MANUAL CONTROL OFF"
                manualControl = False
            else:
                drone.moveForward(0)
        elif pressedKey is 'm':
            print "MANUAL CONTROL ON"
            manualControl = True
        # Stop if q is pressed
        if pressedKey is 'q':
            return True
    return False

### PROGRAM AND BRAINS ###
IMC = drone.VideoImageCount
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

        # Painting the move..
        text = "RIGHT " + str(leftRight) + "%"
        cv2.putText(frame, text, (0, 30), font, 1, (255,255,255), 2, cv2.LINE_AA)
        text = "FORW. " + str(backwardForward) + "%"
        cv2.putText(frame, text, (320, 30), font, 1, (255,255,255), 2, cv2.LINE_AA)

        drone.move(leftRight, backwardForward, 0, 0)
        cv2.imshow("Frame", frame)
        out.write(frame)
        if wait(abs(leftRight) + abs(backwardForward)):
            break
        
    drone.stop()
    if wait(0.3):
        break

cv2.destroyAllWindows()
drone.shutdown()