def permute(a, l, r):
    z = []
    if l == r and a not in z:
        z.append(a)
        print(a)
    else:
        for i in range(l, r+1):
            if a[l] != a[i]:
                a[l], a[i] = a[i], a[l]
                permute(a, l+1, r)
                a[l], a[i] = a[i], a[l]


a = ['A', 'B', 'C', 'B']
permute(a, 0, len(a)-1)
