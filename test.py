import math

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import cont2discrete, dstep

T = 10 ** -4
s = 0  # sec
K = 62.89  # 'motor_gain'
z = math.exp(s * T)
tau = 16.05 * (10 ** -3)
a1 = -(1 + math.exp(-T / tau))
a2 = math.exp(-T / tau)
b1 = K * (T - tau + tau * math.exp(-T / tau))
b2 = K * (tau - (T + tau) * math.exp(-T / tau))
num_s = [62.89]
den_s = [0.0001605, 1]
sys_s = signal.TransferFunction(num_s, den_s)
t, y = signal.step(sys_s)

num_z = [b1, b2]
den_z = [1, a1, a2]
sys_z = signal.TransferFunction(num_z, den_z,dt=T)
fig, ax = plt.subplots()
dt = T
d_system = cont2discrete((num_s, den_s), dt, method='zoh')
print('a1=',a1,'a2=',a2,'b1=',b1,'b2=',b2)
print(d_system,"\n",sys_z)
s, x_d = dstep(d_system)
ax.step(s, np.squeeze(x_d))
#ax.axis=[0,0.0012,0,70]
plt.xlim(0,0.0011)
plt.plot(t, y)
plt.show()
