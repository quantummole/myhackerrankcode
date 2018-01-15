#!/bin/python

import sys

def matrixRotation(matrix,m,n,r):
    num_steps = min(m,n)/2
    new_matrix = []
    for i in range(0,num_steps) :
        values = matrix[i][i:n-i] + map(lambda x : x[n-1-i],matrix[i+1:m-i]) +matrix[m-1-i][i:n-i-1][-1::-1]+ map(lambda x : x[i],matrix[m-2-i :i:-1])
        total_values = max(1,2*(m+n) - 4*(2*i + 1))
        net_shift =  r % total_values
        shifted = values[net_shift:] + values[0:net_shift]
        matrix[i][i:n-i] = shifted[0:n-2*i]
        matrix[m-1-i][i:n-i] = shifted[m+n - 4*i -2 : m+n - 4*i -2 +n - 2*i ][-1::-1]
        for j,x in enumerate(shifted[n-2*i : m + n -4*i -2]) :
            matrix[i+1+j][n-1-i] = x
        for j,x in enumerate(shifted[ m+n - 4*i -2 +n - 2*i :]) :
            matrix[m-2-i-j ][i] = x
    return matrix 
        
if __name__ == "__main__":
    m, n, r = raw_input().strip().split(' ')
    m, n, r = [int(m), int(n), int(r)]
    matrix = []
    for matrix_i in xrange(m):
        matrix_temp = map(int,raw_input().strip().split(' '))
        matrix.append(matrix_temp)
    ans = matrixRotation(matrix,m,n,r)
    for row in ans :
        t = reduce(lambda x,y : str(x) + ' '+ str(y),row)
        print t
