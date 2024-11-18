import random

def createSignalS(m, p0):
    if (m<=p0):
        s = 0
    else:
        s = 1
    return s

def createSignalR(t, s, e0, e1):
    if s==0 and t<=e0:
        r=1
    elif s==0 and t>e0:
        r=0
    elif s==1 and t>=e1:
        r=1
    elif s==1 and t<=e1:
        r=0
    return r

def experiment(N):
    e0 = 0.02
    e1 = 0.015
    successes = 0

    for i in range(N):
        # Always generate signal S = 1
        s = 1
        t = random.random()
        r = createSignalR(t, s, e0, e1)
        if r == s:
            successes += 1

    # Return the conditional probability P(R=1 | S=1)
    return successes / N


if __name__ == "__main__":
    N=100000
    print(f"Conditional Probability P(R=1 | S=1): {experiment(N)}")