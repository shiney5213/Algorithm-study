import numpy as np

a = np.zeros((15,14), dtype = np.uint32)


for i in range(len(a[0])):
    a[0][i]= i+1

for i in range(1, a.shape[0]):
    for j in range(0, a.shape[1]):
        a[i,j]= a[i][j-1]+a[i-1][j]


t = int(input())

k = int(input())
n = int(input())-1

print(f'{k}층 {n+1}호에는 {a[k][n]}명 살고있어요')