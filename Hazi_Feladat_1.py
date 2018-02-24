import math as mt
import cmath as cmt

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
    a=input("Mikor születtél? ")
    most=input("Hanyadika van ma? ")
    q=a.split(".")
    w=most.split(".")
    x=0
    for i in range(int(q[0]),int(w[0])+1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            napok = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for i in range(len(napok)):
                x += napok[i]
        else:
            napok=[31,28,31,30,31,30,31,31,30,31,30,31]
            for i in range(len(napok)):
                x += napok[i]
    sz=int(q[2])
    for j in range(int(q[1])-1):
        if int(q[0]) % 4 == 0 and int(q[0]) % 100 != 0 or int(q[0]) % 400 == 0:
            napok = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            sz += napok[j]
        else:
            napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            sz += napok[j]
    mo=int(w[2])*-1
    for k in range(int(w[1])-1,12):
        if int(w[0]) % 4 == 0 and int(w[0]) % 100 != 0 or int(w[0]) % 400 == 0:
            napok = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mo += napok[k]
        else:
            napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mo += napok[k]
    print(x-sz-mo," Napot éltem már.")

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
    if len(str(masolat))>9:
        print("Túl hosszú a szám.")
    else:
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
    lakos=int(input("Lakosok száma: "))
    terulet=int(input("Ország területe: "))
    print(lakos/terulet," fő/km2 az ország népsűrűsége.")
    if lakos/terulet<50:
        print("Az ország ritkán lakott.")
    elif lakos/terulet>=50 and lakos/terulet<300:
        print(" Átlagos népsűrűségű ország.")
    else:
        print(" Sűrűn lakott ország.")

def feladat_26():
    x=int(input(" Adj meg egy számot: "))
    pozitív=0
    negatív=0
    if x<0:
        negatív+=1
    else:
        pozitív+=1
    összeg=x
    while összeg!=0:
        x=int(input("Add meg a következő számot: "))
        if x < 0:
            negatív += 1
        else:
            pozitív += 1
        összeg += x
        print(összeg," Eddig a kapott számok összege.")
    print("Negatív számok: {}, Pozitív számok: {}".format(negatív,pozitív))

def feladat_27():
    x=int(input("Adj meg egy számot: "))
    n=0
    p=0
    while True:
        if x<0:
            n += 1
            x = int(input("Adj még számot: "))
            if x<0:
                n += 1
                break
        else:
            p += 1
            x = int(input("Adj még számot: "))
            if x>0:
                p += 1
                break
    print("Negatív számok: {}, Pozitív számok: {}".format(n, p))

def feladat_28(n):
    legn=0
    for i in range(n+1):
        if mt.sqrt(i)%1==0:
            legn=i
    print(legn," Az n-nél kisebb legnagyobb negyzetszám.")

def feladat_29(n):
    o=1
    if n>0 and n<12:
        for i in range(1,n+1):
            o=o*i
        print(o, " n faktoriális eredménye.")
    else:
        print(" NEm tudom kiszámolni...")

def feladat_30():
    datum=input("Írj egy dátumot: ")
    x=datum.split(".")
    nap=0
    for j in range(int(x[1]) - 1):
        if (int(x[0]) % 4 == 0 and int(x[0]) % 100 != 0) or int(x[0]) % 400 == 0:
            napok = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            nap += napok[j]
        else:
            napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            nap += napok[j]
    print(nap, " nap telt el az évből.")

def feladat_31(n):
    for i in range(1,n+1):
        if int(n)%i==0:
            print(i,end=" ")

def feladat_32(k):
    n1=int(input("Adj meg egy számot: "))
    n2 = int(input("Adj még egy nagyobb számot: "))
    for i in range(n1,n2+1):
        if i%k==0:
            print(i, " osztható k-val")

def feladat_33(n):
    c=0
    for i in range(1,n+1):
        a=[]

        for j in range(i):
            if j==0:
                continue
            if i%j==0:
                a.append(j)

        if c<len(a):
            c=i
    print(c," a legtöbb osztóval rendelkező szám.")

def feladat_34(x):
    for i in range(x,6,-1):
        if i%2==0:
            for a in range(1,i+1):
                if feladat_19(a):
                    for b in range(1,i+1):
                        if feladat_19(b):
                            if a+b==i:
                                if a<=b:
                                    print (i,"=",a,"+",b)
                                    return

def feladat_35(x):
    for a in range(1,x+1):
        if feladat_19(a):
            for b in range(1,x+1):
                if feladat_19(b):
                    if abs(a-b)==2:
                        if a<=b:
                            print ("(",a,",",b,")")

def feladat_36(n):
    x=0
    a = 1
    b = 1
    if n == 1:
        x=1
        print(x)
    elif n == 2:
        x=2
        print(x)
    else:
        c = a + b
        x=2
        k = 3
        while c < n:

            a = b
            b = c
            c = a + b
            x+=1
            k += 1
        print(x)



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
    #feladat_10(1996,2018)
    #feladat_11()
    #feladat_12(61,100)
    #feladat_13()
    #feladat_14()
    #feladat_15(200,2)
    #feladat_16(350,40)
    #print(feladat_17(11211))
    #feladat_18()
    #print(feladat_19(13))
    #feladat_20(10)
    #feladat_21(233321222)
    #feladat_22(2,10)
    #feladat_23(10000)
    #feladat_24()
    #feladat_25()
    #feladat_26()
    #feladat_27()
    #feladat_28(200)
    #feladat_29(5)
    #feladat_30()
    #feladat_31(100)
    #feladat_32(7)
    #feladat_33(19)
    #feladat_34(100)
    #feladat_35(100)
    feladat_36(10)

main()
