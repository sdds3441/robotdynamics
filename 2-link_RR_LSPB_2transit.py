import math

import matplotlib.pyplot as plt
import numpy as np


def theta1(init, theta_2d, i, t=4):
    theta1 = init + (theta_2d * (i ** 2)) / 2
    theta1_d = theta_2d * i
    theta1_2d = theta_2d
    return theta1, theta1_d, theta1_2d


def theta2(init, theta_2d, i, t, v):
    theta2 = init + (theta_2d * t * (i - (t / 2)))
    if v == 1:
        theta2_d = v1
    else:
        theta2_d = v2
    theta2_2d = 0
    return theta2, theta2_d, theta2_2d


def theta3(transit, theta_2d, i, t=4.0):
    theta3 = transit - (0.5 * theta_2d * ((t - i) ** 2))
    theta3_d = -(i - (t)) * theta_2d
    theta3_2d = -theta_2d
    return theta3, theta3_d, theta3_2d


init = 30
transit = 45
final = 60
transit2 = 30

t = 4
t2 = 2
v1 = ((2 * (transit - init)) / (t2)) * 0.85
tb1 = (init - transit + (v1 * (t2))) / v1

v2 = ((2 * (final - transit2)) / t) * 0.85
tb2 = (transit2 - final + (v2 * t)) / v2

theta1_2d = (v1 ** 2) / (init - transit + (v1 * (t2)))
theta2_2d = (v2 ** 2) / (transit2 - final + (v2 * t))

const = (4 * (transit - init)) / ((t / 2) ** 2)

theta_list = []
theta_list2 = []
theta_d_list = []
theta_d_list2 = []
theta_2d_list = []
theta_2d_list2 = []

for i in np.arange(0, t, 0.001):
    if i < tb1:
        theta, theta_d, theta_2d = theta1(init, theta1_2d, i, t=tb1)
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(theta_2d)

    if tb1 <= i < t2 - tb1:
        theta, theta_d, theta_2d = theta2(init, theta1_2d, i, tb1, 1)
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(theta_2d)

    if t2 - tb1 < i <= t2:

        theta, theta_d, theta_2d = theta3(transit, theta1_2d, i, t=t2)
        a_theta, a_theta_d, a_theta_2d = theta3(transit, theta1_2d, i, t=t2)
        b_theta, b_theta_d, b_theta_2d = theta1(transit2, theta2_2d, i)
        c_theta, c_theta_d, c_theta_2d = theta2(transit2, theta2_2d, i, tb2, 2)
        if tb2 > i:
            if b_theta_d < a_theta_d:
                theta, theta_d, theta_2d = a_theta, a_theta_d, a_theta_2d
            else:
                theta, theta_d, theta_2d = a_theta, b_theta_d, b_theta_2d
        elif i > tb2:
            theta, theta_d, theta_2d = a_theta, c_theta_d, c_theta_2d
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(theta_2d)

    if t2 < i <= t - tb2:
        theta, theta_d, theta_2d = theta2(transit2, theta2_2d, i, tb2, 2)
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(theta_2d)

    if t - tb2 < i <= t:
        theta, theta_d, theta_2d = theta3(final, theta2_2d, i, t)
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(theta_2d)

Time = int(float(input("Input Time:")) * 1000)
Torque = str(round(theta_2d_list[Time] ** 2, 3)) + "ml^2+" + str(round(math.sin(theta_list[Time]), 3)) + "mgl"
ax1 = plt.subplot(3, 1, 1)
plt.plot(theta_list)
plt.title("Position")
plt.text(3, 50, 'Torque=' + str(round(theta_2d_list[Time] ** 2, 3)) + r"m$l^2$+" + str(
    round(math.sin(theta_list[Time]), 3)) + "mgl")
plt.xticks(visible=False)

plt.subplot(3, 1, 2, sharex=ax1)
plt.plot(theta_d_list)
plt.title("Velocity")
plt.xticks(visible=False)

plt.subplot(3, 1, 3, sharex=ax1)
plt.plot(theta_2d_list)
plt.title("Acceleration")
plt.xlabel("Time(seconds)")
plt.xticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000], [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
plt.show()
