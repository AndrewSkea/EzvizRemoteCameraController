from enum import Enum


# Global Env Variables
bouncetime = 750
cam_1_pin = 7
cam_2_pin = 8
cam_3_pin = 10
cam_4_pin = 11
move_up_pin = 11
move_left_pin = 12
move_down_pin = 13
move_right_pin = 15

class Cameras(Enum):
    BUILDING=0
    TURBINE=1
    INSIDE1=2
    INSIDE2=3

CAMERA_NAMES = {
    Cameras.TURBINE: "F75629697",
    Cameras.BUILDING: "F83286712",
    Cameras.INSIDE1: "F83286711",
    Cameras.INSIDE2: "F75629415"
}