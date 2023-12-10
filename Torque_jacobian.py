from numpy import *


def calculate_torque(theta_1, theta_2, theta_3, phi):
    L1 = 10
    L2 = 8
    L3 = 6
    J11 = -L1 * sin(theta_1) - L2 * sin(theta_1 + theta_2) - L3 * sin(theta_1 + theta_2 + theta_3)
    J12 = -L2 * sin(theta_1 + theta_2) - L3 * sin(theta_1 + theta_2 + theta_3)
    J13 = -L3 * sin(theta_1 + theta_2 + theta_3)

    J21 = L1 * cos(theta_1) + L2 * cos(theta_1 + theta_2) + L3 * cos(theta_1 + theta_2 + theta_3)
    J22 = L2 * cos(theta_1 + theta_2) + L3 * cos(theta_1 + theta_2 + theta_3)
    J23 = L3 * cos(theta_1 + theta_2 + theta_3)

    J = array([[J11, J12, J13],
               [J21, J22, J23]])

    # Force vector (as a column vector)
    F = array([[1.0], [1.0]])

    # Transpose of the Jacobian matrix
    J_T = J.T

    # Torque calculation
    torque = dot(J_T, F)

    return torque


deg = deg2rad(30)
print(calculate_torque(-deg, -deg, -deg, 90))
