#Project Euler Q3
#finding the largest prime factor for a given number.

#first a prime number finder

#second find the factors of given that are prime numbers.
#logic of finding prime factors in english:
# - divide given number by lowest to highest prime until remainder = 0.
# - when = 0, save that prime and check if other number is prime.
#   - if yes, save that number also and DONE.
#   - if no, begin divide by next prime number you left off on and repeat until yes or remainder = 0.

primes = []
factors = []
givenNumber = 600851475143
maxPrime = 100000 #not sure how to select max prime for given number.

#prime number finder
for num in range(2,maxPrime + 1):
    if all(num % value != 0 for value in primes): #if the number divided by any previously found prime number not= 0, it's a prime.
        primes.append(num)

#prime factor finder
for prime in primes:
    if givenNumber % prime == 0:
        factors.append(prime)
        givenNumber = givenNumber//prime
        if givenNumber in primes:
            factors.append(givenNumber)
            break

print(max(factors))