import random

def hackerList(m):
    # create a list of m random 4-digit passcodes
    passcodes = [f"{random.randint(0, 9999):04d}" for i in range(m)]
    return passcodes

def userPassword():
    # generate a random 4-digit passcode
    user_passcode = f"{random.randint(0, 9999):04d}"
    return user_passcode

def experiment(N, m):
    passwordList = hackerList(m)
    successes = 0

    for i in range(N):
        user = userPassword()
        if user in passwordList:
            successes+=1
    return successes

if __name__ == "__main__":
    N = 1000
    m = 7000 # 10**4
    successes = experiment(N, m)
    probability = successes/N
    print(f"Number of successes: {successes}")
    print(f"Probability : {probability}")