import matplotlib.pyplot as plt #enables plotting
import random


#function returning a single side
def nsided_die(p):
    # creating die with n-sides
    dice =  list(range(1, len(p)+1))

    #adjusting probability of randint, k = # of choices, k = # of rolls
    result = random.choices(dice, weights=p, k=1)
    return result


if __name__ == "__main__":
    # probabilities per dice side 
    p = [0.2, 0.05, 0.1, 0.25, 0.30, 0.1]
    N = 1000

    result = []

    for i in range(N):
        result += nsided_die(p)

    #finding frequency of each side after rolling n times,
    frequency = [result.count(i) for i in range(1, len(p) + 1)]


    #plotting results on stem plot
    plt.stem(range(1,len(p)+1), frequency)
    plt.xlabel("Face of the Die")
    plt.ylabel("Frequency")
    plt.title("Stem Plot of Die Rolls")
    plt.grid(True)
    plt.show()

