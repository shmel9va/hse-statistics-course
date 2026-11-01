
import numpy as np
from scipy.stats import norm, t

def get_ci(data, method=1, q=0.95, bounds=None):
    x = np.array(data, dtype=float)
    n = len(x)
    if n < 2 or not 0 < q < 1:
        raise ValueError("Некорректная выборка или уровень доверия")

    m, s = x.mean(), x.std(ddof=1)

    if method == 1:
        d = norm.ppf((1 + q) / 2) * s / np.sqrt(n)
    elif method == 2:
        d = t.ppf((1 + q) / 2, n - 1) * s / np.sqrt(n)
    elif method == 3:
        if bounds is None:
            raise ValueError("Укажите границы распределения")
        a, b = bounds
        if a >= b or np.any((x < a) | (x > b)):
            raise ValueError("Некорректные границы")
        d = (b - a) * np.sqrt(np.log(2 / (1 - q)) / (2 * n))
    else:
        raise ValueError("Неизвестный метод")

    return m - d, m + d

x = list(map(float, input("Выборка: ").split()))
method = int(input("Метод (1, 2, 3): "))
q = float(input("Уровень доверия [0.95]: ") or 0.95)
bounds = tuple(map(float, input("Границы a b: ").split())) if method == 3 else None

print("Доверительный интервал:", get_ci(x, method, q, bounds))