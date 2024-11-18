import numpy as np
import matplotlib.pyplot as plt


def normalDist(mu, sig, z):
    f = np.exp(-(z-mu) ** 2 / (2 * sig ** 2)) / (sig * np.sqrt(2* np.pi))
    return f

if __name__ == "__main__":
    beta = 40  # Mean lifetime of an individual battery
    N = 10_000  # Number of cartons to simulate
    n = 24  # Number of batteries in one carton

    # Create an array to store the lifetime of each carton
    C = np.zeros((N,))

    # Generate lifetimes for each carton (N experiments)
    for T in range(N):
        C[T] = sum(np.random.exponential(beta, n))

    # Plot the histogram of the experimental PDF
    plt.hist(C, bins=50, density=True, alpha=0.6, color='blue', label="Experimental PDF")

    # Calculate mean and standard deviation using CLT
    mu_C = n * beta  # Mean lifetime of a carton
    sigma_C = np.sqrt(n) * beta  # Standard deviation of a carton's lifetime

    # Generate points for the theoretical normal distribution (CLT approximation)
    z = np.linspace(min(C), max(C), 1000)
    normal_pdf = normalDist(mu_C, sigma_C, z)

    # Plot the theoretical normal distribution
    plt.plot(z, normal_pdf, color='red',  linewidth=2, label="Normal Distribution (CLT)")

    plt.title("Lifetime Distribution of a 24-Pack of Batteries")
    plt.xlabel("Lifetime (days)")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

    # Calculate the histogram for experimental PDF again (for CDF calculation)
    hist, bin_edges = np.histogram(C, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2  # Compute bin centers

    # Calculate the CDF using the cumulative sum of the PDF
    cdf = np.cumsum(hist * np.diff(bin_edges))  # CDF as cumulative sum of PDF values

    # Plot the CDF
    plt.hist(C, bins=50, density=True, alpha=0.6, cumulative=True, color='b', label="Experimental CDF")  
    plt.title("CDF of Lifetime of a 24-Pack of Batteries")
    plt.xlabel("Lifetime (days)")
    plt.ylabel("Cumulative Density")
    plt.grid(alpha=0.3)
    plt.show()

    # Calculate the probability that the carton lasts longer than 3 years 
    time_3_years = 1095
    F_1095 = np.interp(time_3_years, bin_centers, cdf)
    prob_3_years = 1 - F_1095  # P(S > 1095)
    print(f"Probability that the carton lasts longer than 3 years: {prob_3_years:.4f}")

    # calculate probability that carton last between 2.0 and 2.5 years
    time_2_years = 730
    time_2_5_years = 912
    F_730 = np.interp(time_2_years, bin_centers, cdf) 
    F_912 = np.interp(time_2_5_years, bin_centers, cdf) 
    prob_between_2_and_2_5_years = F_912 - F_730  # P(730 <= S <= 912)
    print(f"Probability that the carton lasts between 2.0 and 2.5 years: {prob_between_2_and_2_5_years:.4f}")
