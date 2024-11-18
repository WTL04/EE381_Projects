import numpy as np
import matplotlib.pyplot as plt

# book thickness W = RV
# RV uniformly distributed between min(a) < RV < max(b)
# a, b is provided
# calculate mean and std of thickness using a and b

a = 1
b = 3
mean = (a+b)/2
std = np.sqrt((b-a)**2/12)

def meanAndStd(a, b, n):
    print(f"Number of Books = {n}")
    print(f"mean = {mean * n}")
    print(f"standard deviation = {std * np.sqrt(n)}")
    print()

def experiment(a, b, N, n):
    # plotting histogram of stacks
    RV_S = np.random.uniform(a, b, (N,n))
    
    stacks = np.sum(RV_S, axis=1)
    plt.hist(stacks, bins=50, density=True, alpha=0.6, color='b', label=f'Histogram of {n} books')

    # plotting normal distribution probability funciton
    theoretical_mean = mean * n
    theoretical_std = std * np.sqrt(n)

    x = np.linspace(min(stacks), max(stacks), 1000)
    y = (1/(theoretical_std * np.sqrt(2 * np.pi))) * np.exp(-((x - theoretical_mean)**2) / (2 * theoretical_std**2))
    plt.plot(x, y, color="red", label = "Normal Distribution Function")

    plt.title(f"Stack Thickness Distribution for {n} Books")
    plt.xlabel("Stack Thickness (cm)")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    N = 10000
    n = [1, 5, 10, 15]

    # finding mean and standard dev for stack of n books
    for i in n: 
        meanAndStd(a, b, i)
        experiment(a, b, N, i)
