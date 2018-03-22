import numpy as np
def fel_1():
    n=int(input("Ennyi db számot kérek: "))
    tomb=[]
    for i in range(n):
        x=int(input("szam: "))
        tomb.append(x)
    for j in range(n-1):
        for k in range(j+1,n):
            if tomb[j]==tomb[k]:
                print(j,k)
            break

def fel_2():
    n=int(input("Darab számot kérek: "))
    paros=0
    paratlan=0
    for i in range(n):
        x=int(input("szam: "))
        if x%2==1:
            paratlan+=1
        else:
            paros+=1
    print(paros,"/",paratlan," paros/paratlan arány")

def fel_3():
    n = int(input("Darab számot kérek: "))
    tomb = []
    for i in range(n):
        x = int(input("szam: "))
        tomb.append(x)
    sum=0
    for j in range(n):
        sum+=abs(tomb[j])
    return sum/n

def fel_4():
    n = int(input("Darab számot kérek: "))
    szorzat=1
    szka=0
    db=0
    for i in range(n):
        x = int(input("szam: "))
        if x>0:
            szorzat*=x
        if x<0:
            szka+=x
            db+=1
    print("Szigoruan p+ számok szorzata: {}, negativ számok szamtani közepe: {}".format(szorzat,szka/db))

def fel_5():
    n = int(input("Darab számot kérek: "))
    szorzat = 1
    osszeg = 0
    tomb=[]
    for i in range(n):
        y = int(input("szam: "))
        tomb.append(y)
    for x in tomb:
        if x < 7:
            szorzat *= x
        if x > 10:
          osszeg += x
    print("7nél kisseb szamok szorzata: {}, 10 nél nagyobbak összege: {}".format(szorzat,osszeg))

def fel_6():
    n = int(input("Darab számot kérek: "))
    x=0
    z=0
    for i in range(n):
        y = int(input("szam: "))
        if y==0:
            break
        if i>1:
            if x+z==y:
                print (y)
        if i%2==0:
            x=y
        if i%2==1:
            z=y

def fel_7():
    n = int(input("Darab számot kérek: "))
    t=[]
    for i in range(n):
        y = int(input("szam: "))
        if y==0:
            break
        t.append(y)

    max=0
    hely=[]
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if t[i]+t[j]+t[k]>max:
                    max=t[i]+t[j]+t[k]
                    hely=[t[i],t[j],t[k]]
    print(hely,"összege a maximális")

def fel_8(tomb,n):
    for i in range(n-1):
        for j in range(i+1,n):

            if tomb[i]<=tomb[j]:
                break
            else:
                return "Nincs növekvőbe rendezve"
    return "jól van rendezve,növekszik"

def lnko(m,n):
    maradek=m%n
    if maradek==0:
        return n
    else:
        return lnko(n,maradek)

def fel_9(tomb,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if lnko(tomb[i],tomb[j])!=1 :
                return 0
    return 1

def oszt_szam(x):
    db=1
    for i in range(1,x):
        if x%i==0:
            db+=1
    return db

def fel_10(tomb,k):
    pt=[]
    for i in range(len(tomb)-1):
        for j in range(i+1,len(tomb)):
            if oszt_szam(tomb[i])>oszt_szam(tomb[j]):
                tmp=tomb[i]
                tomb[i]=tomb[j]
                tomb[j]=tmp
    #for j in tomb:
    #    pt.append(oszt_szam(j))
    #print (pt)
    #print(tomb)'''
    ah=0
    fh=len(tomb)-1
    while ah<=fh:
        x=(ah+fh)//2
        if oszt_szam(tomb[x])>k:
            return x
        else:
            ah=x+1
    return -1

def main():
    #fel_1()
    #fel_2()
    #print(fel_3())
    #fel_4()
    #fel_5()
    #fel_6()
    #fel_7()
    double=np.array([1,2,3,4,5,6,6,7,8,9])
    #print(fel_8(double,10))
    rel=np.array([2,3,5,8,11,13,17,19])
    #print(fel_9(rel,8))
    nt=np.array([5,34,2,32,4,3,14,6,16,23,10])
    print(fel_10(nt,5))


main()