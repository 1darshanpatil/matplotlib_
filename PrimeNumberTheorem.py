import numpy as np
from math import *
from sympy import isprime
import matplotlib.pyplot as plt
def pr(x):
    return len(np.array([i for i in range(1, x+1) if isprime(i)]))
def cal(x):
    if x==1:
        return 0
    return floor(x/log(x))
print('The program compares the graphs of actual number of prime and primes by prime number')
N = int(input("Enter any positive integer: "))
X = range(1, N+1)
Y_actual, Y_cal = np.array([pr(i) for i in range(1, N+1)]), np.array([cal(j) for j in range(1, N+1)])
plt.plot(X, Y_actual, label = 'Actual #primes')
plt.plot(X, Y_cal, label = 'Prime #theorem')
plt.xlabel('Value of N')
plt.ylabel('Number of primes less than N')
plt.title('Comapring the prime number theorem')
plt.legend()
plt.show()
print(Y_actual)
