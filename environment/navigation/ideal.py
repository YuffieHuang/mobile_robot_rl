import numpy as np

from environment.navigation.base import Base


class Ideal(Base):
    def __init__(self, target_position, wheel_diameter, robot_width, dt):
        super(Ideal, self).__init__(target_position, wheel_diameter,
                                    robot_width, dt)

    def compute_position(self, **kwargs):
        position = np.round(kwargs['position'], 3)
        position[2] = self._angle_correction(position[2])
        self._navigation_error[0] = np.sqrt(
            np.sum((self._target_position - position[0:2])**2))

        theta = np.arctan2(self._target_position[1] - position[1],
                           self._target_position[0] - position[0])

        theta = self._angle_correction(theta)

        self._navigation_error[1] = self._angle_correction(theta - position[2])