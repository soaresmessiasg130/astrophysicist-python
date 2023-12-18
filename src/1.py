import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

plt.style.use('dark_background')
plt.rc('font', size=16)

data=pd.read_csv('data/asteroid_data.csv', sep=',')
print(data)

fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111, projection='polar')

# ASTEROIDS
ax.scatter(data['angle[deg]']*np.pi/180, data['dist[AU]'], color='#FF9600', s=16)

# EARTH
theta=np.linspace(0, 2*np.pi, 1000)
r_T=1
ax.plot(theta, np.repeat(r_T,1000), color='blue')

# MARS
gamma=np.linspace(0, 2*np.pi, 1000)
r_M=1.51
ax.plot(gamma, np.repeat(r_M,1000), color='red')

# JUPITER
jupiter=np.linspace(0, 2*np.pi, 1000)
r_J=5.18
ax.plot(jupiter, np.repeat(r_J,1000), color='brown')

# SUN
ax.scatter(0, 0, marker='o', color='yellow', s=100)

plt.show()
