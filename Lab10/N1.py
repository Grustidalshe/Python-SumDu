import matplotlib.pyplot as plt  

import numpy as np

t = np.linspace(1, 5, 51) 

y = np.cos(t**2)/t

plt.plot(t, y, label='cos(t)/t', color = "red", linewidth = 5)

plt.title('My plot', fontsize=15)   # назва графіка 

plt.xlabel('t', fontsize=12, color='blue') # позначення вісі абсцис
plt.ylabel('y', fontsize=12, color='blue') # позначення вісі ординат  
plt.legend()
plt.grid(True)