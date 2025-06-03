def matr(s):
    for i in range(0,4):
        print(s[i])


a=[[1,2,3,1,2],
   [2,3,2,2,-1],
   [3,2,1,-2,2],
   [-3,2,1,4,2],
   [3,4,-4,2,0]]
b=[[2,1,3,4,2],
   [3,4,2,6,2],
   [1,2,3,2,-1],
   [3,5,3,2,1],
   [2,4,2,4,1]]
c=[[],[],[],[],[]]
for i in range(0,5):
    for v in range(0,5):
        c[i].append(a[i][v]+b[i][v])
matr(a)
print('       +')
matr(b)
print('       =')
matr(c)