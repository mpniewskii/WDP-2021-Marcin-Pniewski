waga = 75
wzrost = 180

#sposob przez format
s = "Jan Kowalski (waga: {}, wzrost: {})"
s = s.format(waga, wzrost)
print(s)

#sposob przez konwersje liczby na string
waga_txt = str(waga)
wzrost_txt = str(wzrost)
s = "Jan Kowalski (waga: " + waga_txt + ", wzrost: " + wzrost_txt +")"
print(s)