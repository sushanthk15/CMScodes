#Author:Sushanth Keshav
#Function to plot the trajectories of dislocations
#Date:26-05-2019
import numpy as np
import matplotlib.pyplot as plt

#System Definitions
# Introducing the constants and terms used for the code below
length = 2e-6 # System Length in X-Direction (micro-meters)
shear_modulus = 26e9 # Shear Modulus in GPa
poissons_ratio = 0.33
burgers_vector = 0.256e-9 # in Nano-meter
braggs_coeff = 1e-4 # Dragg Coeffecient in (Pas)
total_time = 10e-9 #seconds
n_dislocations = 4 #number of dislocations
initial_position = length * np.array([0.1,0.13,0.16,0.3])
n_steps = 100
delta_t = total_time/100

def get_internal_stress(x,shear_modulus,poissons_ratio,burgers_vector):
    D = (1)*shear_modulus*burgers_vector/(2*np.pi*(1-poissons_ratio))
    tau = []
    for i in x:
        x_new = [] #tau elemental
        for j in x:
            if (j)!= i :
                x_new.append(D/(i-j))
        tau.append(np.sum(x_new))
    return np.array(tau)
#Function to plot the Trajectories
def plot_trajectories(times,positions):
    plt.title('Trajectory of dislocations', fontsize = 20)
    plt.ylabel('times[ns]', fontsize = 20)
    plt.xlabel('Position of Dislocations[$\mu$m]', fontsize = 20)
    plt.plot((np.asarray(positions)*1e6),(np.asarray(times)*1e9), marker='')
    plt.legend(("Dislocation 1", "Dislocation 2","Dislocation 3","Dislocation 4"))
    plt.tight_layout()
    plt.savefig('DislocationTrajectories_task3.png')
    plt.close()
x_coords = initial_position
times=[0.]
x_old = initial_position
positions = [initial_position]
for n in range(n_steps):
    tau=get_internal_stress(x_old,shear_modulus,poissons_ratio,burgers_vector)
    v = burgers_vector/braggs_coeff*tau
    x_old =x_old+delta_t*v
    positions.append(x_old)
    times.append((n+1)*delta_t)

plot_trajectories(times,positions)
