import sys

N, X = map(int, sys.stdin.readline().split())

temp = list(map(int, sys.stdin.readline().split()))

for j in range(0,N):
    if(temp[j]<X):
        print(temp[j])












# 런타임에러
# import sys
#
# N, X = map(int, sys.stdin.readline().split())
# temp = []
# for i in range(1, N+1):
#     num = int(sys.stdin.readline())
#     temp.insert(i, num)
#
#
# for j in range(0,N):
#     if(temp[j]<X):
#         print(temp[j])