# -*- coding: utf-8 -*-

import time
from sdls.engine.calibration.calibration import Calibration


class MovingCalibration(Calibration):

    """Moving calibration:

            - Move motor sequence
            - Call _capture at each position
            - Call _calibrate at the end
    """

    def __init__(self):
        Calibration.__init__(self)
        self.step = 3

    def _initialize(self):
        raise NotImplementedError

    def _capture(self, angle):
        raise NotImplementedError

    def _calibrate(self):
        raise NotImplementedError

    def _start(self):
        if self.driver.is_connected:
            angle = 0.0

            self._initialize()

            # Setup scanner
            self.driver.board.lasers_off()
            self.driver.board.motor_enable()
            self.driver.board.motor_reset_origin()
            self.driver.board.motor_speed(200)
            self.driver.board.motor_acceleration(200)

            # Move to starting position
            self.driver.board.motor_move(-90)

            if self._progress_callback is not None:
                self._progress_callback(0)

            while self._is_calibrating and abs(angle) < 180:

                if self._progress_callback is not None:
                    self._progress_callback(100 * abs(angle) / 180.)

                self._capture(angle)

                angle += self.step
                self.driver.board.motor_move(self.step)
                time.sleep(0.5)

            # Move to origin
            self.driver.board.motor_move(90 - angle)

            self.driver.board.lasers_off()
            self.driver.board.motor_disable()

            # Compute calibration
            response = self._calibrate()

            if self._after_callback is not None:
                self._after_callback(response)
