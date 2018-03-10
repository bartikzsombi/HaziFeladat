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

def fel_4():
    for i in range(100,1000):
        lst=[]
        for j in str(i):
            lst.append(j)
        a=lst[0]
        b=lst[1]
        c=lst[2]
        #print(lst)

        if a!=b and a!=c and b!=c:
            print (i)

def fel_5(n):
    lst=[]
    for i in range(1,n+1):
        db=0
        for j in range(1,i+1):
            if i%j==0:
                db+=1
        lst.append(db)
    #print(lst)
    legN =0
    hanyadik=0
    for x in lst:
        hanyadik+=1
        if x>legN:
            legN=x
            #print(legN)
            print(hanyadik)

def fel_6():
    a=input("szam1: ")
    b=input("szam2: ")
    lst=[]
    lstA=[]
    lstB=[]
    for i in range(len(a)):
        lstA.append(a[i])
    for j in range(len(b)):
        lstB.append(b[j])
    db=0
    for x in lstA:
        for y in lstB:
            if x==y:
                lst.append(x)
                break
    szamj = [0,1,2,3,4,5,6,7,8,9]
    for k in szamj:
        for l in lst:
            if int(l)==int(k) :
                db+=1
                break
    if db>1:
        print("eszek a számok rokonok")

def fel_7():
    a = input("szam1: ")
    b = input("szam2: ")
    lst = []
    lstA = []
    lstB = []
    for i in range(len(a)):
        lstA.append(a[i])
    for j in range(len(b)):
        lstB.append(b[j])
    db = 0
    for x in lstA:
        for y in lstB:
            if x == y:
                lst.append(x)
                break
    szamj = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in szamj:
        for l in lst:
            if int(l) == int(k):
                db += 1
                break
    print("szam1: {}, szam2:{}".format(lstA,lstB))
    if db > 0:
        print("eszek a számok barátok")

def fel_8(n):
    db=0
    osszeg=0
    for i in range(1,n):
        osszeg+=i
        db+=1
        if osszeg>=n:
            print(db)
            break

def fel_9():
    paszuj=1
    perc=0
    i=2
    while paszuj!=300:
        paszuj+=paszuj/i
        i+=1
        perc+=1
    print(perc)

def konverzio(n,p,x): #(szám,számrendszer,hatvány)
    if n==0:
        return 0
    else:
        x+=1
        print((p**x)*(n%10))
        return konverzio(n//10,p,x) +(p**x)*(n%10)

def main():
    # print(fel_1(8))
    # fel_2(5)
    # print(fel_3(513))
    #fel_4()
    #fel_5(15)
    #fel_6()
    #fel_7()
    #fel_8(100)
    #fel_9()
    print(konverzio(1101, 2, -1))


main()