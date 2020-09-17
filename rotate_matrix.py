def matrix_rotate(matrix, degrees, clockwise = True): # don't change the function definition and the parameter list, otherwise no point will be given.
    rotateindex = [0,1,2,3]
    rlen = len(rotateindex)
    n = len(matrix)
    i = int((degrees / 90) % rlen)
    if not clockwise:
        i = -i
    if rotateindex[i] == 1:
        matrix = [[row[i] for row in matrix[::-1]]for i in range(0,n)]
    elif rotateindex[i] == 2:
        matrix = [matrix[i][::-1] for i in range(n-1,-1,-1)]
    elif rotateindex[i] == 3:
        matrix = [[row[i] for row in matrix]for i in range(n-1,-1,-1)]
    print(matrix)
    
n_dim = 3
mat = [[n_dim*i+j for j in range(n_dim)] for i in range(n_dim)]

print(f'orginal matrix: {mat}')
matrix_rotate(mat, 180, False)