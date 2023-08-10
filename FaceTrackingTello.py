from utils import *
import cv2

drone = initialize_tello()
width, height = 480, 360

while True:
    ## Step 1 getting the image from drone camera 
    img = tello_get_frame(drone, width, height)
    # print(img)
    cv2.imshow('Image', img)


    ## Step 2 Finding a face
    img = find_face(img)

    ## stopping the drone
    if cv2.waitKey(1) and 0xFF == ord('q'):
        drone.land()
        break