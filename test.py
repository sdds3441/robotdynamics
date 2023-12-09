from numpy import *
from matplotlib import pyplot as plt

# Length of links in cm
a1 = 10
a2 = 8
a3 = 6

# Desired Position of End effector
px = 15
py = -0

phi = 30
phi = deg2rad(phi)

# Equations for Inverse kinematics
wx = px - a3 * cos(phi)
wy = py - a3 * sin(phi)

delta = wx ** 2 + wy ** 2
c2 = (delta - a1 ** 2 - a2 ** 2) / (2 * a1 * a2)
s2 = sqrt(1 - c2 ** 2)  # elbow down
theta_2 = arctan2(s2, c2)

s1 = ((a1 + a2 * c2) * wy - a2 * s2 * wx) / delta
c1 = ((a1 + a2 * c2) * wx + a2 * s2 * wy) / delta
theta_1 = arctan2(s1, c1)
theta_3 = phi - theta_1 - theta_2
theta_1 = -theta_1
theta_2 = -theta_2
theta_3 = -theta_3

x1 = a1 * cos(theta_1)
y1 = a1 * sin(theta_1)
x2 = a1 * cos(theta_1) + a2 * (cos(theta_1 + theta_2))
y2 = a1 * sin(theta_1) + a2 * (sin(theta_1 + theta_2))
x3 = a1 * cos(theta_1) + a2 * (cos(theta_1 + theta_2)) + a3 * cos(theta_1 + theta_2 + theta_3)
y3 = a1 * sin(theta_1) + a2 * (sin(theta_1 + theta_2)) + a3 * sin(theta_1 + theta_2 + theta_3)
plt.plot([0, x1, x2, x3], [0, y1, y2, y3])
plt.xlim(0, 30)
plt.ylim(0, 30)
plt.show()
