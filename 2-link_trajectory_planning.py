import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(frame, Route, link_l1, link_l2):
    global start_x
    global start_y

    Route.set_data([start_x, x_l2_end[frame]], [start_y, y_l2_end[frame]])

    link_l1_x = [0, x_l1_end[frame]]
    link_l1_y = [0, y_l1_end[frame]]
    link_l1.set_data(link_l1_x, link_l1_y)

    link_l2_x = [l1 * np.cos(theta1_list[frame]), x_l2_end[frame]]
    link_l2_y = [l1 * np.sin(theta1_list[frame]), y_l2_end[frame]]
    link_l2.set_data(link_l2_x, link_l2_y)

    return Route, link_l1, link_l2


l1 = 5
l2 = 4

Route_point = 10

start_x = 2
start_y = 5

end_x = 4.5
end_y = 6.5

x_trajectory = np.linspace(start_x, end_x, Route_point)
y_trajectory = np.linspace(start_y, end_y, Route_point)

theta1_list = []
theta2_list = []
x_l1_end = []
y_l1_end = []
x_l2_end = []
y_l2_end = []

for i in range(Route_point):
    distance = np.sqrt(x_trajectory[i] ** 2 + y_trajectory[i] ** 2)
    c2 = (x_trajectory[i] ** 2 + y_trajectory[i] ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
    s2 = np.sqrt(1 - c2 ** 2)
    theta2 = np.arctan2(s2, c2)
    c1 = (x_trajectory[i] * (l1 + l2 * c2) + y_trajectory[i] * l2 * s2)
    s1 = (y_trajectory[i] * (l1 + l2 * c2) - x_trajectory[i] * l2 * s2)

    theta1 = np.arctan2(s1, c1)
    theta1_list.append(theta1)
    theta2_list.append(theta2)

    x_l1_end.append(l1 * np.cos(theta1))
    y_l1_end.append(l1 * np.sin(theta1))
    x_l2_end.append(l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2))
    y_l2_end.append(l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2))

figure, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
Route, = ax.plot([], [], 'k')
link_l1, = ax.plot([], 'b', lw=10)
link_l2, = ax.plot([], 'r', lw=10)

ani = animation.FuncAnimation(figure, update, frames=range(Route_point), fargs=(Route, link_l1, link_l2))
plt.title("2-link trajectory planning")
plt.text(8.25, 8 + 1 / 2, 'x')
plt.text(9.25, 8 + 1 / 2, 'y')
for i in range(len(x_trajectory)):
    plt.text(8, 8 - i / 2, round(x_trajectory[i], 3))
    plt.text(9, 8 - i / 2, round(y_trajectory[i], 3))
plt.show()
