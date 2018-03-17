from math import *
import sys
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

def fel_10():
    try:
        fajl=open("be.txt",mode="r")
        max=0

        for sor in fajl:
            db = 0
            list = sor.split(" ")
            for szo in list:
                if szo[0].isupper():
                    for i in sor:
                        db += 1
                    break
            if max<db:
                max=db
        print (max)
    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close

def fel_11():
    try:
        fajl=open("be.txt",mode="r")
        minls=[]

        for sor in fajl:
            db = 0
            x=sor.split("\n")
            for jel in x:
                if jel[-1] == "?" or jel[-1] == "!" or jel[-1] == ".":
                    for i in sor:
                        db += 1
                    minls.append(db)
                    print(jel[-1],db)
                    break
                break
        print (min(minls))
    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close

def fel_12():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")
        szamok=[]
        for szam in fajl:
            szamok=szam.split(",")
        print(szamok[-1])
        x=0
        for l in szamok:
            x+=1
        for i in range(x-1):
            db=0
            for j in range(i,x):
                if int(szamok[i])!=int(szamok[j]):
                    break
                if int(szamok[i])==int(szamok[j]):
                    db+=1
            if db>=int(szamok[-1]):
                fajlk.write("Tartalmaz")
                break
    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_13():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")
        szamok=[]
        for szam in fajl:
            szamok=szam.split(",")
        print(szamok[-1])
        x=0
        for l in szamok:
            x+=1
        db = 0
        for i in range(x-1):



            if abs(int(szamok[i])-int(szamok[i+1]))>(int(szamok[-1])):
                db+=1

        fajlk.write("{}".format(db))

    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_14():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")
        sorok=[]

        for x in fajl:
            x=x.strip()
            sorok.append(x)
        for b in sorok:
            a = ""

            x=0
            for i in range(int(len(b)/2)):



                for j in range(int(len(b) / 2)+x,int(len(b))):

                    #print(i, j)
                    if b[i]!=b[j]:
                        a=""
                        i=0
                        x+=1
                    if b[i]==b[j]:
                        a+=(b[j])
                        x+=1
                        i+=1
            print(a)
            hossz=len(a)
            fajlk.write("{}\n".format(hossz))
    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_15():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")
        x=[]

        for sor in fajl:
            sor=sor.strip()
            if sor=="":
                break
            else:
                x.append(sor)
        for i in x:
            fajlk.write("{}\n".format(i))



    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_16():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")
        x = []

        for sor in fajl:
            sor = sor.strip()
            for i in range(len(sor)):

                if  not sor.isupper():
                    break
            else:
                x.append(sor)
        for i in x:
            fajlk.write("{}\n".format(i))



    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_17():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")

        for sor in fajl:
            sor=sor.strip()
            szavak=sor.split(" ")
            for kis in szavak:
                if kis.islower():
                    fajlk.write("{}".format(sor))
                    return

    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_18():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")
        csapat=[]
        eredmenyek=[0,0]
        for sor in fajl:
            sor=sor.strip()
            szavak=sor.split(" ")
            felek=szavak[0].split("-")
            pont=szavak[1].split(":")
            for i in felek:
                if i not in csapat:
                    csapat.append(i)


            if felek[0]==csapat[0]:
                eredmenyek[0] += int(pont[0])
            if felek[1] == csapat[1]:
                eredmenyek[1] += int(pont[1])
            if felek[0] == csapat[1]:
                eredmenyek[1] += int(pont[0])
            if felek[1] == csapat[0]:
                eredmenyek[0] += int(pont[1])
        if eredmenyek[0]>eredmenyek[1]:
            fajlk.write("{} nyert".format(csapat[0]))
        elif eredmenyek[0]<eredmenyek[1]:
            fajlk.write("{} nyert".format(csapat[1]))
        else:
            fajlk.write("{}-{} döntetlen".format(csapat[0],csapat[1]))


    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_19():
    try:
        fajl=open("be.txt",mode="r")
        fajlk=open("ki.txt",mode="w")
        honlap=[]
        vendeg=[]
        for sor in fajl:
            sor=sor.strip()
            adatok=sor.split(" ")
            honlap.append(adatok[0])
            vendeg.append(adatok[1])
        hanyas=0
        max=0
        for sok in range(len(vendeg)):

            if int(vendeg[sok])>max:
                max=int(vendeg[sok])
                hanyas=sok
        print(max,hanyas)
        fajlk.write("{} latogattak a legtobben".format(honlap[hanyas]))

    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_20():
    try:
        fajl=open("be.txt",encoding="utf-8",mode="r")
        fajlk=open("ki.txt",encoding="utf-8",mode="w")
        varos=[]
        orszag=[]
        lakos=[]
        for sor in fajl:
            sor=sor.strip()
            adat=sor.split(";")
            varos.append(adat[0])
            orszag.append(adat[1])
            lakos.append(adat[2])
        for i in range(len(lakos)):
            if lakos[i]==max(lakos):
                fajlk.write("{} lakják a legtöbben".format(varos[i]))

    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_21():
    try:
        fajl = open("be.txt", mode="r")
        fajlk = open("ki.txt", mode="w")
        for sor in fajl:
            adat=sor.split(";")
            sum=0
            for i in range(1,len(adat)):
                sum+=int(adat[i])
            fajlk.write("{} pontjai: {}\n".format(adat[0],sum))

    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_22():
    try:
        fajl = open("be.txt", mode="r")
        fajlk = open("ki.txt", mode="w")
        nev=[]
        ido=[]
        for sor in fajl:
            adat=sor.split(";")
            nev.append(adat[0])
            ido.append(adat[2])
        for i in range(len(ido)):
            if ido[i] == min(ido):
                fajlk.write("A leggyorsabb versenyzo, a gyoztes: {}".format(nev[i]))


    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_23():
    try:
        fajl = open("be.txt", mode="r")
        fajlk = open("ki.txt", mode="w")
        mp=[]
        cm=[]
        for sor in fajl:
            sor=sor.strip()
            adat=sor.split(" ")
            mp.append(adat[0])
            cm.append(adat[1])
        x=0
        for i in range(1,len(mp)):
            print(cm[x],cm[i])
            if int(cm[x])>int(cm[i]):
                fajlk.write("NO")
                print(x)
                return
            x+=1

        fajlk.write("YES")
    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_24():
    try:
        fajl = open("be.txt", mode="r")
        fajlk = open("ki.txt", mode="w")
        tcm=0
        cscm=0
        sorok=[]
        for sor in fajl:
            sor=sor.strip()
            sorok.append(sor)

        teki=sorok[1].split(" ")
        csiga=sorok[2].split(" ")

        for cm in teki:
            tcm+=int(cm)
        for ccm in csiga:
            cscm+=int(ccm)

        if tcm>cscm:
            fajlk.write("{}\nTURTLE".format(2*tcm))
        elif cscm>tcm:
            fajlk.write("{}\nSNAIL".format(2*cscm))
        else:
            fajlk.write("{}\nDRAW".format(tcm+tcm))

    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_25():
    try:
        fajl = open("be.txt", mode="r")
        fajlk = open("ki.txt", mode="w")
        sorok=[]
        for sor in fajl:
            sor=sor.strip()
            sorok.append(sor)
        A=[]
        M=[]
        for i in range(1,int(sorok[0])+1):
            szo=sorok[i].split(":")
            A.append(szo[0])
            M.append(szo[1])

        Adb=0
        Ax=[]
        for a in A:
            if a not in Ax:
                Adb+=1
                Ax.append(a)
        Mx=[]
        Mdb=0
        for m in M:
            if m not in Mx:
                Mdb+=1
                Mx.append(m)

        fajlk.write("{}\n{}".format(Adb,Mdb))
    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close

def fel_26():
    try:
        fajl1 = open(sys.argv[1], mode="r")
        fajl2 = open(sys.argv[2], mode="r")
        fajlk = open("ki.txt", mode="w")
        sorok1=[]
        sorok2 = []
        for sor in fajl1:
            sor=sor.strip()
            sorok1.append(sor)
        for sor in fajl2:
            sor=sor.strip()
            sorok2.append(sor)
        print(sorok1,sorok2)
        mas=[]
        for i in sorok1:
            if i not in sorok2:
                mas.append(i)
        dbe=0
        dbk=0
        for e in sorok1:
            dbe+=1
        for k in sorok2:
            dbk+=1

        fajlk.write("{} {}\n".format(dbe,dbk))
        for m in mas:
            fajlk.write("{}\n".format(m))

    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl1.close
        fajl2.close
        fajlk.close

def fel_27():
    try:
        fajl = open(sys.argv[3], mode="r")
        fajlk = open("ki.txt", mode="w")
        cim=[]
        iro=[]
        db=[]
        for sor in fajl:
            sor=sor.strip()
            adatok=sor.split(":")
            cim.append(adatok[0])
            iro.append(adatok[1])

        for x in iro:
            d = 0
            idb=x.split(",")
            for y in idb:
                d+=1
            db.append(d)

        for minimum in range(len(db)) :
            if db[minimum]==min(db):
                fajlk.write("{}\n".format(cim[minimum]))
                
    except FileExistsError:
        print("nem létezik a fájl")
    except Exception as e:
        print("Valami van", e)
    finally:
        fajl.close
        fajlk.close
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
    #print(konverzio(1101, 2, -1))
    #fel_10()
    #fel_11()
    #fel_12()
    #fel_13()
    #fel_14()
    #fel_15()
    #fel_16()
    #fel_17()
    #fel_18()
    #fel_19()
    #fel_20()
    #fel_21()
    #fel_22()
    #fel_23()
    #fel_24()
    #fel_25()
    #fel_26()
    fel_27()
main()