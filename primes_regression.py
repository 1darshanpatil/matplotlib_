from sympy import isprime
from scipy import stats
def count_primes(x):
    return len([i for i in range(x+1) if isprime(i)])
print("The code gives you a scatter plot of number of primes less than or equal to N")
N = int(input("Enter any positive integer: "))
x = [i for i in range(1, N+1) if isprime(i)]
y = [count_primes(i) for  i in x]
m, c, r, p, std_err = stats.linregress(x, y)

Y = list(map(lambda y: m*y+c, x))
plt.scatter(x, y)
plt.plot(x, Y)
plt.title("The scatter plot of number primes")
plt.ylabel('Primes less than N')
plt.xlabel('N')
plt.show()
