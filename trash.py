from numpy import *

l1 = 10.0
l2 = 8.0
l3 = 6.0

I1 = 1
I2 = 1
I3 = 1

m1 = 1.0
m2 = 1.0
m3 = 1.0

theta1 = 30.0
theta1 = deg2rad(theta1)
theta2 = 30.0
theta2 = deg2rad(theta2)
theta3 = 30.0
theta3 = deg2rad(theta3)

g = 9.81

g1 = m3 * g * ((l1 * cos(theta1)) + 0.5 * l3 * cos(theta1 + theta2 + theta3) + l2 * cos(theta1 + theta2)) + m2 * g * (
        l1 * cos(theta1) + 0.5 * l2 * cos(theta1 + theta2)) + 0.5 * m1 * g * l1 * cos(theta1)

g2 = m3 * g * (0.5 * l3 * cos(theta1 + theta2 + theta3) + l2 * cos(theta1 + theta2)) + 0.5 * m2 * g * l2 * cos(
    theta1 + theta2)

g3 = 0.5 * m3 * g * l3 * cos(theta1 + theta2 + theta3)

M11 = l1 ** 2 * (0.25 * m1 + m2 + m3) + l2 ** 2 * (0.25 * m2 + m3) + 0.25 * l3 ** 2 * m3 + l1 * l2 * cos(theta2) * (
            m2 + 2 * m3) + l2 * l3 * m3 * cos(theta3) + 0.5 * l1 * l3 * m3 * cos(theta2 + theta3) + I1 + I2 + I3
M12 = l2 ** 2 * (0.25 * m2 + m3) + 0.25 * l3 ** 2 * m3 + l1 * l2 * cos(theta2) * (m3 + 0.5 * m2) + l2 * l3 * m3 * cos(
    theta3) + 0.5 * l1 * l3 * m3 * cos(theta2 + theta3) + I2 + I3
M13 = 0.25 * l3 ** 2 * m3 + 0.5 * l2 * l3 * m3 * cos(theta3) + 0.5 * l1 * l3 * m3 * cos(theta2 + theta3) + I3

M21 = l2 ** 2 * (0.25 * m2 + m3) + 0.25 * l3 ** 2 * m3 + l1 * l2 * cos(theta2) * (m3 + 0.5 * m2) + l2 * l3 * m3 * cos(
    theta3) + 0.5 * l1 * l3 * m3 * cos(theta2 + theta3) + I2 + I3
M22 = l2 ** 2 * (0.25 * m2 + m3) + 0.25 * l3 ** 2 * m3 + l2 * l3 * m3 * cos(theta3) + I2 + I3
M23 = 0.25 * l3 ** 2 * m3 + 0.5 * l2 * l3 * m3 * cos(theta3) + I3

M31 = 0.25 * l3 ** 2 * m3 + 0.5 * l2 * l3 * m3 * cos(theta3) + 0.5 * l1 * l3 * m3 * cos(theta2 + theta3) + I3
M32 = 0.25 * l3 ** 2 * m3 + 0.5 * l2 * l3 * m3 * cos(theta3) + I3
M33 = 0.25 * l3 ** 2 * m3 + I3

print(M11, M12, M13)
