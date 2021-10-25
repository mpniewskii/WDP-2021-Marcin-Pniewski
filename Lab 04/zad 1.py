s = "programujemy w pythonie"

#wyswietlanie
print(s)
print (len(s))
print(s[2:7])
print(s[-8:])
print(s[1])

#duze-male litery
s2 = s.upper()
print(s2)
s3 = s2.lower()
print(s3)

#rozdzielanie stringow
r = "Anna, Bartek, Celina, Dawid"
x1 = r.split(",")
print(x1)
r2 = r.replace(" ", "")
print(r2)
x1 = r2.split(",")
print(x1)

#sklejanie
imie = "Jan"
nzawisko = 'Kowalski'
imnaz = imie + " " + nzawisko
print(imnaz)