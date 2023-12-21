import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(frame, Route, link_l1, ball):
    global start_x
    global start_y

    Route.set_data([start_x], [start_y])

    link_l1_x = [0, x_l1_end[frame]]
    link_l1_y = [0, y_l1_end[frame]]
    link_l1.set_data(link_l1_x, link_l1_y)

    ball_x = ball_x_list[frame]
    ball_y = ball_y_list[frame]
    ball.set_data(ball_x, ball_y)

    return Route, link_l1, ball


outputs = 0
First = True
past_input = 0
distance = []
sec = 0


def pid(kp, ki, kd, input_data, goal):
    global First
    global past_input
    global outputs
    if First:
        outputs = 0
        past_input = 0
    input_diff = input_data - past_input
    error = goal - input_data
    outputs += ki * error
    if 30 < outputs:
        outputs = 30
    elif outputs < -30:
        outputs = -30
    output_data = kp * error
    output_data += outputs - kd * input_diff
    if 30 < output_data:
        output_data = 30
    elif output_data < -30:
        output_data = -30

    if First:
        First = False
    input_data = past_input
    return output_data


l1 = 34

Route_point = 250

start_x = 0
start_y = 10

end_x = 34
end_y = 10

theta1_list = []

x_l1_end = []
y_l1_end = []
ball_x_list = []
ball_y_list = []

x_trajectory = np.linspace(start_x, end_x, Route_point)
y_trajectory = np.linspace(start_y, end_y, Route_point)

csv = np.loadtxt('dataset/dist.csv', delimiter=',')
'''csv 파일없을때 사용
csv = [30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0,
        30.0,
        30.0, 30.0, 30.0, 18.61, 16.4, 16.08, 16.73, 16.08, 16.1, 16.08, 11.37, 11.76, 9.11, 7.68, 7.04, 6.7, 4.78,
        4.78,
        3.81, 3.5, 3.28, 2.94, 2.31, 2.64, 1.99, 2.21, 2.64, 2.96, 2.96, 2.64, 2.64, 2.31, 1.89, 2.96, 2.64, 2.31, 3.28,
        3.93, 3.59, 4.15, 3.5, 3.81, 5.13, 5.15, 5.12, 5.81, 6.07, 8.01, 9.01, 9.45, 11.37, 16.73, 15.78, 15.76, 16.4,
        15.78, 16.4, 15.83, 16.71, 16.4, 18.21, 17.66, 19.33, 20.21, 22.12, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0,
        30.0,
        30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 18.38, 17.88, 16.71, 17.03, 16.71, 15.84, 16.4, 15.76, 16.73, 16.08,
        16.71, 11.14, 10.47, 8.67, 7.99, 7.14, 7.12, 6.8, 5.2, 4.88, 5.2, 5.53, 5.53, 5.2, 4.88, 5.85, 4.88, 6.49, 6.49,
        7.67, 7.99, 7.68, 9.01, 10.13, 11.05, 30.0, 15.86, 16.73, 16.4, 16.08, 15.76, 15.45, 16.73, 16.4, 16.08, 16.08,
        30.0, 17.7, 19.57, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0,
        30.0,
        17.68, 17.99, 16.39, 16.08, 16.71, 15.78, 15.76, 15.78, 16.1, 16.4, 16.47, 16.73, 12.39, 11.05, 10.47, 9.01,
        8.77,
        8.67, 8.43, 7.79, 8.31, 7.34, 8.31, 7.74, 8.42, 7.77, 9.69, 10.03, 9.88, 10.46, 15.76, 11.14, 12.73, 13.52,
        15.2,
        15.78, 15.78, 16.08, 16.73, 16.01, 16.73, 16.4, 16.08, 15.78, 16.4, 15.62, 15.45, 16.4, 16.1, 15.78, 15.52,
        16.73,
        16.4, 16.08, 16.08, 16.08, 16.4, 16.4, 16.4, 16.4, 16.73, 16.71, 16.4, 16.4, 16.71, 16.4, 16.73, 16.4, 16.4,
        16.73,
        16.73, 16.73, 16.17, 16.73, 16.73, 16.4, 16.4, 16.27, 16.4, 16.4, 16.4, 16.4, 16.4, 16.4, 16.4, 16.4]
'''
for i in range(Route_point):
    distance = np.sqrt(x_trajectory[i] ** 2 + y_trajectory[i] ** 2)
    ball_dist = csv[i]
    theta1 = pid(2, 0, 1, ball_dist, 15)
    theta1 = np.deg2rad(theta1)

    ball_x_list.append(30 - ball_dist)
    ball_y_list.append((30 - ball_dist) * np.sin(theta1) + 1)
    x_l1_end.append(l1 * np.cos(theta1))
    y_l1_end.append(l1 * np.sin(theta1))

figure, ax = plt.subplots()
ax.set_xlim(0, 40)
ax.set_ylim(-20, 20)
Route, = ax.plot([], [], 'k')
link_l1, = ax.plot([], 'b', lw=10)
ball, = ax.plot([], 'or')

ani = animation.FuncAnimation(figure, update, fargs=(Route, link_l1, ball))

plt.show()
