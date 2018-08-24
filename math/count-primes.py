# Count Primes

# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Sieve of Eratosthenes algorithm

def countPrimes(self, n):
        
    if n <= 2:
        return 0
    
    not_prime = set()
    count = 0
    
    for i in xrange(2, n):
        if i not in not_prime:
            count += 1
            for j in xrange(i*i, n, i):
                not_prime.add(j)
    
    return count