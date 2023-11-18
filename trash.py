import math

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import cont2discrete, lti, dstep

from Pure import ax, fig

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
den_s = [0.001605, 1]
sys_s = signal.TransferFunction(num_s, den_s)
t, y = signal.step(sys_s)

num_z = [b1, b2]
den_z = [1, a1, a2]

A = np.array([[0, 1], [-10., -3]])
B = np.array([[0], [10.]])
C = np.array([[1., 0]])
D = np.array([[0.]])
l_system = lti(A, B, C, D)

t, x = l_system.step(T=np.linspace(0, 5, 100))
fig, ax = plt.subplots()
ax.plot(t, x, label='Continuous', linewidth=3)
dt = 0.1
for method in ['zoh']:
    d_system = cont2discrete((A, B, C, D), dt, method=method)
    s, x_d = dstep(d_system)
    ax.step(s, np.squeeze(x_d), label=method, where='post')
ax.axis([t[0], t[-1], x[0], 1.4])
ax.legend(loc='best')
fig.tight_layout()
plt.show()
