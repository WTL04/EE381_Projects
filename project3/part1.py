import random
import matplotlib.pyplot as plt #enables plotting

def dice():
	p = [0.1, 0.2, 0.15, 0.25, 0.3] 
	dice =  list(range(1, 6)) #5-sided die
	roll3 = random.choices(dice, weights=p, k=3)
	
	return roll3[0] == 1 and roll3[1] == 1 and roll3[2] == 1

def bernoulliTrial():
	X = 0 
	for i in range(1000):
		if dice() == True:
			X+=1

	return X #num of successes in 1000 rolls
		
def experiment(N):
	results = []
	for i in range(N):
		results.append(bernoulliTrial())
    
	# Generate histogram to approximate PMF
	max_X = max(results)
	frequency = [results.count(i) for i in range(max_X + 1)]
	probability = [f / N for f in frequency]  # Normalize to get probabilities
    
    # Create stem plot
	plt.stem(range(max_X + 1), probability)
	plt.xlabel("Number of successes in n = 1000 trials")
	plt.ylabel("Probability")
	plt.title("Bernoulli Trials: PMF - Experimental Results")
	plt.show()
	
   
if __name__ == "__main__":
	N = 10000
	experiment(N)
