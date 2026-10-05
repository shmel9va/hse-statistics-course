import numpy as np
from scipy.optimize import minimize

def MLE(pdf, x, p0):
    return minimize(lambda p: -np.log(pdf(np.asarray(x), p)).sum(), p0).x