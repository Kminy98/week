# n=8
# tri=[]
# for i in range(n):
#     tri.append([])
#     tri[i].append(1)
    
#     for j in range(1,i):
#         tri[i].append(tri[i-1][j-1]+tri[i-1][j])
#     if i > 0:
#         tri[i].append(1)
#     print('tri=',tri)


def pascal(tri,n):
    if len(tri) == n: #j=8 == 8
        return tri #
    print(n)
    next_tri=[1] * n
    print(next_tri)
    for j in range(1,n+1): #j=1,2,3,4,5,6,7,8
        next_tri[j] = (tri[j-1]+tri[j])
      # next_tri[j] = (tri[1-1]+tri[1])
    # next_tri[j-1]=1
    tri=next_tri
    return pascal(tri,n)



# for j in range(1,8):
#     print(j)
