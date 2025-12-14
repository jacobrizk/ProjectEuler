#Project Euler Q2
#find sum of all even valued numbers in the Fibonacci sequence greater than or equal to 4,000,000 (four million).

#most errors were in placement of statements.

fib = [1,2]
evenFib = []
i = 0
i_2 = 0
maxFib = 4000000
nextFib = 0

#finds fib less than or equal to max.
while True:
    nextFib = fib[i] + fib[i+1]

    if nextFib > maxFib:
        break

    fib.append(nextFib)

    i += 1

#makes new list that finds values in fib that when /2 = 0
for num in fib:
    if num % 2 == 0:
        evenFib.append(num)

#result
print("Final even fib sum:",sum(evenFib))