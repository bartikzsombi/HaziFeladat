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
    i=0
    y=1
    x=0
    z=0
    while y!=0:
        y = int(input("szam: "))
        if i>1:
            if x+z==y:
                print (y)
        if i%2==0:
            x=y
        if i%2==1:
            z=y
        i+=1

def fel_7():
    y = 1
    t=[]
    n=0
    while y!=0:
        y = int(input("szam: "))
        n+=1
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

def fel_11():
    n=int(input("matrix sorai száma: "))
    m=int(input("matrix oszlopai száma: "))
    matrix=np.zeros((n,m),dtype='int')
    for i in range(n):
        for j in range(m):
            x=int(input("Mátrix egyik eleme: "))
            matrix[i][j]=x
    #print (matrix)
    for j in range(m):
        neg = 0
        nul = 0
        for i in range(n):
            if matrix[i][j]<0:
                neg+=1
            if matrix[i][j]==0:
                nul+=1
        if neg/2>=nul:
            print(j,". oszlopba legalább 2x annyi negativ szám van mint nulla")

def fel_12(matrix,m,n):
    for i in range(m):
        for j in range(n):
            if i+j!=0 and matrix[i][j]%(i+j)==0 :
                print ("{} érték, matrix[{}][{}] helyen".format(matrix[i][j],i,j))
    #print(matrix)

def fel_13(matrix,m,n):
    tomb=np.zeros((m,n))

    for j in range(n):
        kicsi = matrix[0][j]
        for i in range(m):
            if matrix[i][j]<kicsi:
                kicsi=matrix[i][j]
        for i in range(m):
            tomb[i][j]=matrix[i][j]-kicsi
    print(matrix)
    print (tomb)

def fel_14(tomb,n):
    nagy=tomb[n-1][n-1]
    for i in range(n):
        for j in range(n):
            if i+j>n-1:
                if tomb[i][j]>nagy:
                    nagy=tomb[i][j]
    print(nagy)

def fel_15(matrix,n):
    for i in range(n):
        for j in range(n):
            if i==j:
                if matrix[i][j]!=0:
                    return False
    return True

def fel_16(t1,t2,m,n):
    for i in range(m):
        for j in range(n):
            t2[j][i]=t1[i][j]
    print(t1,"\n\n",t2)

def ASCIIszamj6(n,m):
    hat = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or i == n // 2:
                hat[i][j] = 42
            else:
                hat[i][j] = 32
        hat[i][0] = 42
        if i > n // 2:
            hat[i][m - 1] = 42

    for i in range(n):
        for j in range(m):
            print(chr(int(hat[i][j])), end=' ')
        print('\n')

def tankol():
    try:
        fajl=open("tankolas.txt",mode='r')
        rendszam=[]

        for sor in fajl:
            sor=sor.strip().split("/")
            rendszamsor=[]
            rendszamsor.append(sor[0])
            rendszamsor.append(sor[1])
            rendszam.append((rendszamsor))
            #print(rendszamsor)
            d = 0
            for i in rendszamsor[1]:

                if i=="1":
                    d+=1
            rendszamsor.append(d)
        rendszam=sorted(rendszam)

        i=12
        while i>3:
            for c in range(len(rendszam)):
                if rendszam[c][2]==i:
                    print(rendszam[c])
            i-=1

        #print(rendszam)


    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close

def MGHvParatlan():
    abc=np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],dtype='str')
    print("Passz, nem igazán értem a feladatot :/ ")

def bevasarlas():
    x=0
    blokk=[]
    while x!='END':
        x=str(input())
        if x != 'END':
            blokk.append(x)
    sum=0
    for i in range(len(blokk)):
        sum+=float(blokk[i])
    print ("%.2f"%sum)

def main():
    #fel_1()
    #fel_2()
    #print(fel_3())
    #fel_4()
    #fel_5()
    #fel_6()
    #fel_7()
    dou=np.array([1,2,3,4,5,6,6,7,8,9],dtype='double')
    #print(fel_8(dou,10))
    rel=np.array([2,3,5,8,11,13,17,19])
    #print(fel_9(rel,8))
    nt=np.array([5,34,2,32,4,3,14,6,16,23,10])
    #print(fel_10(nt,5))
    #fel_11()
    ma=np.array([[2,1,2,3],[2,2,3,5],[3,3,7,8],[1,3,2,1],[6,4,2,1]])
    #fel_12(ma,5,4)
    #fel_13(ma,5,4)
    tm=np.array([[1,9,4,12],[23,25,28,12],[13,35,38,73],[46,49,94,45]])
    #fel_14(tm,4)
    fonul=np.array([[0,9,4,62],[3,0,28,12],[13,3,0,7],[6,42,4,0]])
    #print(fel_15(fonul,4))

    mszern=np.array([[0,9,10,4,62],[3,30,0,28,12],[13,3,0,19,7],[50,6,42,4,0]],dtype='double')
    nszerm=np.zeros((5,4),dtype='double')
    #fel_16(mszern,nszerm,4,5)
    #esetek = int(input())
    #t=np.zeros(2*esetek,dtype='int')
    '''
    for i in range(0,2*esetek,2):
       sor=input()
       sor=sor.strip()
       sor=sor.split()
       t[i]=int(sor[0])
       t[i+1]=int(sor[1])
    print(t)
    for i in range(0,2*esetek,2):
       ASCIIszamj6(t[i],t[i+1])
    '''
    #tankol()
    #MGHvParatlan()
    bevasarlas()

main()