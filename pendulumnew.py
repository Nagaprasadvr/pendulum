import math
import matplotlib.pyplot as plt

l = 10
dt = 0.3
g = 9.8
n = 100
q = 0.09  # damping strength
time = [0.0]*n
time.insert(0,0.0)
omega = [0.0] * n
theta = [0.0] * n
omega.insert(0,0.0)
theta.insert(0,math.pi / 6)
for i in range(0, n):
    omega[i+1] = omega[i] - (g / l * math.sin(theta[i]) * dt + q * omega[i] * dt)
    theta[i+1] = theta[i] + omega[i+1] * dt
    time[i+1] = time[i] + dt

print(omega)
print(theta)
print(time)
plt.plot(time,theta)

plt.show()
#plt.subplot(theta,time)

