from math import *

def fel_1(a):
    szam=a
    db=0
    for i in range(1,a+1):
        if a%i==0:
            db+=1
    if db==4:
        return True
    else:
        return False

def fel_2(n):
    db=0
    i=0
    while db!=n:
        if i==2:
            db+=1
        elif i%2==1:
            xdb=0
            for j in range(1,i+1):
                if i%j==0:
                    xdb+=1
            if xdb==2:
                db+=1
        i+=1
    print(i-1)

def fel_3(x):
    for i in range(x):
        if 2**i  >=x:
            return 2**i



def main():
    #print(fel_1(8))
    # fel_2(5)
    # print(fel_3(513))

main()