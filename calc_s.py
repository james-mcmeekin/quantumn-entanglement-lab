from calc_e import calc_e

def calc_s(alpha, beta, aprime, betaprime, state="non"):
    return abs(calc_e(alpha, beta, state) - calc_e(alpha, betaprime, state) + calc_e(aprime, beta, state) + calc_e(aprime, betaprime, state))

calc_s(0, 45, 22.5, 67.5, "non") 
calc_s(0, 45, 22.5, 67.5, "sym") # 2.8284271247461903