#!/usr/bin/python3
import logging
import os
import sys
import time

import RPi.GPIO as GPIO
from dotenv import load_dotenv

from constants import *
from controller import CameraController
import argparse
parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
parser.add_argument('-w', action='store_true')

args = parser.parse_args()

is_test = args.w

# Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger(__name__)

output_file_handler = logging.FileHandler("/home/pi/logs/output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(output_file_handler)
logger.addHandler(stdout_handler)

# OS Environment variables
load_dotenv()
APP_USERNAME = os.environ.get("EZVIZ_USERNAME")
APP_PASSWORD = os.environ.get("EZVIZ_PASSWORD")

controller = CameraController(APP_USERNAME, APP_PASSWORD, logger, is_test)
is_moving = False

def choose_turbine_cam(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.select(Cameras.TURBINE)
        time.sleep(1)
    is_moving = False

def choose_building_cam(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.select(Cameras.BUILDING)
        time.sleep(1)
    is_moving = False

def choose_inside1_cam(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.select(Cameras.INSIDE1)
        time.sleep(1)
    is_moving = False

def choose_inside2_cam(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.select(Cameras.INSIDE2)
        time.sleep(1)
    is_moving = False

def move_up(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.move_up()
        time.sleep(1)
    is_moving = False

def move_left(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.move_left()
        time.sleep(1)
    is_moving = False

def move_down(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.move_down()
        time.sleep(1)
    is_moving = False

def move_right(channel):
    global is_moving
    if not is_moving:
        is_moving = True
        controller.move_right()
        time.sleep(1)
    is_moving = False


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
GPIO.add_event_detect(move_up_pin, GPIO.RISING, callback=move_up, bouncetime=bouncetime)
GPIO.add_event_detect(move_left_pin, GPIO.RISING, callback=move_left, bouncetime=bouncetime)
GPIO.add_event_detect(move_down_pin, GPIO.RISING, callback=move_down, bouncetime=bouncetime)
GPIO.add_event_detect(move_right_pin, GPIO.RISING, callback=move_right, bouncetime=bouncetime)

print("Waiting foreverrrr.....")
while True:
    time.sleep(1)
GPIO.cleanup()
