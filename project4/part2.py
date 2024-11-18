import numpy as np
import matplotlib.pyplot as plt

def experiment(N):
    RV_U =  np.random.uniform(0, 1, N)
    RV_T = (-1/2) * np.log(1-RV_U)
    return RV_T

def histogram(RV_T, bins=50):
    plt.hist(RV_T, bins=bins, density=True, alpha=0.6, color='b', label='Histogram of RV T')

    # theoretical PDF of the exponential distribution
    lambda_ = 2
    x = np.linspace(0, max(RV_T), 1000)
    pdf = lambda_ * np.exp(-lambda_ * x)
    
    # plot the theoretical PDF
    plt.plot(x, pdf, color='red', label='Theoretical PDF')
    
    # add labels and legend
    plt.title("Exponential Distribution of RV T")
    plt.xlabel("RV T")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    N = 10000
    T = experiment(N)
    histogram(T)
