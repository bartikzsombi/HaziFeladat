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




def main():
    #print(fel_1(8))


main()