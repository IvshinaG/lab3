k=open('D:/3.Galina/1 курс/Прогр/2 сем/synonyms.txt')
a=[]
h=True
while h:
    m=str(k.readline())
    if not m:
        h=False
    else:
        m=m.lower()
        #print(m)
        a.append(m)
s=input("Введите слово: ")
s=s.lower()
str=False
for i in range (len(a)):
    #print(a[i])
    m=a[i]
    if s in m:
        str=i
        v=m.find(s)
        pv=v+len(s)
        if v==0:
            print("Синонимы слова", s, m[pv:])
        else:
            pp=m.find(" ")
            print("Синонимы слова", s,"-", m[:pp], ";", m [pp+3:v], m[pv:])
        break
it=''
if str==False:
    print("Слова не существует в словаре")
