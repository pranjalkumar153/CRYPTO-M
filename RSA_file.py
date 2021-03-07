PRIMES = []
for i in range(10000):
    PRIMES.append(True)
# print(arr)
PRIMES[0] = False
PRIMES[1] = False

for i in range(10000):
    if PRIMES[i]==True: 
        for j in range(2*i,10000,i):
            PRIMES[j] = False

# for i in range(10000):
#     print(i,PRIMES[i]) 
    
print(PRIMES[0],PRIMES[1], PRIMES[2], PRIMES[3])

## code for mathematical functions

class MATHEMATICAL_ALGORITHMS:
    def POWER(self,A,N,M):
        if(N==0):
            return 1
        if(N==1):
            return A%M
        if(N%2==0):
            return (POWER(A,N//2,M)%M*POWER(A,N//2,M)%M)%M
        return (((POWER(A,N//2,M)%M*POWER(A,N//2,M)%M)%M)*(A%M))%M
    def MODULAR_INVERSE(self,e,N):
        for i in range(N):
            if ((i%N)*(e*N))%N==1:
                return i
    def PRIME_TO_TOTIENT(self,PHI):
        x = -1
        for i in range(min(PHI,10000)):
            if(PRIMES[i]==True):
                x = i
        return x
 
## code for encryption   
    
class ENCRYPTION(MATHEMATICAL_ALGORITHMS):
    # initializing the class
    def __init__(self,username_sender,username_receiver):
        self.sender = username_sender
        self.receiver = username_receiver
        print()
    # calculating the key
    def usernames_pair(self):
        self.__KEY_ONE_SUM = 0
        for x in self.sender:
            self.__KEY_ONE_SUM += ord(x)
        self.__KEY_TWO_SUM = 0
        for x in self.receiver:
            self.__KEY_TWO_SUM += ord(x)
        self.VAR_KEY_ONE = 1
        for i in range(self.__KEY_ONE_SUM):
            if(PRIMES[i]==True):
                self.VAR_KEY_ONE *= i
        self.VAR_KEY_ONE += 1  
        self.VAR_KEY_TWO = 1
        for i in range(self.__KEY_ONE_SUM):
            if(PRIMES[i]==True):
               self.VAR_KEY_TWO *= i
        self.VAR_KEY_TWO += 1
        self.__KEY_ONE = VAR_KEY_ONE
        self.__KEY_TWO = VAR_KEY_TWO
        print(self.VAR_KEY_ONE,self.VAR_KEY_TWO)
    
x = ENCRYPTION("pranjalkumar153","Abhisekh64")
print(x.usernames_pair())