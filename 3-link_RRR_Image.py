from numpy import *
from matplotlib import pyplot as plt, animation
import math


def update(frame, Route, link_l1, link_l2, link_l3):
    start_x = 15
    start_y = -10

    Route.set_data([start_x, x_l3_end[frame]], [start_y, y_l3_end[frame]])

    link_l1_x = [0, x_l1_end[frame]]
    link_l1_y = [0, y_l1_end[frame]]
    link_l1.set_data(link_l1_x, link_l1_y)
    link_l2_x = [x_l1_end[frame], x_l2_end[frame]]
    link_l2_y = [y_l1_end[frame], y_l2_end[frame]]
    link_l2.set_data(link_l2_x, link_l2_y)

    link_l3_x = [x_l2_end[frame], x_l3_end[frame]]
    link_l3_y = [y_l2_end[frame], y_l3_end[frame]]
    link_l3.set_data(link_l3_x, link_l3_y)

    return Route, link_l1, link_l2, link_l3


def make_trajectory(start_x, start_y, end_x, end_y):
    x_l1_end_local = []
    y_l1_end_local = []
    x_l2_end_local = []
    y_l2_end_local = []
    x_l3_end_local = []
    y_l3_end_local = []
    x_trajectory = linspace(start_x, end_x, Route_point)
    y_trajectory = linspace(start_y, end_y, Route_point)

    for i in range(Route_point):
        wx = x_trajectory[i] - l3 * cos(phi)
        wy = y_trajectory[i] - l3 * sin(phi)
        delta = wx ** 2 + wy ** 2
        c2 = (delta - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
        s2 = sqrt(1 - c2 ** 2)
        theta_2 = arctan2(s2, c2)
        s1 = ((l1 + l2 * c2) * wy - l2 * s2 * wx) / delta
        c1 = ((l1 + l2 * c2) * wx + l2 * s2 * wy) / delta
        theta_1 = arctan2(s1, c1)
        theta_3 = phi - theta_1 - theta_2
        theta_1 = -theta_1
        theta_2 = -theta_2
        theta_3 = -theta_3

        x_l1_end_local.append(l1 * cos(theta_1))
        y_l1_end_local.append(l1 * sin(theta_1))
        x_l2_end_local.append(l1 * cos(theta_1) + l2 * (cos(theta_1 + theta_2)))
        y_l2_end_local.append(l1 * sin(theta_1) + l2 * (sin(theta_1 + theta_2)))
        x_l3_end_local.append(l1 * cos(theta_1) + l2 * (cos(theta_1 + theta_2)) + l3 * cos(theta_1 + theta_2 + theta_3))
        y_l3_end_local.append(l1 * sin(theta_1) + l2 * (sin(theta_1 + theta_2)) + l3 * sin(theta_1 + theta_2 + theta_3))

    return x_l1_end_local, x_l2_end_local, x_l3_end_local, y_l1_end_local, y_l2_end_local, y_l3_end_local


x_l1_end = []
y_l1_end = []
x_l2_end = []
y_l2_end = []
x_l3_end = []
y_l3_end = []
theta1_list = []
theta2_list = []
theta3_list = []

first_x = 15
first_y = -10

final_x = 15
final_y = 0

# Length of links in cm
l1 = 10
l2 = 8
l3 = 6

Route_point = 100
# Desired Position of End effector


phi = 30
phi = deg2rad(phi)

x_l1_end, x_l2_end,x_l3_end,y_l1_end,y_l2_end,y_l3_end=make_trajectory(first_x, first_y, final_x, final_y)
figure, ax = plt.subplots()

plt.xlim(0, 30)
plt.ylim(0, 30)
Route, = ax.plot([], [], 'k')
link_l1, = ax.plot([], 'b', lw=2)
link_l2, = ax.plot([], 'r', lw=2)
link_l3, = ax.plot([], 'g', lw=2)
ani = animation.FuncAnimation(figure, update,
                              fargs=(Route, link_l1, link_l2, link_l3))
plt.show()
print('asdf')
