import random
import math
import matplotlib.pyplot as plt  # Enables plotting

# Function to simulate rolling three dice and checking for three ones
def dice():
    p = [0.1, 0.2, 0.15, 0.25, 0.3] 
    dice_faces = list(range(1, 6))  # 5-sided die
    roll3 = random.choices(dice_faces, weights=p, k=3)
    
    return roll3[0] == 1 and roll3[1] == 1 and roll3[2] == 1

# Function to perform a Bernoulli trial
def bernoulliTrial():
    X = 0 
    for i in range(1000):
        if dice():
            X += 1
    return X  # Number of successes in 1000 rolls

# Function to calculate the binomial distribution PMF
def binomialDist(n, p, x):
    binom_coeff = math.comb(n, x)  # n choose x
    pdf = binom_coeff * (p ** x) * ((1 - p) ** (n - x))
    return pdf

# Function to perform the experiment and plot PMF
def experiment(N):
    results = []
    for i in range(N):
        results.append(bernoulliTrial())
    
    # Calculate theoretical PMF using the poisson distribution
    p = [0.1, 0.2, 0.15, 0.25, 0.3]
    
    # Probability of rolling three ones
    p_success = (p[0]) ** 3  

    # Maximum number of successes
    max_X = max(results)

    binomial_pmf = [binomialDist(1000, p_success, x) for x in range(max_X + 1)]

    # Plot theoretical PMF
    plt.stem(range(max_X + 1), binomial_pmf)

    # Plot settings
    plt.xlabel("Number of successes in n = 1000 trials")
    plt.ylabel("Probability")
    plt.title("Bernoulli Trials: PMF - Binomial Formula")
    plt.show()

if __name__ == "__main__":
    N = 10000
    experiment(N)
