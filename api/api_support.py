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

def generate_keys(username_sender,username_receiver):
    KEY_ONE_COUNT = 0
    for x in username_sender:
        KEY_ONE_COUNT += ord(x)
    KEY_ONE = 1
    for i in range(KEY_ONE_COUNT):
        if(PRIMES[i]==True):
            KEY_ONE *= i
    KEY_ONE += 1
    KEY_TWO_COUNT = 0
    for x in username_receiver:
        KEY_TWO_COUNT += ord(x)
    KEY_TWO = 1
    for i in range(KEY_TWO_COUNT):
        if(PRIMES[i]==True):
            KEY_TWO *= i
    KEY_TWO += 1 
    dictionary = {"p":KEY_ONE,"q":KEY_TWO}
    return jsonify(dictionary)
    