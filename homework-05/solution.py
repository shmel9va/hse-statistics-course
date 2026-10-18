import numpy as np

def bootci(est, x):
    # 10 000 выборок размера len(x) с возвращением; для каждой вычисляем оценку est
    estimates = [est(np.random.choice(x, len(x))) for _ in range(10000)]
    # Квантили 2,5% и 97,5% - границы 95%-го процентильного бутстреп-интервала
    return np.quantile(estimates, [0.025, 0.975])

x = [1, 2, 3, 4, 5]
print(bootci(np.mean, x))  # Доверительный интервал для среднего