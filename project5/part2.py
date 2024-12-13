# Using the sample mean to estimate the population mean
import numpy as np
import random

N = 1000000 
mu_grams = 50
std_grams = 3

# 95% confidence interval functions
def upper95(X_bar, S, n):
        return X_bar + 1.96 * (S / np.sqrt(n))

def lower95(X_bar, S, n):
        return X_bar - 1.96 * (S / np.sqrt(n))

# 99% confidence interval functions
def upper99(X_bar, S, n):
        return X_bar + 2.58 * (S / np.sqrt(n))  

def lower99(X_bar, S, n):
        return X_bar - 2.58 * (S / np.sqrt(n))

def n_dist(n):
    n95_success = 0
    n99_success = 0
    M = 10000
    bearings = np.random.normal(mu_grams, std_grams, N)

    for i in range(M):
        X = bearings[random.sample(range(N), n)]
        S = np.std(X, ddof=1)
        X_bar = np.mean(X)
    
        l95 = lower95(X_bar, S, n)
        u95 = upper95(X_bar, S, n)
        l99 = lower99(X_bar, S, n)
        u99 = upper99(X_bar, S, n)

        if mu_grams >= l95 and mu_grams <= u95:
            n95_success += 1
        if mu_grams >= l99 and mu_grams <= u99:
            n99_success += 1

    n95_success = n95_success / M * 100
    n99_success = n99_success / M * 100

    print(f"95% Confidence (Normal Dist) at n = {n}: {n95_success}")
    print(f"99% Confidence (Normal Dist) at n = {n}: {n99_success}")

def t_dist(n):
    t95_success = 0
    t99_success = 0
    M = 10000
    bearings = np.random.normal(mu_grams, std_grams, N)
    for i in range(M):
        # values from student t table
        if n == 5:
            t95 = 2.78
            t99 = 4.60
        elif n == 40:
            t95 = 2.02
            t99 = 2.71
        elif n == 120:
            t95 = 1.98
            t99 = 2.62
        elif n == 200:
            t95 = 1.97
            t99 = 2.60
        else:
            break

        X = bearings[random.sample(range(N), n)]
        S = np.std(X, ddof=1)
        X_bar = np.mean(X)

        l95 = lower95(X_bar, S, n)
        u95 = upper95(X_bar, S, n)
        l99 = lower99(X_bar, S, n)
        u99 = upper99(X_bar, S, n)

        if mu_grams >= l95 and mu_grams <= u95:
            t95_success += 1
        if mu_grams >= l99 and mu_grams <= u99:
            t99_success += 1

    t95_success = t95_success / M * 100
    t99_success = t99_success / M * 100

    print(f"95% Confidence (Student t Dist) at n = {n}: {t95_success}")
    print(f"99% Confidence (Student t Dist) at n = {n}: {t99_success}")


if __name__ == "__main__":
    n_dist(n=5)
    n_dist(n=40)
    n_dist(n=120)
    n_dist(n=200)

    t_dist(n=5)
    t_dist(n=40)
    t_dist(n=120)
    t_dist(n=200)
    
