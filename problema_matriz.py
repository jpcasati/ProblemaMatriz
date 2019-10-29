def gerar(n):

    r = round(n/2)

    m = [[0 for i in range(n)] for j in range(n)]

    i = 0
    f = n
    for k in range(r):
        for j in range(i, f):
            m[k][j] = 1
        f = f-1
        i = i+1

    i = r-2

    if (n % 2) == 0:
        i = r-1

    f = r+1

    for k in range(r, n):
        for j in range(i, f):
            m[k][j] = 1
        f = f+1
        i = i-1

    print('Matriz de ' + str(n) + ' por ' + str(n) + ':')

    for r in m:
        print(' '.join(map(str, r)))

    print('\n')
    return m



def teste(matriz1, matriz2):

    m1 = [[1, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1]]

    m2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    if((matriz1 == m1) and (matriz2 == m2)):
        return True
    else:
        return False

print(teste(gerar(7), gerar(10)))