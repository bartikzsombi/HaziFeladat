import math as mt
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


def main():
    #feladat_1(20,-9)
    #feladat_2()
    #feladat_3(20)
    #feladat_4(32,22,-11)
    #feladat_5(12,23,33,-1)
    #feladat_6(5,3,6)
    #feladat_7(12,23,100)
    feladat_8()

main()
