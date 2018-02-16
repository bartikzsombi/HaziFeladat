import codecs as cod
def legH(fajl_nev):
    fajl=cod.open(fajl_nev,encoding='utf-8' ,mode="r")
    max=0
    max_sor=""
    for sor in fajl:
        sor=sor.strip()
        if sor[0].isupper() and len(sor)>max:
            max= len(sor)
            max_sor=sor
    print(max, max_sor)
    fajl.close()

def olvas():
    fajl=open("bel.txt",mode="r")
    for sor in fajl:
        if "   " in sor:
            fajl=open("kil.txt", mode="w")
            fajl.write(sor)
            fajl.close()
            break
def fel7(lista,betu):
    li=[]
    fajl=open("kil.txt",mode="w")
    for i in lista:
        if i [0]==betu:
            li.append()
    fajl.write(str(li))
    fajl.close()



def main():
    #legH("bel.txt")
    #olvas()
    fel7(["alma","ananász","barack","meggy"],"a")
main()
