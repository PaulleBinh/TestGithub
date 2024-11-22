import math
import ObliqueShock
import ExpansionFan
def lift_coefficients(L_u_p,L_l_p,T_u_p,T_l_p,M1,gamma,AOAttack,deflect_angle):#L_u_p: Leading upper pressure ratio, T_l_p: Trailing lower pressure ratio
    AOAttack_radians = math.radians(AOAttack)
    deflect_angle_radians =math.radians(deflect_angle)
    a = (1/2)*((L_l_p+T_l_p)-(L_u_p+T_u_p))*math.cos(AOAttack_radians)
    b = (1/2)*((L_l_p+L_u_p)-(T_l_p+T_u_p))*math.tan(deflect_angle_radians)*math.sin(AOAttack_radians)

    coefficient = (a-b)/((gamma/2)*M1**2)
    return coefficient

def drag_coefficients(L_u_p,L_l_p,T_u_p,T_l_p,M1,gamma,AOAttack,deflect_angle):#L_u_p: Leading upper pressure ratio, T_l_p: Trailing lower pressure ratio
    AOAttack_radians = math.radians(AOAttack)
    deflect_angle_radians =math.radians(deflect_angle)
    a = (1/2)*((L_l_p+T_l_p)-(L_u_p+T_u_p))*math.sin(AOAttack_radians)
    b = (1/2)*((L_l_p+L_u_p)-(T_l_p+T_u_p))*math.tan(deflect_angle_radians)*math.cos(AOAttack_radians)

    coefficient = (a+b)/((gamma/2)*M1**2)
    return coefficient

def upper_airfoil_properties(M1,gamma,AOAttack,deflect_angle):
    theta = deflect_angle - AOAttack
    #Leading upper ratio
    if theta >= 0: #Oblique Shock 
        beta = ObliqueShock.Oblique_shock_angle1(theta,M1,gamma)
        M2 = ObliqueShock.Mach_after_oblique_shock(M1,beta,gamma,theta)
        L_u_p = ObliqueShock.pressure_ratio_oblique(M1,beta,gamma)
    else: 
        M2 = ExpansionFan.mach_after_expansion(M1,theta,gamma)
        L_u_p = ExpansionFan.pressure_ratio(M1,M2,gamma)
    #Trailing upper ratio
    M3 = ExpansionFan.mach_after_expansion(M2,2*deflect_angle,gamma)
    T_u_p = ExpansionFan.pressure_ratio(M2,M3,gamma)
    T_u_p = T_u_p * L_u_p # T_U_P / P1
    Upper_pressure = [L_u_p,T_u_p]
    return Upper_pressure

def Lower_airfoil_properties(M1,gamma,AOAttack,deflect_angle):
    theta = deflect_angle + AOAttack
    #Leading upper ratio
    beta = ObliqueShock.Oblique_shock_angle1(theta,M1,gamma)
    M2 = ObliqueShock.Mach_after_oblique_shock(M1,beta,gamma,theta)
    L_l_p = ObliqueShock.pressure_ratio_oblique(M1,beta,gamma)
   
    #Trailing upper ratio
    M3 = ExpansionFan.mach_after_expansion(M2,2*deflect_angle,gamma)
    T_l_p = ExpansionFan.pressure_ratio(M2,M3,gamma)
    T_l_p = T_l_p * L_l_p # T_l_P / P1
    Lower_pressure = [L_l_p,T_l_p]
    return Lower_pressure



def calculate_lift_drag_coefficients(M1,gamma,AOAttack,t_c):
   deflect_angle = math.degrees(math.atan(t_c))
   Upper_pressure = upper_airfoil_properties(M1,gamma,AOAttack,deflect_angle)
   Lower_pressure = Lower_airfoil_properties(M1,gamma,AOAttack,deflect_angle)
   Lift_coefficients = lift_coefficients(Upper_pressure[0],Lower_pressure[0],Upper_pressure[1],Lower_pressure[1],M1,gamma,AOAttack,deflect_angle)
   Drag_coefficients = drag_coefficients(Upper_pressure[0],Lower_pressure[0],Upper_pressure[1],Lower_pressure[1],M1,gamma,AOAttack,deflect_angle) 
   coefficents = [Lift_coefficients,Drag_coefficients] 
   return coefficents


if __name__ == "__main__":
    print("2D wing with diamond airfoil")
    M1 = float(input('input M1: '))
    gamma = float(input('input gamma: '))
    AOAttack = float(input('input AOAttack: '))
    t_c = float(input('input t/c: '))
    deflect_angle = math.atan(t_c)
    result=calculate_lift_drag_coefficients(M1,gamma,AOAttack,t_c)
    lowpressure = Lower_airfoil_properties(M1, gamma, AOAttack, deflect_angle)
    print('Lift coefficient 2D = ', result[0])
    print('Drag coefficient 2D = ',result[1])
