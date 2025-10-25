#importing req libraries- numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv

R = 10
L = 50e-3
C = 100e-6

#create the freq range 
f=np.linspace(10,5000,5000)

X_L= 2 * np.pi * f * L      #inductive reactance 
X_C=1/(2 * np.pi * f * C)   #capacitive reactance

#total impedance
Z=np.sqrt(R**2 + (X_L - X_C)**2)

#resonant freq
f_r = 1/(2 * np.pi * np.sqrt(L*C))
print(f"resonant frequency = {f_r:2f} hz")
Z_min = R

#plot the graph
plt.figure(figsize=(10,6))
plt.plot(f,Z , label='Impedance (Z)' , linewidth=2)
plt.axvline(f_r , color='r' , linestyle='--' , label=f'Resonant Frequency ({f_r:.2f} Hz)')
plt.scatter(f_r , Z_min , color='g' , zorder=5)
plt.text(f_r+50 , Z_min+2 , f'Z_min={Z_min:.2f}' , color='g')
plt.title('Series RLC Circuit: Impedance vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance (Ohms)')
plt.legend()
plt.grid(True)
plt.savefig('outputrlc.png')
plt.show()




