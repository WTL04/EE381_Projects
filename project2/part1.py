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

    p0 = 0.40
    e0 = 0.02
    e1 = 0.015
    fails = 0

    for i in range(N):
        
        m = random.random()
        t = random.random()
        #ensure t != m
        while (m==t):
            t = random.random()

        s = createSignalS(m, p0)
        r = createSignalR(t, s, e0, e1)

        if (r!=s):
            fails+=1

    return fails / N


if __name__ == "__main__":
    N=10000
    print(f"Probability of transmission error: {experiment(N)}")