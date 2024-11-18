import matplotlib.pyplot as plt #enables plotting
import random

# fair die
def fairDie():
    result = random.randint(1, 6)
    return result


def experiment():
    
    #holds number of rolls it takes for a success
    rolls = 0

    while True:
        die1 = fairDie()
        die2 = fairDie()
        rolls+=1

        #add number of rolls to success, reset rolls
        if (die1 + die2 == 2 or die1 + die2 == 10):
            return rolls


if __name__ == "__main__":

    successes = []

    N = 100000

    for i in range(0, N):
        successes.append(experiment())
    
    maxRolls = max(successes)
    # frequency = [successes.count(i) for i in range(1, maxRolls + 1)]

    probability = [successes.count(i)/N for i in range(1, maxRolls + 1)]

    # #plotting results on stem plot
    plt.figure(figsize=(10, 6))
    plt.stem(range(1, maxRolls+1), probability)
    plt.xlabel("Number of Rolls")
    plt.ylabel("Probability")
    plt.title('Stem Plot of Rolls Until Success (Sum of 2 or 10)')
    plt.grid(True)
    plt.show()



