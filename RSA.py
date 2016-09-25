#### Key Generation ######
##Public key##
import rabinMiller
from rabinMiller import generateLargePrime, isPrime

formatarray = []
dectostring = []
encryptstring = []



# Using rabinMiller to help generate large prime numbers
p = generateLargePrime() 
q = generateLargePrime()
n = p * q


z = (p - 1) * (q - 1)

# e is set to 65537 because it is one of the highest fermat numbers 
e = 65537


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0


def mulinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n



g, x, t = xgcd(e, z)
print ("GCD : ", g)
# mv = mulinv (e, z)
d =  mulinv (e, z)
print ("Private Key: ", d)



# Get input from user
text = input(' > ')
# convert the text to decimal
for x in text:
        P = ord(x)

        # Encrypt the decimals
        E = (P ** e) % n
       
        # Decrypt the decimals
        plain = (E ** d) % n

        # add the decrypted string to list for concatenation later on
        formatarray.append(plain)

        # Due to encrypting each character at a time, this concatenates the encrypted value
        encryptstring.append(str(E))
encryptedstring = (''.join(encryptstring))
print (encryptedstring)


# Convert decimals back to their character equivilant while adding to list
for x in formatarray:
    dectostring.append(chr(x))
    # format the string correctly
    justformatting = (''.join(dectostring))
print (justformatting)
