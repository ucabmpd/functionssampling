import matplotlib.pyplot as plt
import numpy as np

def drawRandomNumbers(args):
    numbersamples = args[0]
    distribution = args[1]
    if (distribution == 'Normal'):
        if (len(args) != 4):
            mu = 0
            sigma = 1
        else:
            mu = args[2]
            sigma = args[3]
        x = np.random.normal(mu, sigma, size=numbersamples)
    if (distribution == 'Poisson'):
        lam = args[2]
        x = np.random.poisson(lam, size=numbersamples)
    if (distribution == 'Binomial'):
        n = args[2]
        p = args[3]
        x = np.random.binomial(n, p, size=numbersamples)
    return (x)

class sample:
    values = []
    numbersamples = 0
    distribution = ""

    def __init__(self, parameters):
        self.numbersamples = parameters[0]
        self.distribution = parameters[1]
        self.values = drawRandomNumbers(parameters)

    def summary(self):
        print("---- SAMPLE SUMMARY -----")
        print("Data Statistics:")
        print("min               = " + str(min(self.values)))
        print("1st quartile      = " + str(np.percentile(self.values, 25)))
        print("mean              = " + str(np.percentile(self.values, 50)))
        print("3rd quartile      = " + str(np.percentile(self.values, 75)))
        print("max               = " + str(max(self.values)))
        print("number of samples = " + str(len(self.values)))

    def plot(self):
        plt.hist(self.values, normed=True, bins=30)
        plt.ylabel('Probability');
        plt.show()

class normalSample(sample):
    mu = 0
    sigma = 1

    def __init__(self, n, parameterMu, parameterSigma):
        parameters = [n, 'Normal', parameterMu, parameterSigma]
        sample.__init__(self, parameters)
        self.mu = parameterMu
        self.sigma = parameterSigma

    def summary(self):
        sample.summary(self)
        print("Original Parameters:")
        print("distribution      = " + self.distribution)
        print("parameter mu      = " + str(self.mu))
        print("parameter sigma   = " + str(self.sigma))
        print("------ END SUMMARY ------")
        print("")

class poissonSample(sample):
    lambd = 1

    def __init__(self, n, parameterLambda):
        sample.__init__(self, [n, 'Poisson', parameterLambda])
        self.lamds = parameterLambda

    def summary(self):
        sample.summary(self)
        print("Original Parameters:")
        print("distribution      = " + str(self.distribution))
        print("parameter lambda  = " + str(self.lambd))
        print("------ END SUMMARY ------")
        print("")

class binomialSample(sample):
    n = 1
    p = 0.5

    def __init__(self, n, parameterN, parameterP):
        sample.__init__(self, [n, 'Binomial', parameterN, parameterP])
        self.n = parameterN
        self.p = parameterP

    def summary(self):
        sample.summary(self)
        print("Original Parameters:")
        print("distribution      = " + str(self.distribution))
        print("parameter n       = " + str(self.n))
        print("parameter p       = " + str(self.p))
        print("------ END SUMMARY ------")
        print("")