from flask import jsonify

PRIMES = []
for i in range(100000):
    PRIMES.append(True)
PRIMES[0]=False
PRIMES[1]=False

for i in range(100000):
    if(PRIMES[i]==True):
        for j in range(2*i,100000,i):
            PRIMES[j] = False

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x



def generate_keys(username_sender,username_receiver):
    KEY_ONE = 809
    KEY_TWO = 811
    index = 941
    dictionary = {"p":KEY_ONE,"q":KEY_TWO,"e":index}
    return dictionary





def bin_pow(a,b,M):
    if(b==0):
        return 1
    if(b==1):
        return a%M
    if(b%2==0):
        return ((bin_pow(a,b//2,M)%M)*(bin_pow(a,b//2,M)%M))%M
    return ((((bin_pow(a,b//2,M)%M)*(bin_pow(a,b//2,M)%M))%M)*(a%M))%M
