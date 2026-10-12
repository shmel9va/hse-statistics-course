import numpy as np
from scipy.stats import skew, kurtosis

x = np.array([1, 2, 3, 4, 5, 6, 7])

print("Матожидание:", x.mean())
print("Медиана:", np.median(x))
print("Дисперсия (смещенная / несмещенная):", x.var(), x.var(ddof=1))
print("СКО (обычное / исправленное):", x.std(), x.std(ddof=1))
print("Асимметрия:", skew(x, bias=False))
print("Эксцесс:", kurtosis(x, bias=False))