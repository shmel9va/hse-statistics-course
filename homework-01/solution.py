import numpy as np
import matplotlib.pyplot as plt

x = list(map(float, input().split()))  # Выборка
p = float(input())                     # Вероятность

plt.ecdf(x)  # Оценка функции распределения Fr*(x)
plt.show()

# Квантиль: минимальное x, при котором Fr*(x) ≥ p
print(np.quantile(x, p, method="inverted_cdf"))

# Альтернатива: квантиль с линейной интерполяцией
# print(np.quantile(x, p))