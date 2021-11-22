def rysujDomek(a, x, y):

    print(4 * " " + 2 * x + 4 * " ")
    print(3 * " " + 4 * x + 3 * " ")
    print(2 * " " + 6 * x + 2 * " ")
    print(1 * " " + 8 * x + 1 * " ")
    while a>0:
        print(10 * y)
        print(3 * y + 4 * " " + 3 * y)
        print(3 * y + 4 * " " + 3 * y)
        print(10 * y)
        a = a-1

rysujDomek(3, "^", "#")