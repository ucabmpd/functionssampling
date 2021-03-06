import functionssampling as fs
# This package provides objects that get samples of different distributions

# For Normal distribution: normalSample(n,mu,sigma)
# n: number of samples  (mu, sigma): parameters of Normal distribution
# example: 
x = fs.normalSample(1000,5,0.1)

# For Poisson distribution: poissonSample(n, lambda)
# n: number of samples  lambda: parameter of Poisson distribution
# example: 
y = fs.poissonSample(1000,4)

# For Binomial distribution: binomialSample(n, N, P)
# n: number of samples  (N, P): parameters of Binomial distribution
# example: 
z = fs.binomialSample(1000,100,0.1)

# To get the summary of the different objects:
x.summary()
y.summary()
z.summary()

# To plot histograms of the different samples:
x.plot()
y.plot()
z.plot()
z.plot()
