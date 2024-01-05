import random

import matplotlib.pyplot as plt


def calculate_pi(num_points):
    points_inside_circle = 0
    total_points = 0
    pi_values = []

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            points_inside_circle += 1
        total_points += 1

        pi_values.append(4 * points_inside_circle / total_points)

    return pi_values


# 使用100000个点来计算圆周率
pi_values = calculate_pi(1000)

# 绘制圆周率的估计值
plt.plot(pi_values)
plt.xlabel("Iterations")
plt.ylabel("Estimate of pi")
plt.show()
