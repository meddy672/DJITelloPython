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


def telloGetFrame(drone: Tello, w=360, h=240):
    """Specify frame of the image."""
    frame = drone.get_frame_read()
    img_frame = frame.frame
    return cv2.resize(img_frame, (w,h))
