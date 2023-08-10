from utils import *
import cv2

drone = initialize_tello()
w, h = 1280, 720

while True:
    ## Step 1 getting the image from drone camera 
    img = telloGetFrame(drone, w, h)
    cv2.imshow('Image', img)

    ## stopping the drone
    if cv2.waitKey(1) and 0xFF == ord('q'):
        drone.land()
        break