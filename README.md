## functionssampling
## This package provides objects that get samples of different distributions
## Author: M. De Luca
## Date  : 04/02/2018
## Ver.  : 01

## For Normal distribution: normalSample(n,mu,sigma)
## n: number of samples  (mu, sigma): parameters of Normal distribution
## example: 
#  x = normalSample(1000,5,0.1)

## For Poisson distribution: poissonSample(n, lambda)
## n: number of samples  lambda: parameter of Poisson distribution
## example: 
#  y = poissonSample(1000,4)

## For Binomial distribution: binomialSample(n, N, P)
## n: number of samples  (N, P): parameters of Binomial distribution
## example: 
#  z = binomialSample(1000,100,0.1)

## To get the summary of the different objects:
#  x.summary()
#  y.summary()
#  z.summary()

## To plot histograms of the different samples:
#  x.plot()
#  y.plot()
#  z.plot()