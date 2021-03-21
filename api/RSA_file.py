p = 53
q = 59

def bin_pow(a,b,M):
    if(b==0):
        return 1
    if(b==1):
        return a%M
    if(b%2==0):
        return ((bin_pow(a,b//2,M)%M)*(bin_pow(a,b//2,M)%M))%M
    return ((((bin_pow(a,b//2,M)%M)*(bin_pow(a,b//2,M)%M))%M)*(a%M))%M

N = p*q

e = 3

message = str(input("Enter a text?"))
print("Text before encryption: {}", format(message))


encrypted_array = []
for x in message:
    ascii_val = ord(x)
    encrypted_array.append(bin_pow(ascii_val,e,N))
    
print(encrypted_array)
    
d = 2011
decrypted_array = []
for x in encrypted_array:
    decrypted_array.append(bin_pow(x,d,N))
    
print(decrypted_array)
message_decrypted = ""
for x in decrypted_array:
    message_decrypted += str(chr(x))

print("Decrypted Message: {}",message_decrypted)

