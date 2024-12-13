# Effect of sample size on confidence interval
import matplotlib.pyplot as plt
import numpy as np
import random

# 95% confidence interval functions
def upper95(n, mu, std):
    return mu + 1.96 * (std / np.sqrt(n))

def lower95(n, mu, std):
    return mu - 1.96 * (std / np.sqrt(n))

# 99% confidence interval functions
def upper99(n, mu, std):
    return mu + 2.58 * (std / np.sqrt(n))

def lower99(n, mu, std):
    return mu - 2.58 * (std / np.sqrt(n))


# Needs to graph:
# - sample mean based on sample size n
# - population mean mu
# - 95% confidence
# - 99% confidence

def plot_graph(N, mu_grams, std_grams, n):
    # 95% confidence interval
    X_list = []
    upper_list = []
    lower_list = []

    bearings = np.random.normal(mu_grams, std_grams, N)
    for i in range(1, n+1):
        X = bearings[random.sample(range(N), i)]
        X_bar = np.mean(X)
        X_list.append(X_bar)
        f1 = upper95(i, mu_grams, std_grams)
        f2 = lower95(i, mu_grams, std_grams)
        upper_list.append(f1)
        lower_list.append(f2)

    b = list(range(1, n+1))
    plt.scatter(b, X_list, color = 'b', marker = 'x', label = 'Sample Mean (xbar)')
    plt.title('Sample Mean (xbar) vs Sample Size (n)')
    x_label = 'Sample Size (n)'
    y_label = 'Sample Mean (xbar)'
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(upper_list, 'r-', label='95% Confidence')
    plt.plot(lower_list, 'r-')

    # 99% confidence interval
    X_list = []
    upper_list = []
    lower_list = []

    bearings = np.random.normal(mu_grams, std_grams, N)
    for i in range(1, n+1):
        X = bearings[random.sample(range(N), i)]
        X_bar = np.mean(X)
        X_list.append(X_bar)
        f1 = upper99(i, mu_grams, std_grams)
        f2 = lower99(i, mu_grams, std_grams)
        upper_list.append(f1)
        lower_list.append(f2)

    b = list(range(1, n+1))
    plt.scatter(b, X_list, color = 'b', marker = 'x')
    plt.title('Sample Mean (xbar) vs Sample Size (n)')
    x_label = 'Sample Size (n)'
    y_label = 'Sample Mean (xbar)'
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(upper_list, 'r--', label='99% Confidence')
    plt.plot(lower_list, 'r--')

    # Plot Population Mean
    plt.plot(b, [mu_grams]*n, 'k-', label='Popluation Mean')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    # total num of bearings
    N = 1000000

    # population mean in grams
    mu_grams = 50

    # standard deviation in grams
    std_grams = 3

    # sample size from range 1 - 200
    n = 200

    plot_graph(N, mu_grams, std_grams, n)
