import math
def isPrime():
    prime=[]
    for i in range(100,201):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            prime.append(i)
    return len(prime),prime
n,prime=isPrime()
print(n,prime)