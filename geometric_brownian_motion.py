"""
@title: Geometric Brownian Motion
@date: 15/02/2018
@author: Hayden Hohns
@brief: A simulation of geometric Brownian motion. See page 197 of the
"Handbook of Monte Carlo Methods".
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Initialise values and variables

t0 = 0.0
T = 1.0 # final time
n = 10000 # number of steps
h = T / (n - 1) # step size
t = np.arange(t0, T, h)

# 2. Set parameters

mu = 1
sigma = 0.2
x0 = 1
W = np.empty([n, 1])
x = np.empty([n, 1])
tt = np.empty([n, 1])

# 3. Main Loop

gaussRV = 0
for i in range(0, n):
    W[i - 1] = np.sqrt(h) * gaussRV
    x[i - 1] = x0 * np.exp((mu - sigma * sigma / 2) * t[i - 1] 
            + sigma * W[i - 1])
    tt[i - 1] = t[i - 1]
    gaussRV = gaussRV + np.random.normal()

# 4. Plotting

f = plt.figure()
plt.plot(tt, x)
plt.xlabel('t')
plt.ylabel('X_t')
plt.title('Geometric Brownian Motion')
