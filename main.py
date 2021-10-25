#!/usr/bin/python3
import logging
import os
import sys

import RPi.GPIO as GPIO
from dotenv import load_dotenv

from constants import *
from controller import CameraController


# Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger(__name__)

output_file_handler = logging.FileHandler("output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(output_file_handler)
logger.addHandler(stdout_handler)

logger = logging.getLogger(__name__)

# OS Environment variables
load_dotenv()
APP_USERNAME = os.environ.get("EZVIZ_USERNAME")
APP_PASSWORD = os.environ.get("EZVIZ_PASSWORD")

controller = CameraController(APP_USERNAME, APP_PASSWORD, logger)

def choose_turbine_cam(channel):
    controller.select(Cameras.TURBINE)

def choose_building_cam(channel):
    controller.select(Cameras.BUILDING)

def choose_inside1_cam(channel):
    controller.select(Cameras.INSIDE1)

def choose_inside2_cam(channel):
    controller.select(Cameras.INSIDE2)


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(cam_1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(cam_2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(cam_3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(cam_4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(move_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(move_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(move_down_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(move_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(cam_1_pin, GPIO.RISING, callback=choose_turbine_cam, bouncetime=bouncetime)
GPIO.add_event_detect(cam_2_pin, GPIO.RISING, callback=choose_building_cam, bouncetime=bouncetime)
GPIO.add_event_detect(cam_3_pin, GPIO.RISING, callback=choose_inside1_cam, bouncetime=bouncetime)
GPIO.add_event_detect(cam_4_pin, GPIO.RISING, callback=choose_inside2_cam, bouncetime=bouncetime)
GPIO.add_event_detect(move_up_pin, GPIO.RISING, callback=controller.move_up, bouncetime=bouncetime)
GPIO.add_event_detect(move_left_pin, GPIO.RISING, callback=controller.move_left, bouncetime=bouncetime)
GPIO.add_event_detect(move_down_pin, GPIO.RISING, callback=controller.move_down, bouncetime=bouncetime)
GPIO.add_event_detect(move_right_pin, GPIO.RISING, callback=controller.move_right, bouncetime=bouncetime)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup()
