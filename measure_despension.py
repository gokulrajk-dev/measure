import statistics as s
def stat(d):
    variance = s.variance(d)
    sd = s.stdev(d)
    return variance,sd
d = [1,2,3,4,5,5,6,6,7,8,9,10]
variance, sd=stat(d)
print("variance :",variance)
print("standard deviation :",sd)
