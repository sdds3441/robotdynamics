import matplotlib.pyplot as plt
import numpy as np

init = 30
transit = 45
final = 60

t = 4
v1 = ((2 * (transit - init)) / (t / 2)) * 0.85
tb1 = (init - transit + (v1 * (t / 2))) / (v1)

theta1_2d = (v1 ** 2) / (init - transit + (v1 * (t / 2)))

const = (4 * (transit - init)) / ((t / 2) ** 2)

theta_list = []
theta_d_list = []
theta_2d_list = []

for i in np.arange(0, t, 0.001):
    if i < 0.824:
        theta_list.append(init + (theta1_2d * (i ** 2)) / 2)
        theta_d_list.append(theta1_2d * i)
        theta_2d_list.append(theta1_2d)
    if 0.824 <= i < 1.176:
        theta_list.append(init + (theta1_2d * tb1 * (i - (tb1 / 2))))
        theta_d_list.append(v1)
        theta_2d_list.append(0)
    if 1.176 < i <= t / 2:
        theta_list.append(transit - (0.5 * theta1_2d * ((t / 2 - i) ** 2)))
        theta_d_list.append(-(i - t / 2) * theta1_2d)
        theta_2d_list.append(-theta1_2d)

# if 50<i:
#     theta_list.append(theta_d_list[-1])
#     theta_2d_list.append(0)


# theta_list.append(a1+a2*(i**2)+a3*(i**3))
# theta_d_list.append(2*a2*i+3*a3*(i**2))
#  theta_2d_list.append(2 * a2 + 6 * a3 * i)

ax1 = plt.subplot(3, 1, 1)
plt.plot(theta_list)
plt.title("Position")
# plt.ylabel("Degree")
plt.xticks(visible=False)

plt.subplot(3, 1, 2, sharex=ax1)
plt.plot(theta_d_list)
plt.title("Velocity")
# plt.ylabel("deg/sec")
plt.xticks(visible=False)

plt.subplot(3, 1, 3, sharex=ax1)
plt.plot(theta_2d_list)
plt.title("Acceleration")
# plt.ylabel(r"deg/sec$^2$")
plt.xlabel("Time(seconds)")
# plt.xticks([0,100,200,300,400,500,600],[0,10,20,30,40,50,60])

plt.show()
