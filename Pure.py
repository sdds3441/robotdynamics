import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 2-링크 로봇 매개변수 정의
l1 = 1.0  # 첫 번째 링크 길이
l2 = 1.0  # 두 번째 링크 길이

# 시간 관련 매개변수 정의
total_time = 5.0  # 운동의 총 시간
num_points = 100  # 운동의 점 개수

# 원하는 엔드-이펙터 궤적 정의
x_desired = np.linspace(0.0, 1.5, num_points)
y_desired = np.linspace(0.0, 0.5, num_points)

# 관절 각도와 엔드-이펙터 위치를 저장할 배열 초기화
theta1_array = []
theta2_array = []
x_end_effector = []
y_end_effector = []

for i in range(num_points):
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

    # 엔드-이펙터 위치를 순방향 기구학을 사용하여 계산
    x_end_effector.append(l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2))
    y_end_effector.append(l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2))


# 애니메이션에서 로봇 팔의 위치를 업데이트하는 함수 정의
def update(frame, line, points, links):
    line.set_data([0, x_end_effector[frame]], [0, y_end_effector[frame]])
    points.set_data(x_end_effector[frame], y_end_effector[frame])

    # 로봇 팔의 링크 위치를 업데이트
    link_x = [0, l1 * np.cos(theta1_array[frame]), x_end_effector[frame]]
    link_y = [0, l1 * np.sin(theta1_array[frame]), y_end_effector[frame]]
    links.set_data(link_x, link_y)

    return line, points, links


# 애니메이션을 위한 피겨와 축 생성
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], lw=2)
points, = ax.plot([], [], 'ro', markersize=10)
links, = ax.plot([], [], lw=2)

# 애니메이션 생성
ani = animation.FuncAnimation(fig, update, frames=range(num_points), fargs=(line, points, links), blit=True)

plt.show()