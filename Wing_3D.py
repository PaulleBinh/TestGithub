import math
import ObliqueShock
import ExpansionFan
import Wing_2D
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

def eq(M1,swept,AOAattack, t_c):
    AOAradians = math.radians(AOAattack)
    swept_radians = math.radians(swept)
    M_eq = M1 * math.sqrt(1-((math.sin(swept_radians))**2 * (math.cos(AOAradians))**2))
    AOAeq = math.atan(math.tan(AOAradians)/ math.cos(swept_radians) )
    tc_eq =t_c/(math.cos(swept_radians))
    eq_properties = [M_eq , AOAeq,tc_eq]
    return eq_properties

def calculate_lift_drag_3D(M_eq, gamma, AOAeq, tc_eq, swept):
    deflect_angle = math.degrees(math.atan(tc_eq))
    deflect_radians = math.radians(deflect_angle)
    swept_radians = math.radians(swept)
    coefficients = Wing_2D.calculate_lift_drag_coefficients(M_eq,gamma,math.degrees(AOAeq),tc_eq) 
    #Upper_pressure = upper_airfoil_properties(M_eq,gamma,AOA_eq,deflect_angle)
    #Lower_pressure = Lower_airfoil_properties(M_eq,gamma,AOA_eq,deflect_angle)
    #CL_eq = (gamma * M_eq**2 / (4* math.cos(deflect_radians)))* ((Lower_pressure[0] -Upper_pressure[1])*math.sin(deflect_radians+AOA_eq) + (Upper_pressure[0]-Lower_pressure[1])*math.sin(deflect_radians-AOA_eq))
    #CD_eq = (gamma * M_eq**2 / (4* math.cos(deflect_radians)))* ((Lower_pressure[0] -Upper_pressure[1])*math.cos(deflect_radians+AOA_eq) + (-Upper_pressure[0]+Lower_pressure[1])*math.cos(deflect_radians-AOA_eq))
    CL3D = coefficients[0] * ((1- (((math.sin(swept_radians))**2) * ((math.cos(AOAeq))**2))))
    CD3D = coefficients[1] * math.cos(swept_radians)* (1- ((math.sin(swept_radians))**2) * ((math.cos(AOAeq))**2))
    result_3D = [CL3D, CD3D]
    return result_3D
    

if __name__ == "__main__":
    print("3D wing with diamond airfoil")
    M1 = float(input('input M1: '))
    gamma = float(input('input gamma: '))
    AOAttack = float(input('input AOAttack: '))
    t_c = float(input('input t/c: '))
    swept = float(input("input the swpet angle: "))
    Eq_value = eq(M1,swept,AOAttack, t_c)
    Result = calculate_lift_drag_3D(Eq_value[0],gamma,Eq_value[1],Eq_value[2],swept)
    print(Eq_value)
    print('degree',math.degrees(Eq_value[1]))
    print('Lift coefficient 3D: ', Result[0])
    print('Drag coefficient 3D: ', Result[1])
    Result2D = Wing_2D.calculate_lift_drag_coefficients(Eq_value[0],gamma,math.degrees(Eq_value[1]),Eq_value[2])
    print('Lift coefficient 2D: ', Result2D[0])
    print('Drag coefficient 2D: ', Result2D[1])

    
