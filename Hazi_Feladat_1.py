import math as mt
import cmath as cmt
from datetime import date

def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

def feladat_2():
    a=int(input("elso szam: "))
    b=int(input("masodik szam: "))
    c=int(input("harmadik szam: "))
    ls=[a,b,c]
    for i in ls:
        if i>min(ls) and i<max(ls):
            print(max(ls),i ,min(ls))

def feladat_3(x):
    if x>-2 and x<0:
        x=2*x
        print(x)
    elif x>=0 and x<2:
        x=x*x
        print(x)
    elif x>2:
        x=10
        print(x)
    else:
        print("Nem esik bele egyik tartományba sem!")

def feladat_4(a,b,c):
    ls=[a,b,c]
    als=[abs(a),abs(b),abs(c)]
    print(min(ls) ,max(als))

def feladat_5(a,b,c,d):
    print(a,b,c,d)
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

def feladat_6(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        p=(a+b+c)/2
        T=mt.sqrt(p*(p-a)*(p-b)*(p-c))
        R=(a*b*c)/(4*T)
        r=T/p
        print(" R= %.2f és r= %.2f" %(R,r))
    else:
        print("Nem képezhetik!")

def feladat_7(a,b,drot):
    K=2*(a+b)
    if K>drot:
        print("Szükség van még ",K-drot,"drótra.")
    elif drot>K:
        print("Maradt még", drot-K," drót.")
    else:
        print("Megfelelő mennyiségű a drót.")

def feladat_8():
    x=int(input("Adj meg egy számot: "))
    if x<5:
        x=3*x-5
    elif x>=5 and x<=10:
        x=10
    else:
        x=9*x+1
    print("f függvény értéke: ",x)

    a=int(input("Adj meg egy számot: "))
    b=int(input("Adj meg egy számot: "))
    c=int(input("Adj meg egy számot: "))
    d=int(input("Adj meg egy számot: "))
    y=0
    if a+c>2*d and b>0:
        y=d-3*b
    elif a+c<2*d and b<0:
        y=d+3*b
    else:
        y=4
    print("Az E függvény eredménye: ", y)

def feladat_9(a,b,c):
    a= input("Kérem a másodfokú tagot: ")
    a = float(a)
    while a == 0:
        print("Ez nem lesz másodfokú egyenlet; nem oldom meg.")
        a = input("Kérem a másodfokú tagot: '")
        a = float(a)

    b = input("Kérem az elsőfokú tagot: ")
    c = input("Kérem a konstans tagot: ")
    b = float(b)
    c = float(c)

    d = b * b - 4 * a * c

    if d >= 0:
        print("Van valós megoldás.")
        x1 = (-b - mt.sqrt(d)) / (2 * a)
        x2 = (-b + mt.sqrt(d)) / (2 * a)
        print("Az egyik megoldás", x1)
        print("A másik megoldás", x2)
    else:
        print("Nincs valós megoldás.")
        x1 = (-b - cmt.sqrt(d)) / (2 * a)
        x2 = (-b + cmt.sqrt(d)) / (2 * a)
        print("Az egyik megoldás", x1)
        print("A másik megoldás", x2)

def feladat_10(a,b):
    x=0
    for i in range(a,b+1):
        if i%4==0 and i%100!=0 or i%400==0:
            x+=1
    print(x)

def feladat_11():
    a=date(input("Mikor születtél? "))
    most=date.today()
    x=most-a
    print(x)

def feladat_12(adottpont,maxpont):
    if adottpont>maxpont*0.6:
        print("Sikeres vizsga!")
    else:
        print("Bukás!")

def feladat_13():
    a=int(input("Jegyed?"))
    if a==5:
        print("Jeles!")
    elif a==4:
        print("Jó!")
    elif a==3:
        print("Közepes!")
    elif a==2:
        print("Eléséges!")
    elif a==1:
        print("Elégtelen")
    else:
        print("Nincs ilyen érdemjegy!")

def feladat_14():
    a=int(input("Hanyadik hónapot keresed? "))
    honapok=["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
    for i in range(12):
        if i==a:
            print(honapok[i-1])

def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados+=1
        a=a-b
    print (hanyados)

def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    print(a)

def feladat_17(n):
    masolat = n
    uj_szam = 0
    while n != 0:
        szj = n % 10
        uj_szam = uj_szam * 10 + szj
        n = n // 10
    return(uj_szam==masolat)

def feladat_18():
    x=int(input("Szám x: "))
    y=int(input("Szám y: "))
    f=[]
    d=[]
    szorzat=0
    while True:
        f.append(x)
        d.append(y)
        x = x // 2
        y=y*2
        if x<1:
            break
    for i in range(len(f)):
        if f[i]%2==1:
            szorzat+=d[i]

    print(szorzat)

def feladat_19(n):
    prim = True
    if n == 1:
        prim = False
    for i in range(2, int(mt.sqrt(n)) + 1):
        if n % i == 0:
            prim = False
            break
    return prim

def feladat_20(n):
    a = 1
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        c = a + b
        print(a, b, c, end=" ")
        k = 3
        while k < n:
            a = b
            b = c
            c = a + b
            print(c, end=" ")
            k += 1

def feladat_21(n):
    masolat = n
    uj_szam = 0
    while n != 0:
        szj = n % 10
        uj_szam = uj_szam * 10 + szj
        n = n // 10
    print(uj_szam)

def feladat_22(x,n):

    eredmeny=1
    while n>0:
        if n%2==1:
            eredmeny=eredmeny*x
            n=n-1
        else:
            x=x*x
            n=n/2
    print( eredmeny)
    '''vagy így:
    alap=x
    for i in range(n-1):
        x=x*alap
    print (x)'''

def feladat_23(n):

    for i in range(1,n+1):
        a=[]
        for j in range(i):
            if j==0:
                continue
            if i%j==0:
                a.append(j)
        c=0
        for o in range(len(a)):
            c+=a[o]
        if i==c:
            print(i)
            print(a)

def feladat_24():
    x=1
    het=0
    tihá=0
    while x!=0:
        x=int(input("Szám: "))
        if x%7==5:
            het+=1
        if x%13==7:
            tihá+=1
    print("Héttel osztva maradékul ötöt ad: {} szám, Tizenhárommal osztva maradékul hetet ad: {} szám".format(het,tihá))

def feladat_25():
    


def main():
    #feladat_1(20,-9)
    #feladat_2()
    #feladat_3(20)
    #feladat_4(32,22,-11)
    #feladat_5(12,23,33,-1)
    #feladat_6(5,3,6)
    #feladat_7(12,23,100)
    #feladat_8()
    #feladat_9(1,2,4)
    #feladat_10(1010,2018)
    #feladat_11(???)
    #feladat_12(61,100)
    #feladat_13()
    #feladat_14()
    #feladat_15(200,2)
    #feladat_16(350,40)
    #print(feladat_17(11211))
    #feladat_18()
    #print(feladat_19(13))
    #feladat_20(10)
    #feladat_21(2333212)
    #feladat_22(2,10)
    #feladat_23(10000)
    #feladat_24()
    feladat_25()

main()
