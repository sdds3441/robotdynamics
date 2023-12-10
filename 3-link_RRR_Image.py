from numpy import *
from matplotlib import pyplot as plt, animation
import cv2


def update(frame, Route, link_l1_loc, link_l2_loc, link_l3_loc):
    start_x = 15
    start_y = -10

    if frame < 100:
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
    elif 100 <= frame < 200:
        link_l1_x2 = [0, x_l1_end[99 - frame]]
        link_l1_y2 = [0, y_l1_end[99 - frame]]
        link_l1_loc.set_data(link_l1_x2, link_l1_y2)

        link_l2_x2 = [x_l1_end[99 - frame], x_l2_end[99 - frame]]
        link_l2_y2 = [y_l1_end[99 - frame], y_l2_end[99 - frame]]
        link_l2_loc.set_data(link_l2_x2, link_l2_y2)

        link_l3_x2 = [x_l2_end[99 - frame], x_l3_end[99 - frame]]
        link_l3_y2 = [y_l2_end[99 - frame], y_l3_end[99 - frame]]
        link_l3_loc.set_data(link_l3_x2, link_l3_y2)
    # 여기까지가 1번쨰
    elif 200 <= frame < 300:
        img = cv2.imread('dataset/img_90.png')
        cv2.imshow('tri', img)
        if frame == 200:
            plt.scatter(12, 0, s=20, c='#FF0000', zorder=1)
            plt.scatter(15, 0, s=20, c='#0000FF', zorder=1)
        link_l1_x = [0, x_l1_end2[frame - 200]]
        link_l1_y = [0, y_l1_end2[frame - 200]]
        link_l1_loc.set_data(link_l1_x, link_l1_y)

        link_l2_x = [x_l1_end2[frame - 200], x_l2_end2[frame - 200]]
        link_l2_y = [y_l1_end2[frame - 200], y_l2_end2[frame - 200]]
        link_l2_loc.set_data(link_l2_x, link_l2_y)

        link_l3_x = [x_l2_end2[frame - 200], x_l3_end2[frame - 200]]
        link_l3_y = [y_l2_end2[frame - 200], y_l3_end2[frame - 200]]
        link_l3_loc.set_data(link_l3_x, link_l3_y)

    elif 300 <= frame < 400:
        link_l1_x2 = [0, x_l1_end2[299 - frame]]
        link_l1_y2 = [0, y_l1_end2[299 - frame]]
        link_l1_loc.set_data(link_l1_x2, link_l1_y2)

        link_l2_x2 = [x_l1_end2[299 - frame], x_l2_end2[299 - frame]]
        link_l2_y2 = [y_l1_end2[299 - frame], y_l2_end2[299 - frame]]
        link_l2_loc.set_data(link_l2_x2, link_l2_y2)

        link_l3_x2 = [x_l2_end2[299 - frame], x_l3_end2[299 - frame]]
        link_l3_y2 = [y_l2_end2[299 - frame], y_l3_end2[299 - frame]]
        link_l3_loc.set_data(link_l3_x2, link_l3_y2)
    # 여기까지가 2번쨰
    elif 400 <= frame < 500:
        img = cv2.imread('dataset/img_135.png')
        cv2.imshow('tri', img)
        if frame == 400:
            plt.plot([10, 18], [0, 0], color="white", linewidth=5, zorder=2)
            plt.plot([14, 19], [0, 0], color="red", linewidth=5, zorder=3)
            plt.scatter(19, 0, s=20, c='#0000FF', zorder=4)
        link_l1_x = [0, x_l1_end3[frame - 400]]
        link_l1_y = [0, y_l1_end3[frame - 400]]
        link_l1_loc.set_data(link_l1_x, link_l1_y)

        link_l2_x = [x_l1_end3[frame - 400], x_l2_end3[frame - 400]]
        link_l2_y = [y_l1_end3[frame - 400], y_l2_end3[frame - 400]]
        link_l2_loc.set_data(link_l2_x, link_l2_y)

        link_l3_x = [x_l2_end3[frame - 400], x_l3_end3[frame - 400]]
        link_l3_y = [y_l2_end3[frame - 400], y_l3_end3[frame - 400]]
        link_l3_loc.set_data(link_l3_x, link_l3_y)

    elif 500 <= frame < 600:
        link_l1_x2 = [0, x_l1_end3[499 - frame]]
        link_l1_y2 = [0, y_l1_end3[499 - frame]]
        link_l1_loc.set_data(link_l1_x2, link_l1_y2)

        link_l2_x2 = [x_l1_end3[499 - frame], x_l2_end3[499 - frame]]
        link_l2_y2 = [y_l1_end3[499 - frame], y_l2_end3[499 - frame]]
        link_l2_loc.set_data(link_l2_x2, link_l2_y2)

        link_l3_x2 = [x_l2_end3[499 - frame], x_l3_end3[499 - frame]]
        link_l3_y2 = [y_l2_end3[499 - frame], y_l3_end3[499 - frame]]
        link_l3_loc.set_data(link_l3_x2, link_l3_y2)
    # 여기까지가 3번째

    elif 600 <= frame < 700:
        img = cv2.imread('dataset/img_180.png')
        cv2.imshow('tri', img)
        if frame == 600:
            plt.plot([10, 20], [0, 0], color="white", linewidth=5, zorder=4)
            plt.plot([12, 18], [0, 0], color="red", linewidth=5, zorder=5)
            plt.scatter(18, 0, s=20, c='#0000FF', zorder=6)
        link_l1_x = [0, x_l1_end4[frame - 600]]
        link_l1_y = [0, y_l1_end4[frame - 600]]
        link_l1_loc.set_data(link_l1_x, link_l1_y)

        link_l2_x = [x_l1_end4[frame - 600], x_l2_end4[frame - 600]]
        link_l2_y = [y_l1_end4[frame - 600], y_l2_end4[frame - 600]]
        link_l2_loc.set_data(link_l2_x, link_l2_y)

        link_l3_x = [x_l2_end4[frame - 600], x_l3_end4[frame - 600]]
        link_l3_y = [y_l2_end4[frame - 600], y_l3_end4[frame - 600]]
        link_l3_loc.set_data(link_l3_x, link_l3_y)

    elif 700 <= frame < 800:
        link_l1_x2 = [0, x_l1_end4[699 - frame]]
        link_l1_y2 = [0, y_l1_end4[699 - frame]]
        link_l1_loc.set_data(link_l1_x2, link_l1_y2)

        link_l2_x2 = [x_l1_end4[699 - frame], x_l2_end4[699 - frame]]
        link_l2_y2 = [y_l1_end4[699 - frame], y_l2_end4[699 - frame]]
        link_l2_loc.set_data(link_l2_x2, link_l2_y2)

        link_l3_x2 = [x_l2_end4[699 - frame], x_l3_end4[699 - frame]]
        link_l3_y2 = [y_l2_end4[699 - frame], y_l3_end4[699 - frame]]
        link_l3_loc.set_data(link_l3_x2, link_l3_y2)

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

    x_trajectory = linspace(start_x, end_x, 100)
    y_trajectory = linspace(start_y, end_y, 100)

    for i in range(100):
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

    return torque

img=cv2.imread('dataset/triangle.png',cv2.IMREAD_COLOR)
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
print(cX,cY)


M1 = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
M2 = cv2.getRotationMatrix2D((138, 108), 135, 1.0)
M3 = cv2.getRotationMatrix2D((cX, cY), 180, 1.0)
rotated_90 = cv2.warpAffine(img, M1, (w, h))
rotated_135 = cv2.warpAffine(img, M2, (w, h))
rotated_180 = cv2.warpAffine(img, M3, (w, h))
cv2.imshow('img',img)
cv2.imshow('img_90',rotated_90)
cv2.imshow('img_135',rotated_135)
cv2.imshow('img_180',rotated_180)
cv2.waitKey()
cv2.imwrite('dataset/img_90.png', rotated_90)
cv2.imwrite('dataset/img_135.png', rotated_135)
cv2.imwrite('dataset/img_180.png', rotated_180)

cv2.destroyAllWindows()

x_l1_end = []
y_l1_end = []
x_l2_end = []
y_l2_end = []
x_l3_end = []
y_l3_end = []

x_l1_end2 = []
y_l1_end2 = []
x_l2_end2 = []
y_l2_end2 = []
x_l3_end2 = []
y_l3_end2 = []

x_l1_end3 = []
y_l1_end3 = []
x_l2_end3 = []
y_l2_end3 = []
x_l3_end3 = []
y_l3_end3 = []

x_l1_end4 = []
y_l1_end4 = []
x_l2_end4 = []
y_l2_end4 = []
x_l3_end4 = []
y_l3_end4 = []

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

final_x2 = 15
final_x3 = 19
final_x4 = 18

l1 = 10
l2 = 8
l3 = 6

phi = 30
phi = deg2rad(phi)

x_l1_end, x_l2_end, x_l3_end, y_l1_end, y_l2_end, y_l3_end, theta1_list, theta2_list, theta3_list = make_trajectory(
    first_x, first_y,
    final_x, final_y)

x_l1_end2, x_l2_end2, x_l3_end2, y_l1_end2, y_l2_end2, y_l3_end2, theta1_list, theta2_list, theta3_list = make_trajectory(
    first_x, first_y,
    final_x2, final_y)

x_l1_end3, x_l2_end3, x_l3_end3, y_l1_end3, y_l2_end3, y_l3_end3, theta1_list, theta2_list, theta3_list = make_trajectory(
    first_x, first_y,
    final_x3, final_y)

x_l1_end4, x_l2_end4, x_l3_end4, y_l1_end4, y_l2_end4, y_l3_end4, theta1_list, theta2_list, theta3_list = make_trajectory(
    first_x, first_y,
    final_x4, final_y)

for i in range(len(theta1_list)):
    Torque = torque_jacobian(theta1_list[i], theta2_list[i], theta3_list[i])
    theta1_torque_list.append(Torque[0])
    theta2_torque_list.append(Torque[1])
    theta3_torque_list.append(Torque[2])

figure, ax = plt.subplots()

plt.xlim(0, 30)
plt.ylim(0, 30)
plt.scatter(12, 0, s=20, c='#0000FF', zorder=1)
plt.plot([12, 18], [0, 0], color="red", linewidth=5, zorder=0)
Route, = ax.plot([], [], 'k', lw=0)
link_l1, = ax.plot([], 'b', lw=2)
link_l2, = ax.plot([], 'r', lw=2)
link_l3, = ax.plot([], 'g', lw=2)
ani = animation.FuncAnimation(figure, update,
                              fargs=(Route, link_l1, link_l2, link_l3))

tri = cv2.imread('dataset/triangle.png')
cv2.imshow('tri', tri)
plt.show()
