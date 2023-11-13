import matplotlib.pyplot as plt
import numpy as np


def theta1(init, theta_2d, i, t=4):
    theta1 = init + (theta_2d * (i ** 2)) / 2
    theta1_d = theta_2d * i
    theta1_2d = theta_2d
    return theta1, theta1_d, theta1_2d


def theta2(init, theta_2d, i, t=4.0):
    theta2 = init + (theta_2d * t * (i - (t / 2)))
    theta2_d = v1
    theta2_2d = 0
    return theta2, theta2_d, theta2_2d


def theta3(transit, theta_2d, i, t=4):
    theta3 = transit - (0.5 * theta_2d * ((t - i) ** 2))
    theta3_d = -(i - (t)) * theta_2d
    theta3_2d = -theta_2d
    return theta3, theta3_d, theta3_2d


init = 30
transit = 50
transit2 = 40
final = 60

t = 4
t2 = 3
t3 = 2
t4 = 1
v1 = ((2 * (transit - init)) / t2) * 0.85
tb1 = (init - transit + (v1 * t2)) / v1
print(v1, tb1)
v2 = ((2 * (final - transit2)) / t2) * 0.85
tb2 = (transit2 - final + (v2 * t2)) / v2
print(v1, tb1, v2, tb2)
theta1_2d = (v1 ** 2) / (init - transit + (v1 * t2))
theta2_2d = (v2 ** 2) / (transit2 - final + (v2 * t2))

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
    # print(i)
    if tb1 <= i < t2 - tb1:
        theta, theta_d, theta_2d = theta2(init, theta1_2d, i, t=tb1)
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(theta_2d)
    # print(i)
    if (t2) - tb1 < i <= t3:
        # if i < tb2:
        # if theta2_2d * i < -(i - t2) * theta1_2d:
        theta, theta_d, theta_2d = theta3(transit, theta1_2d, i, t2)
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(-theta1_2d)
        # print(i)
        # print(i)
        # else:q
        # print(transit - (0.5 * theta1_2d * ((t / 2 - i) ** 2)))
        # theta_list.append(init +(theta1_2d*(i**2))/2)
        # theta_d_list.append(theta2_2d * i)
        # theta_2d_list.append(theta2_2d)
        # print(i)
        # else:
        # print(i)
        #   theta_list.append(transit - (0.5 * theta2_2d * ((t / 2 - i) ** 2)))
        #  theta_d_list.append(v2)
        #  theta_2d_list.append(0)
        # theta_2d_list.append(-theta1_2d)

    if t3 < i <= tb2 + 1:
        theta, theta_d, theta_2d = theta1(init, theta1_2d, i - t4, t=tb1)
        theta_list.append(theta)
        theta_d_list.append(theta_d)
        theta_2d_list.append(theta_2d)

ax1 = plt.subplot(3, 1, 1)
plt.plot(theta_list)
# plt.plot(theta_list2)
plt.title("Position")
# plt.ylabel("Degree")
plt.xticks(visible=False)

plt.subplot(3, 1, 2, sharex=ax1)
plt.plot(theta_d_list)
# plt.plot(theta_d_list2)
plt.title("Velocity")
# plt.ylabel("deg/sec")
plt.xticks(visible=False)

plt.subplot(3, 1, 3, sharex=ax1)
plt.plot(theta_2d_list)
# plt.plot(theta_2d_list2)
plt.title("Acceleration")
# plt.ylabel(r"deg/sec$^2$")
plt.xlabel("Time(seconds)")
# plt.xticks([0,100,200,300,400,500,600],[0,10,20,30,40,50,60])

plt.show()

''' if i<0:
        theta_list2.append(None)
        theta_d_list2.append(None)
        theta_2d_list2.append(None)

         if 0 <= i < tb2:
        theta_list2.append(init + (theta2_2d * (i ** 2)) / 2)
        theta_d_list2.append(theta2_2d * i)
        theta_2d_list2.append(theta2_2d)

            if tb2 <= i < t - tb2:
        theta_list.append(init + (theta2_2d * tb2 * (i - (tb2 / 2))))
        theta_d_list.append(v2)
        theta_2d_list.append(0)'''

'''if tb2 + 1 < i <= t - tb2:
     theta, theta_d, theta_2d = theta2(init, theta2_2d, i, tb2+1)
     theta_list.append(theta)
     theta_d_list.append(theta_d)
     theta_2d_list.append(theta_2d)'''
