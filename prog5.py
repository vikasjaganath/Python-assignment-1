def factorial(n) :
    """Return factorial of n using recurison."""
    if not isinstance (n, int):
        raise TypeError("factorial is only defined for integers.")
    if n < 0:
        raise ValueError ("Factorial of negative numbers is not allowed.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if n is a prime number."""
    if not isinstance(n, int):
        raise TypeError ("prime check requires an integer.")
    if n < 0:
        raise ValueError ("Negative numbers cannot be prime")
    if n < 2:
        return False 
    
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
           return False
        return True 
    
    def gcd(a,b):
        """Return GCD of a and b using Eulid's algorithm."""
        if not isintance(a,int) or not isintance(b,int):
            raise TypeError("GCD woeks only with integers.")
        if a<0 or b < 0:
            raise ValueError ("GCD of negative numbers is not allowed.")
        while b != 0:
            a,b = b,a%b
        return a