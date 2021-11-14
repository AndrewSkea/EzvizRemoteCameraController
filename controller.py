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

    def __init__(self, username, password, logger, is_test):
        self.is_test = is_test
        self.logger = logger
        if is_test:
            self.client = None
        else:
            self.client = EzvizClient(username, password)
        self.cameras = {}
        self._selected = Cameras.TURBINE
        if not is_test:
            self.setup_cameras()

    def setup_cameras(self):
        cameras = self.client.load_cameras()
        self.logger.info(cameras)
        for cam, serial in CAMERA_NAMES.items():
            self.cameras[cam] = Camera(
                CAMERA_NAMES[cam], self.client,
                cameras[serial]
            )

    def select(self, choice):
        self._selected = choice
        self.logger.info("Chose {}".format(choice))

    def move_up(self):
        if not self.is_test:
            self.cameras[self._selected].move_up()
        self.logger.info("Moving Up, Cam: {}".format(self._selected))

    def move_down(self):
        if not self.is_test:
            self.cameras[self._selected].move_down()
        self.logger.info("Moving Down, Cam: {}".format(self._selected))

    def move_right(self):
        if not self.is_test:
            self.cameras[self._selected].move_right()
        self.logger.info("Moving Right, Cam: {}".format(self._selected))

    def move_left(self):
        if not self.is_test:
            self.cameras[self._selected].move_left()
        self.logger.info("Moving Left, Cam: {}".format(self._selected))
