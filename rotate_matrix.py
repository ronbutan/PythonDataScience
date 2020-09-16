def matrix_rotate(matrix, degrees, clockwise = True): # don't change the function definition and the parameter list, otherwise no point will be given.
    if degrees == 0:
        return matrix
    limit = len(matrix)
    

n_dim = 3
mat = [[n_dim*i+j for j in range(n_dim)] for i in range(n_dim)]

print(f'orginal matrix: {mat}')
matrix_rotate(mat, 0, False)