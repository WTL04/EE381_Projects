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

def majorityVote(r1, r2, r3):
    if (r1+r2+r3) >=2:
        return 1
    else:
        return 0

def experiment(N):
    p0 = 0.40
    e0 = 0.02
    e1 = 0.015
    fails = 0

    for i in range(N):
        m = random.random()
        s = createSignalS(m, p0)

        # transmit the same bit S three times into R1, R2, R3
        t1, t2, t3 = random.random(), random.random(), random.random()
        r1 = createSignalR(t1, s, e0, e1)
        r2 = createSignalR(t2, s, e0, e1)
        r3 = createSignalR(t3, s, e0, e1)

        # calculating if D = 1 or D = 0 via majority rule
        d = majorityVote(r1, r2, r3)

        if d != s:
            fails+=1
            
    return fails/N



if __name__ == "__main__":
    N=10000
    print(f"Probability of error with enhanced transmission: {experiment(N)}")