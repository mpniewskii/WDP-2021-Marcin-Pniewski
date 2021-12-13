def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #przypadek bazowy dla macierzy 2x2
    if len(m) == 2:
        return len(m)

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

m = [[2, 1, 3, 0], [1, 0, 2, 3], [3, 2, 0, 1], [2, 0, 1, 3]]
d = getMatrixDeternminant(m)
print(d)