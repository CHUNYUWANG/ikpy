import unittest
import numpy as np
import poppy_inverse_kinematics.robot_utils
import poppy_inverse_kinematics.model
import poppy_inverse_kinematics.model_config
import scripts_config


class TestModel(unittest.TestCase):
    def setUp(self):

        params = poppy_inverse_kinematics.model_config.from_urdf_file(scripts_config.urdf_file, scripts_config.base_link, scripts_config.last_link_vector)
        self.robot = poppy_inverse_kinematics.model.Model(params, computation_method="hybrid", simplify=False)

        target = [-0.1, 0.1, 0.1]

        self.robot.target = target

    def test_ik(self):
        self.robot.goto_target()
        np.testing.assert_almost_equal(self.robot.forward_kinematic(), self.robot.target, decimal=3)


if __name__ == '__main__':
    unittest.main()
