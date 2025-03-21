# Python Program to Add Two Matrices
A =[[1,5,8],
    [4,6,7],
    [9,5,3]]
B = [[2,3,4],
     [6,2,1],
     [3,7,4]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result [i][j]=A[i][j]+B[i][j]

for r in result:
    print(r)
