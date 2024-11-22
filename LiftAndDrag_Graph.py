import Wing_2D
import matplotlib.pyplot as plt
import math
import random
import Wing_3D

def Plot_Lift_vs_alpha ( ):
    M1 = 2
    gamma = 1.4
    AOAttack = 0
    t_c = 0.08749
    Lift_list=[]
    alpha_list=[]
    for j in range (0,8):
        Lift_list=[]
        alpha_list=[]
        AOAttack = 0
        for i in range (0,30):
        
            result=Wing_2D.calculate_lift_drag_coefficients(M1,gamma,AOAttack,t_c)
            Lift_list.append(result[0])
            alpha_list.append(AOAttack)
        
            #M1=M1+1
            AOAttack += 0.5
        random_color = (random.random(), random.random(), random.random())
        plt.plot(alpha_list, Lift_list, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
        M1+=1
    #plt.plot(z, y, marker='o', linestyle='-', color='r', label='Variable Z')
    # Add labels and title
    
    # Create a line plot
    
    plt.xlabel('Alpha-degree')
    plt.ylabel('Lift coefficient')
    plt.title('Lift vs AOA (same t/c)')
    plt.legend()
    # Show the plot
    return plt.show()


def Plot_Drag_vs_alpha ( ):
    M1 = 2
    gamma = 1.4
    AOAttack = 0
    t_c = 0.08749
    Lift_list=[]
    alpha_list=[]
    for j in range (0,8):
        Lift_list=[]
        alpha_list=[]
        AOAttack = 0
        for i in range (0,30):
        
            result=Wing_2D.calculate_lift_drag_coefficients(M1,gamma,AOAttack,t_c)
            Lift_list.append(result[1])
            alpha_list.append(AOAttack)
        
            #M1=M1+1
            AOAttack += 0.5
        random_color = (random.random(), random.random(), random.random())
        plt.plot(alpha_list, Lift_list, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
        M1+=1
    #plt.plot(z, y, marker='o', linestyle='-', color='r', label='Variable Z')
    # Add labels and title
    
    # Create a line plot
    
    plt.xlabel('Alpha-degree')
    plt.ylabel('Drag coefficient')
    plt.title('Drag vs AOA (same t/c)')
    plt.legend()
    # Show the plot
    return plt.show()

def Plot_Drag_vs_alpha_t_cIncrease ( ):
    M1 = 2
    gamma = 1.4
    AOAttack = 0
    t_c = 0.08749
    Lift_list=[]
    alpha_list=[]
    for j in range (0,8):
        Lift_list=[]
        alpha_list=[]
        AOAttack = 0
        for i in range (0,30):
        
            result=Wing_2D.calculate_lift_drag_coefficients(M1,gamma,AOAttack,t_c)
            Lift_list.append(result[1])
            alpha_list.append(AOAttack)
        
            #M1=M1+1
            AOAttack += 0.5
        random_color = (random.random(), random.random(), random.random())
        plt.plot(alpha_list, Lift_list, marker='o', linestyle='-', color=random_color, label=f't/c = {t_c}')
        t_c+=0.00595
    #plt.plot(z, y, marker='o', linestyle='-', color='r', label='Variable Z')
    # Add labels and title
    
    # Create a line plot
    
    plt.xlabel('Alpha-degree')
    plt.ylabel('Drag coefficient')
    plt.title('Drag vs AOA (same M = 2)')
    plt.legend()
    # Show the plot
    return plt.show()


def Plot_Drag_vs_t_cIncrease_ ( ):
    M1 = 2
    gamma = 1.4
    AOAttack = 0
    
    drag_list=[]
    t_c_list=[]
    for j in range (0,8):
        drag_list=[]
        t_c_list=[]
        t_c = 0.0
        for i in range (0,30):
        
            result=Wing_2D.calculate_lift_drag_coefficients(M1,gamma,AOAttack,t_c)
            drag_list.append(result[1])
            t_c_list.append(t_c)
        
            #M1=M1+1
            t_c += 0.01
        random_color = (random.random(), random.random(), random.random())
        plt.plot(t_c_list, drag_list, marker='o', linestyle='-', color=random_color, label=f'Mach = {M1}')
        M1+=0.5
    #plt.plot(z, y, marker='o', linestyle='-', color='r', label='Variable Z')
    # Add labels and title
    
    # Create a line plot
    
    plt.xlabel('t/c')
    plt.ylabel('Drag coefficient')
    plt.title('Drag vs thickness ratio (same alpha = 0)')
    plt.legend()
    # Show the plot
    return plt.show()

def plot_2D_alpha (M1,gamma,t_c):
    plt.figure(figsize=(15, 5))

    Lift_list=[]
    alpha_list=[]
    Drag_list=[]
    Efficiency=[]
    AOAttack = -10
    for i in range (0,40):
        
        result=Wing_2D.calculate_lift_drag_coefficients(M1,gamma,AOAttack,t_c)
        Lift_list.append(result[0])
        Drag_list.append(result[1])
        Efficiency.append(result[0]/result[1])
        alpha_list.append(AOAttack)
        
        #M1=M1+1
        AOAttack += 0.5
    plt.subplot(1, 3, 1)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(alpha_list, Lift_list, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
    plt.xlabel('Alpha-degree')
    plt.ylabel('Lift coefficient')
    plt.title('Lift vs AOA (same t/c & Mach)')
    plt.legend()

    plt.subplot(1, 3, 2)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(alpha_list, Drag_list, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
    plt.xlabel('Alpha-degree')
    plt.ylabel('Drag coefficient')
    plt.title('Drag vs AOA (same t/c & Mach)')
    plt.legend()

    plt.subplot(1, 3, 3)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(alpha_list, Efficiency, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
    plt.xlabel('Alpha-degree')
    plt.ylabel('Efficiency (CL/CD)')
    plt.title('Efficiency vs AOA (same t/c & Mach)')
    plt.legend()
    #plt.plot(z, y, marker='o', linestyle='-', color='r', label='Variable Z')
    # Add labels and title
    
    # Create a line plot
    return plt.show()
   

def plot_3D_alpha (M1,gamma,t_c,swept):
    plt.figure(figsize=(15, 5))

    Lift_list=[]
    alpha_list=[]
    Drag_list=[]
    Efficiency=[]
    AOAttack = -8
    for i in range (0,35):
        
        result_eq = Wing_3D.eq(M1,swept,AOAttack,t_c)
        result = Wing_3D.calculate_lift_drag_3D(result_eq[0],gamma,result_eq[1],result_eq[2],swept)
        Lift_list.append(result[0])
        Drag_list.append(result[1])
        Efficiency.append(result[0]/result[1])
        alpha_list.append(AOAttack)
        
        #M1=M1+1
        AOAttack += 0.5
    plt.subplot(1, 3, 1)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(alpha_list, Lift_list, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
    plt.xlabel('Alpha-degree')
    plt.ylabel('Lift coefficient')
    plt.title('Lift vs AOA (same t/c & Mach & Swept)')
    plt.legend()

    plt.subplot(1, 3, 2)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(alpha_list, Drag_list, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
    plt.xlabel('Alpha-degree')
    plt.ylabel('Drag coefficient')
    plt.title('Drag vs AOA (same t/c & Mach & Swept)')
    plt.legend()

    plt.subplot(1, 3, 3)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(alpha_list, Efficiency, marker='o', linestyle='-', color=random_color, label=f'Mach M = {M1}')
    plt.xlabel('Alpha-degree')
    plt.ylabel('Efficiency (CL/CD)')
    plt.title('Efficiency vs AOA (same t/c & Mach & Swept)')
    plt.legend()
    #plt.plot(z, y, marker='o', linestyle='-', color='r', label='Variable Z')
    # Add labels and title
    
    # Create a line plot
    return plt.show()
if __name__ == "__main__":
    print("2D wing with diamond airfoil")
    M1 = float(input('input M1: '))
    gamma = float(input('input gamma: '))
    #AOAttack = float(input('input AOAttack: '))
    t_c = float(input('input t/c: '))
    swept = float(input('input Swept angle: '))
    #plot_2D_alpha (M1,gamma,t_c)
    plot_3D_alpha (M1,gamma,t_c,swept)
    #Plot_Lift_vs_alpha()
    #Plot_Drag_vs_alpha ()
    #Plot_Drag_vs_alpha_t_cIncrease ( )
    #Plot_Drag_vs_t_cIncrease_ ( )

