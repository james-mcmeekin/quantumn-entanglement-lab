from calc_c import calc_c

def calc_dolp(alpha,state="non"):

    Ipll = calc_c(alpha, alpha, state)
    Iperp = calc_c(alpha, alpha+90, state)

    return (Ipll - Iperp)/(Ipll + Iperp)

print(calc_dolp(0, "non")) # 1
print(calc_dolp(0, "sym"))  # 1
print(calc_dolp(0, "anti")) # 1
print(calc_dolp(15, "non")) # 0.75
print(calc_dolp(15, "sym"))  # 1
print(calc_dolp(15, "anti")) # 0.5
print(calc_dolp(30, "non"))  # 0.25
print(calc_dolp(30, "sym"))  # 1
print(calc_dolp(30, "anti")) # -0.5
print(calc_dolp(45, "non"))  # 0.0
print(calc_dolp(45, "sym"))  # 1
print(calc_dolp(45, "anti")) # -1
print(calc_dolp(60, "non"))  # 0.25
print(calc_dolp(60, "sym"))  # 1
print(calc_dolp(60, "anti")) # -0.5
print(calc_dolp(75, "non"))  # 0.75
print(calc_dolp(75, "sym"))  # 1
print(calc_dolp(75, "anti")) # -0.5
print(calc_dolp(90, "non"))  # 1
print(calc_dolp(90, "sym"))  # 1
print(calc_dolp(90, "anti")) # 1

