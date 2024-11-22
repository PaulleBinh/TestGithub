import math

def prandtl_meyer(M,gamma):
    if M <= 1:
        raise ValueError("Mach number must be greater than 1 for Prandtl-Meyer expansion calculations.")
    return math.sqrt((gamma + 1) / (gamma - 1)) * math.atan(math.sqrt(((gamma - 1) * (M**2 - 1)) / (gamma + 1))) - math.atan(math.sqrt(M**2 - 1))

def mach_after_expansion(M1, theta,gamma):
    # Target Prandtl-Meyer angle
    nu1 = prandtl_meyer(M1,gamma)
    nu2 = math.degrees(nu1)
    nu_target = nu2 + theta
    M2_lower, M2_upper = M1, 10.0  # Search range for M2

    # Bisection method to find M2
    while (M2_upper - M2_lower) > 1e-6:
        M2 = (M2_upper + M2_lower) / 2
        if math.degrees(prandtl_meyer(M2,gamma)) < nu_target:
            M2_lower = M2
        else:
            M2_upper = M2
    return M2
def pressure_ratio(M1,M2,gamma): #P2/P1
    ratio = ((1+((gamma-1)/2)*(M1**2))/(1+((gamma-1)/2)*(M2**2)))**(gamma/(gamma-1))
    return ratio

if __name__ == "__main__":
    print("2D wing with diamond airfoil")
    M1 = float(input('input M1: '))
    gamma = float(input('input gamma: '))
    AOAttack = float(input('input AOAttack: '))
    t_c = float(input('input t/c: '))
    mach_after_expansion(M1, gamma,gamma)
