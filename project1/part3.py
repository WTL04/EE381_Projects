import numpy as np

def coinToss(N=100000, n=1000):

    # creating matrix with column = coin toss result, row = experiment of 1000 flips
    tosses = np.random.randint(0, 2, (N, n))

    # counts how many heads (1) for each experiment
    headCount = np.sum(tosses, axis=1)

    #counts how many times an exmperiment has 500 heads
    success = np.sum(headCount == 500)

    return success

if __name__ == "__main__":
    success = coinToss()
    probability = success/100000
    print(f"Number of successes: {success}")
    print(f"Probability : {probability}")