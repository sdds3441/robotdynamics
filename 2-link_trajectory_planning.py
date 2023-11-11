import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(frame, Route, link_l1, link_l2):
    global start_x
    global start_y

    Route.set_data([start_x, x_end_effector[frame]], [start_y, y_end_effector[frame]])

    # 로봇 팔의 링크 위치를 업데이트
    link_l1_x = [0, x_l1_end[frame]]
    link_l1_y = [0, y_l1_end[frame]]
    link_l1.set_data(link_l1_x, link_l1_y)

    link_l2_x = [l1 * np.cos(theta1_array[frame]), x_end_effector[frame]]
    link_l2_y = [l1 * np.sin(theta1_array[frame]), y_end_effector[frame]]
    link_l2.set_data(link_l2_x, link_l2_y)

    return Route, link_l1, link_l2


l1 = 5
l2 = 4

Route_point = 10

start_x = 2
start_y = 5

end_x = 4.5
end_y = 6.5

x_desired = np.linspace(start_x, end_x, Route_point)
y_desired = np.linspace(start_y, end_y, Route_point)

# 관절 각도와 엔드-이펙터 위치를 저장할 배열 초기화
theta1_array = []
theta2_array = []
theta3_array = []
x_end_effector = []
y_end_effector = []
x_l1_end = []
y_l1_end = []
x_l2_end = []
y_l2_end = []

for i in range(Route_point):
    # 원하는 엔드-이펙터 위치를 보간
    x = x_desired[i]
    y = y_desired[i]

    # 역기구학을 사용하여 관절 각도 계산
    # 여기에 역기구학 해결 방법을 구현합니다.
    # 단순성을 위해 이전 예제와 동일한 코드를 사용하겠습니다.
    distance = np.sqrt(x ** 2 + y ** 2)
    if distance > (l1 + l2) or distance < abs(l1 - l2):
        raise ValueError("원하는 위치가 로봇의 작업 영역 밖에 있습니다.")
    cos_theta2 = (x ** 2 + y ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
    sin_theta2 = np.sqrt(1 - cos_theta2 ** 2)
    theta2 = np.arctan2(sin_theta2, cos_theta2)
    alpha = np.arctan2(l2 * sin_theta2, l1 + l2 * cos_theta2)
    beta = np.arctan2(y, x)
    theta1 = beta - alpha

    theta1_array.append(theta1)
    theta2_array.append(theta2)
    theta3_array.append(theta1 - theta2)

    # 엔드-이펙터 위치를 순방향 기구학을 사용하여 계산
    x_l1_end.append(l1 * np.cos(theta1))
    y_l1_end.append(l1 * np.sin(theta1))
    x_l2_end.append(l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2))
    y_l2_end.append(l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2))
    x_end_effector.append(l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2))
    y_end_effector.append(l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2))

    print(x, y)

# 애니메이션에서 로봇 팔의 위치를 업데이트하는 함수 정의

# 애니메이션을 위한 피겨와 축 생성
figure, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
Route, = ax.plot([], [], 'k')
link_l1, = ax.plot([], 'b', lw=10)
link_l2, = ax.plot([], 'r',lw=10)

# 애니메이션 생성
ani = animation.FuncAnimation(figure, update, frames=range(Route_point), fargs=(Route, link_l1, link_l2))
plt.title("2-link trajectory planning")
plt.text(8.25, 8 + 1 / 2, 'x')
plt.text(9.25, 8 + 1 / 2, 'y')
for i in range(len(x_desired)):
    plt.text(8, 8 - i / 2, round(x_desired[i], 3))
    plt.text(9, 8 - i / 2, round(y_desired[i], 3))
plt.show()
