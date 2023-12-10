from numpy import *
from matplotlib import pyplot as plt, animation
import math


def update(frame, Route, link_l1_loc, link_l2_loc, link_l3_loc):
    start_x = 15
    start_y = -10

    Route.set_data([start_x, x_l3_end[frame]], [start_y, y_l3_end[frame]])

    link_l1_x = [0, x_l1_end[frame]]
    link_l1_y = [0, y_l1_end[frame]]
    link_l1_loc.set_data(link_l1_x, link_l1_y)

    link_l2_x = [x_l1_end[frame], x_l2_end[frame]]
    link_l2_y = [y_l1_end[frame], y_l2_end[frame]]
    link_l2_loc.set_data(link_l2_x, link_l2_y)

    link_l3_x = [x_l2_end[frame], x_l3_end[frame]]
    link_l3_y = [y_l2_end[frame], y_l3_end[frame]]
    link_l3_loc.set_data(link_l3_x, link_l3_y)

    return Route, link_l1_loc, link_l2_loc, link_l3_loc


def make_trajectory(start_x, start_y, end_x, end_y):
    x_l1_end_local = []
    y_l1_end_local = []
    x_l2_end_local = []
    y_l2_end_local = []
    x_l3_end_local = []
    y_l3_end_local = []

    loc_theta1_list = []
    loc_theta2_list = []
    loc_theta3_list = []

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

        loc_theta1_list.append(theta_1)
        loc_theta2_list.append(theta_2)
        loc_theta3_list.append(theta_3)

        x_l1_end_local.append(l1 * cos(theta_1))
        y_l1_end_local.append(l1 * sin(theta_1))
        x_l2_end_local.append(l1 * cos(theta_1) + l2 * (cos(theta_1 + theta_2)))
        y_l2_end_local.append(l1 * sin(theta_1) + l2 * (sin(theta_1 + theta_2)))
        x_l3_end_local.append(l1 * cos(theta_1) + l2 * (cos(theta_1 + theta_2)) + l3 * cos(theta_1 + theta_2 + theta_3))
        y_l3_end_local.append(l1 * sin(theta_1) + l2 * (sin(theta_1 + theta_2)) + l3 * sin(theta_1 + theta_2 + theta_3))

    return x_l1_end_local, x_l2_end_local, x_l3_end_local, y_l1_end_local, y_l2_end_local, y_l3_end_local, \
           loc_theta1_list, loc_theta2_list, loc_theta3_list


def torque_jacobian(theta_1, theta_2, theta_3):
    loc_l1 = 10
    loc_l2 = 8
    loc_l3 = 6
    J11 = -loc_l1 * sin(theta_1) - loc_l2 * sin(theta_1 + theta_2) - loc_l3 * sin(theta_1 + theta_2 + theta_3)
    J12 = -loc_l2 * sin(theta_1 + theta_2) - loc_l3 * sin(theta_1 + theta_2 + theta_3)
    J13 = -l3 * sin(theta_1 + theta_2 + theta_3)

    J21 = loc_l1 * cos(theta_1) + loc_l2 * cos(theta_1 + theta_2) + loc_l3 * cos(theta_1 + theta_2 + theta_3)
    J22 = loc_l2 * cos(theta_1 + theta_2) + loc_l3 * cos(theta_1 + theta_2 + theta_3)
    J23 = loc_l3 * cos(theta_1 + theta_2 + theta_3)

    J = array([[J11, J12, J13],
               [J21, J22, J23]])

    F = array([[1.0], [1.0]])

    J_T = J.T

    torque = dot(J_T, F)
    loc_theta1_torque = torque[0]
    loc_theta2_torque = torque[1]
    loc_theta3_torque = torque[2]

    return torque


x_l1_end = []
y_l1_end = []
x_l2_end = []
y_l2_end = []
x_l3_end = []
y_l3_end = []

theta1_list = []
theta2_list = []
theta3_list = []
theta1_torque_list = []
theta2_torque_list = []
theta3_torque_list = []

first_x = 15
first_y = -10

final_x = 12
final_y = 0

l1 = 10
l2 = 8
l3 = 6

Route_point = 100

phi = 30
phi = deg2rad(phi)

x_l1_end, x_l2_end, x_l3_end, y_l1_end, y_l2_end, y_l3_end, theta1_list, theta2_list, theta3_list = make_trajectory(
    first_x, first_y,
    final_x, final_y)

for i in range(len(theta1_list)):
    Torque = torque_jacobian(theta1_list[i], theta2_list[i], theta3_list[i])
    theta1_torque_list.append(Torque[0])
    theta2_torque_list.append(Torque[1])
    theta3_torque_list.append(Torque[2])

figure, ax = plt.subplots()

plt.xlim(0, 30)
plt.ylim(0, 30)
plt.scatter(12, 0, s=50, c='#0000FF', zorder=1)
plt.plot([12, 18], [0, 0], color="red", linewidth=3, zorder=0)
Route, = ax.plot([], [], 'k',lw=0)
link_l1, = ax.plot([], 'b', lw=2)
link_l2, = ax.plot([], 'r', lw=2)
link_l3, = ax.plot([], 'g', lw=2)
ani = animation.FuncAnimation(figure, update,
                              fargs=( Route, link_l1, link_l2, link_l3))
plt.show()
print('asdf')
plt.show()
