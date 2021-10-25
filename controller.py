from pyezviz import EzvizClient, EzvizCamera

from constants import *


class Camera:

    def __init__(self, serial, client, data):
        self.camera = EzvizCamera(client, serial, data)

    def move_left(self):
        return self.camera.move("left")

    def move_right(self):
        return self.camera.move("right")

    def move_up(self):
        return self.camera.move("up")

    def move_down(self):
        return self.camera.move("down")


class CameraController:

    def __init__(self, username, password, logger):
        self.logger = logger
        self.client = EzvizClient(username, password)
        self.cameras = {}
        self._selected = Cameras.TURBINE
        self.setup_cameras()

    def setup_cameras(self):
        cameras = self.client.load_cameras()
        for cam, serial in CAMERA_NAMES:
            self.cameras[cam] = Camera(
                CAMERA_NAMES[cam], self.client,
                cameras[CAMERA_NAMES[serial]]
            )

    def select(self, choice):
        self._selected = choice
        self.logger.info("Chose {}".format(choice))

    def move_up(self):
        self.cameras[self._selected].move_up()
        self.logger.info("Moving Up, Cam: {}".format(self._selected))

    def move_down(self):
        self.cameras[self._selected].move_down()
        self.logger.info("Moving Down, Cam: {}".format(self._selected))

    def move_right(self):
        self.cameras[self._selected].move_right()
        self.logger.info("Moving Right, Cam: {}".format(self._selected))

    def move_left(self):
        self.cameras[self._selected].move_left()
        self.logger.info("Moving Left, Cam: {}".format(self._selected))
