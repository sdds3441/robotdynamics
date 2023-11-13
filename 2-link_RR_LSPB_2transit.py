import matplotlib.pyplot as plt
import numpy as np

init = 30
transit = 45
final = 60

t = 4
v1 = ((2 * (transit - init)) / (t / 2)) * 0.85
tb1 = (init - transit + (v1 * (t / 2))) / v1

v2 = ((2 * (final - init)) / t) * 0.85
tb2 = (init - final + (v2 * t)) / v2

theta1_2d = (v1 ** 2) / (init - transit + (v1 * (t / 2)))
theta2_2d = (v2 ** 2) / (init - final + (v2 * t))

const = (4 * (transit - init)) / ((t / 2) ** 2)

theta_list = []
theta_list2 = []
theta_d_list = []
theta_d_list2 = []
theta_2d_list = []
theta_2d_list2 = []

for i in np.arange(0, t, 0.001):
    if i < tb1:
        theta_list.append(init + (theta1_2d * (i ** 2)) / 2)
        theta_d_list.append(theta1_2d * i)
        theta_2d_list.append(theta1_2d)
    if tb1 <= i < (t / 2) - tb1:
        theta_list.append(init + (theta1_2d * tb1 * (i - (tb1 / 2))))
        theta_d_list.append(v1)
        theta_2d_list.append(0)
    if (t / 2) - tb1 < i <= t / 2:
        #theta_list.append(transit - (0.5 * theta1_2d * ((t / 2 - i) ** 2)))

        if i < tb2:
            if theta2_2d * i < -(i - t / 2) * theta1_2d:
                theta_list.append(transit - (0.5 * theta1_2d * ((t / 2 - i) ** 2)))
                theta_d_list.append(-(i - t / 2) * theta1_2d)
                theta_2d_list.append(-theta1_2d)
            else:
                print(transit - (0.5 * theta1_2d * ((t / 2 - i) ** 2)))
                theta_list.append(transit - (0.5 * theta1_2d * ((t / 2 - i) ** 2)))
                theta_d_list.append(theta2_2d * i)
                theta_2d_list.append(theta2_2d)
        else:
            theta_list.append(transit - (0.5 * theta1_2d * ((t / 2 - i) ** 2)))
            theta_d_list.append(v2)
            theta_2d_list.append(0)
        #theta_2d_list.append(-theta1_2d)

    if t / 2 < i < tb2:
        print("dfd")
        theta_list.append(init + (theta2_2d * (i ** 2)) / 2)
        theta_d_list.append(theta2_2d * i)
        theta_2d_list.append(theta2_2d)

    if t - tb2 < i <= t:
        theta_list.append(final - (0.5 * theta2_2d * ((t - i) ** 2)))
        theta_d_list.append(-(i - t) * theta2_2d)
        theta_2d_list.append(-theta2_2d)
# if 50<i:
#     theta_list.append(theta_d_list[-1])
#     theta_2d_list.append(0)


# theta_list.append(a1+a2*(i**2)+a3*(i**3))
# theta_d_list.append(2*a2*i+3*a3*(i**2))
#  theta_2d_list.append(2 * a2 + 6 * a3 * i)

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
