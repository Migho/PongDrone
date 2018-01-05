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
drone.setConfigAllID()
drone.hdVideo()
drone.frontCam(False)
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount: time.sleep(0.0001)
drone.startVideo()
drone.showVideo()

IMC = drone.VideoImageCount

while True:
    # Don't load same frames twice
    while drone.VideoImageCount == IMC: time.sleep(0.01)
    IMC = drone.VideoImageCount
    frame = drone.VideoImage

    # Circle detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,5)
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,minDist=100,param1=50,param2=50,minRadius=20,maxRadius=200)

    # Circle drawing
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (255, 0, 255), 2)
    
    # Paint the frame
    cv2.imshow("Frame", frame)

    # Stop the loop is q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.shutdown()