import matplotlib.pyplot as plt
import numpy as np
a0=30
a1=0
a2=10
a3=(-2/27)*30

t=3

theta=a1+a2*(t**2)+a3*(t**3)
print(theta)
theta_d=2*a2*t+3*a3*(t**2)
theta_2d=2*a2+6*a3*t

theta_list=[]
theta_d_list=[]
theta_2d_list=[]

for i in np.arange(0,t,0.1):
    theta_list.append(a1+a2*(i**2)+a3*(i**3))
    theta_d_list.append(2*a2*i+3*a3*(i**2))
    theta_2d_list.append(2 * a2 + 6 * a3 * i)

ax1=plt.subplot(3,1,1)
plt.plot(theta_list)
plt.title("Position")
plt.ylabel("Degree")
plt.xticks(visible=False)

plt.subplot(3,1,2,sharex=ax1)
plt.plot(theta_d_list)
plt.title("Velocity")
plt.ylabel("deg/sec")
plt.xticks(visible=False)

plt.subplot(3,1,3,sharex=ax1)
plt.plot(theta_2d_list)
plt.title("Acceleration")
plt.ylabel(r"deg/sec$^2$")
plt.xlabel("Time(seconds)")

plt.show()