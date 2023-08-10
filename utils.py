from djitellopy import Tello
import cv2


def initialize_tello():
    """Initialize DJI Tello Drone."""
    tello_drone = Tello()
    tello_drone.connect()
    
    # zero out other drone velocities
    tello_drone.move_forward = 0
    tello_drone.move_back = 0
    tello_drone.move_left = 0
    tello_drone.move_up = 0
    tello_drone.move_down = 0
    tello_drone.go_xyz_speed = 0
    tello_drone.set_speed = 0
    print(tello_drone.get_battery())
    tello_drone.streamoff
    tello_drone.streamon()
    return tello_drone


def tello_get_frame(drone: Tello, w=360, h=240):
    """Specify frame of the image."""
    backround = drone.get_frame_read()
    frame = backround.frame
    return cv2.resize(frame, (w,h))


def find_face(img):
    """Find faces from drone."""
    # Detect face using algorthim
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Select gray image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Find the faces
    scale_factor = 1.2
    min_neighbors = 4
    faces = faceCascade.detectMultiScale(img_gray, scale_factor, min_neighbors)
    # print(faces)

    # drwa faces recieved from drone
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

    return img
