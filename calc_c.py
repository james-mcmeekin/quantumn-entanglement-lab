import numpy as np

def P(theta):
    rad = np.radians(theta)
    return np.matrix([[np.cos(rad)**2, np.cos(rad)*np.sin(rad)],
                      [np.cos(rad)*np.sin(rad), np.sin(rad)**2]])

def evaluate(x, A, y):
    return (x.T @ A @ y).item()


def calc_c(alpha, beta, state="non"):

    Palpha = P(alpha)
    Pbeta = P(beta)

    v = np.matrix([[1], [0]])
    h = np.matrix([[0], [1]])

    cnon = 1/2 * ((evaluate(v, Palpha, v))*(evaluate(v, Pbeta, v)) + (evaluate(h, Palpha, h))*(evaluate(h, Pbeta, h)))
    cross = 1/2 *((evaluate(v, Palpha, h))*(evaluate(v, Pbeta, h)) + (evaluate(h, Palpha, v))*(evaluate(h, Pbeta, v)))
    if state == "non":
        return cnon
    elif state == "sym":
        return cnon + cross
    else:
        return cnon - cross
