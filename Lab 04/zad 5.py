imiona = input()
imiona = imiona.split(", ")
print(imiona)
kobiety = []
for i in imiona:
    if i[-1] == "a":
        kobiety.append(i)
print(kobiety)