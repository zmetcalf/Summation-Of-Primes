import math

counter = 3
primes = 2 # start at two because it was excluded

def CheckPrime(numCheck):
    i = 2
    maxCheck = math.sqrt(numCheck)
    while i <= maxCheck:
        if numCheck % i == 0:
            return 0
        i += 1
    return 1
    
while counter < 2000000:
    if CheckPrime(counter):
        primes = counter + primes
    counter += 2
    
print primes