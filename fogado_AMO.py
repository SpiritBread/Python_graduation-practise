f=open('fogado.txt')
a=f.read().split('\n')
a.pop()
#print(a)
for i in range(len(a)):
    a[i]=a[i].split(' ')
print(a)
f.close()

print('2. feladat')     #hány elemű a tömb?
print('Foglalások száma:',len(a))

print('\n3. feladat')   #egy tanár időpontfoglalásai
nev=input('Adjon meg egy nevet: ')
db=0
for i in range(len(a)):
    if a[i][0]+' '+a[i][1]==nev:
        db+=1
if db==0:
    print('A megadott néven nincs időpontfoglalás.')
else:
    print(nev,'néven',db,'időpontfoglalás van.')

print('\n4. feladat') #megadott időpontban fogaltak neve
ido=input('Adjon meg egy érvényes időpontot (pl. 17:10): ')
b=[]
for i in range(len(a)):
    if a[i][2]==ido:
        b.append(a[i][0]+' '+a[i][1])
#print(b)
for i in range(0,len(b)-1):
    for j in range(len(b)-1,i,-1):
        if b[j]<b[i]:
            c=b[j]
            b[j]=b[i]
            b[i]=c
for i in range(len(b)):
    print(b[i])

ido=ido[0]+ido[1]+ido[3]+ido[4] #pl 17:40, ahol a kettőspontot kihagyjuk
ujf=open(ido+'.txt','w')
for i in range(len(b)):
    ujf.write(b[i]+'\n')
ujf.close()

print('\n5. feladat')   #legkorábbi foglalt időpont adatai
min=a[0][3]
hol=0
for i in range(len(a)):
    if a[i][3]<min:
        hol=i
print('Tanár neve:',a[hol][0]+' '+a[hol][1])
print('Foglalt időpont:',a[hol][2])
print('Foglalás ideje:',a[hol][3])

print('\n6. feladat')   #Barna Eszter szabad időpontjai, mikor távozhat legkorábban
c=[]
for i in range(len(a)):
    if a[i][0]== 'Barna' and a[i][1]=='Eszter':
        c.append(a[i][2])
d=[]
for i in range(16,18):
    d.append(str(i)+':00')
    for j in range(10,60,10):
        d.append(str(i)+':'+str(j))
for i in range(len(d)):
    ures=True
    for j in range(len(c)):
        if d[i]==c[j]:
            ures=False
        if ures:
            print(d[i])
#ide még kell az hogy mikor távozhat legkorábban

#7. tanáronként hány db foglalás van?
