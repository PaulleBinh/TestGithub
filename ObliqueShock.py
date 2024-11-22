import math
import numpy as np
def Oblique_shock_angle (theta,M1,gamma):
    a = ((1+((gamma-1)/2)*M1**2)*math.tan(math.radians(theta)))
    b = (M1**2)-1
    c = ((1+((gamma+1)/2)*M1**2)*math.tan(math.radians(theta)))
    d = 1
    coefficients = [a, b, c, d]

    # Find the roots
    roots = np.roots(coefficients)
    beta = roots[1]
    beta1 = math.degrees(math.atan(beta))
    return beta1

def Oblique_shock_angle1 (theta,M,gamma):
    # Iterate to find Beta
    Beta1=0
    Beta = 1
    Beta_new = 1000 
    theta1 = math.radians(theta)
    while abs(Beta_new - Beta1) > 1e-6:
        f = (2 * (M**2 * np.sin(Beta)**2 - 1) / (np.tan(Beta) * (2 + M**2 * (gamma + np.cos(2 * Beta))))) - np.tan(theta1)
        f_prime = (2 * (M**4 * np.sin(Beta)**3 * (1 + gamma * np.cos(2 * Beta)) + M**2 * (2 * np.cos(2 * Beta) + gamma - 1)) / (np.sin(Beta)**2 * (2 + M**2 * (gamma + np.cos(2 * Beta))))) 
        Beta_new = Beta - f / f_prime
        if abs(Beta_new - Beta) < 1e-6:
            Beta = Beta_new
            Beta_deg = np.degrees(Beta)  # Convert Beta to degrees
            break
           
        else:
            Beta1 = Beta 
            Beta = Beta_new
            Beta_deg = None  # If max iterations are reached without convergence

    return Beta_deg

def Mach_after_oblique_shock(M1, beta, gamma, theta):
    beta1 = math.radians(beta)
    theta1 = math.radians(theta)
    Mn1 = M1 * math.sin(beta1)  # Normal component of Mach number

    # If Mn1 < 1, use expansion wave logic instead
    # Calculate Mn2, the normal Mach number after the shock
    term1 = (1 + ((gamma - 1) / 2) * Mn1**2)
    term2 = (gamma * Mn1**2 - ((gamma - 1) / 2))

    if term2 <= 0:
        raise ValueError("Math domain error in calculating Mn2. Check M1 and beta values for valid range.")

    Mn2 = math.sqrt(term1 / term2)

    # Calculate the Mach number after the oblique shock in the downstream direction
    return Mn2 / math.sin(beta1 - theta1)

def pressure_ratio_oblique(M1, beta, gamma): #P2/P1
    beta1 = math.radians(beta)
    Mn1 = M1 * math.sin(beta1)
    ratio = 1 + ((2 * gamma * (Mn1**2 - 1)) / (gamma + 1))
    return ratio

if __name__ == "__main__":
    print("2D wing with diamond airfoil")
    M1 = float(input('input M1: '))
    gamma = float(input('input gamma: '))
    AOAttack = float(input('input AOAttack: '))
    t_c = float(input('input t/c: '))
    
    print(Oblique_shock_angle1 (5,M1,gamma))
